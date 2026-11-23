---
name: fusion-health-check
description: Health check of the IBM Fusion HCI system isf (the management cluster) using the openshift-lab MCP server. Use for any question about the health or status of isf or Fusion HCI, its storage (FDF, ODF, Ceph, Storage Scale), Fusion services, backups, disaster recovery, hosted clusters or virtual machines.
---

Rules

- Use only the openshift-lab MCP server with context isf. Do not use fusion-lab.
- Always use the exact apiVersion and kind from the tables below. Do not guess versions.
- If a call fails, quote the exact error message in the report. Write "Not available" only if the error says the resource type does not exist. A Forbidden error means "Not checked (no permission)". Any other error means "Not checked" with the error.
- An empty list is not an error. It means "Not configured" or "None", not "Not available".
- Report only what you actually read. Never write Healthy, Ready or Not installed without having read the resource that proves it.
- A namespace existing proves nothing. Judge health from status fields, conditions and pods.
- Read-only: never claim to have changed anything. Suggest oc commands for the user instead.
- Never print passwords, tokens, API keys or private keys.

Keep the data small (the model has a limited context window)

- Work through the areas one at a time. After each area, write a short summary and do not carry the raw data forward.
- Never list all pods, events or PVCs in all namespaces at once. Query only the namespaces that matter, or use label and field selectors.
- Prefer list output over full YAML. Fetch the YAML of a single resource only when you need a specific status field.
- For counts (VMs, PVCs, backups), report the numbers and list only the items that are not OK.

1. Platform

| apiVersion | kind | Check |
| --- | --- | --- |
| config.openshift.io/v1 | ClusterVersion | Version; Available, Progressing, Failing conditions |
| config.openshift.io/v1 | ClusterOperator | Any with Available=False, Degraded=True or Progressing=True |
| v1 | Node | Ready condition; MemoryPressure, DiskPressure, PIDPressure |

2. Fusion core

| apiVersion | kind | Check |
| --- | --- | --- |
| systemhealth.isf.ibm.com/v1 | HealthManager | Fusion's own health view. Report its status and every problem it lists. Most important Fusion check. |
| prereq.isf.ibm.com/v1 | SpectrumFusion | Overall Fusion status |
| service.isf.ibm.com/v1 | FusionServiceInstance | Every installed Fusion service and its status. Source of truth for which services are installed. |
| update.isf.ibm.com/v1 | UpdateManager | Pending or failed updates |
| network.isf.ibm.com/v1 | Switch, Link, Vlan | Anything not OK |
| monitoring.isf.ibm.com/v1 | ComputeMonitoring | Anything not OK |

Status fields of isf.ibm.com resources vary. Read status.conditions and status.phase or status.state, and quote what they say rather than guessing what they mean.

3. Storage

| apiVersion | kind | Check |
| --- | --- | --- |
| ceph.rook.io/v1 | CephCluster | status.ceph.health (HEALTH_OK, HEALTH_WARN, HEALTH_ERR). If not OK, quote status.ceph.details. Capacity used and total if available. |
| ocs.openshift.io/v1 | StorageCluster | status.phase must be Ready |
| ceph.rook.io/v1 | CephBlockPool, CephFilesystem, CephObjectStore | Phase of each |
| odf.isf.ibm.com/v1 | OdfCluster, OdfManager | Fusion's view of FDF |
| storage.isf.ibm.com/v1 | StorageService, Scale | Fusion storage services and Storage Scale, if any exist |
| cns.isf.ibm.com/v1 | ScaleCluster, ScaleManager | Storage Scale cluster status, if any exist |
| v1 | PersistentVolumeClaim | Count Bound, Pending, Lost; list Pending and Lost |

4. Backup and Restore (namespace ibm-backup-restore)

| apiVersion | kind | Check |
| --- | --- | --- |
| v1 | Pod (in ibm-backup-restore) | Any not Running or Completed |
| data-protection.isf.ibm.com/v1alpha1 | Backup | Latest backup per policy, failed backups in the last 24 hours, latest failure reasons |
| data-protection.isf.ibm.com/v1alpha1 | BackupStorageLocation | Whether each location is available |
| data-protection.isf.ibm.com/v1alpha1 | BackupPolicy, PolicyAssignment | What is protected |
| data-protection.isf.ibm.com/v1alpha1 | Restore | Failed restores in the last 24 hours |

5. Disaster recovery

| apiVersion | kind | Check |
| --- | --- | --- |
| metrodr.isf.ibm.com/v1 | MetroDR | Status, if any exist |
| rdr.isf.ibm.com/v1 | RegionalDr | Status, if any exist |

If both lists are empty, report "DR not configured". That is not a problem.

6. Hosted clusters

| apiVersion | kind | Check |
| --- | --- | --- |
| hypershift.openshift.io/v1beta1 | HostedCluster | Available and Degraded conditions, version, per cluster |
| hypershift.openshift.io/v1beta1 | NodePool | Ready versus desired replicas, and conditions |
| v1 | Pod (in clusters-* namespaces) | CrashLoopBackOff, especially capi-provider, which manages the NodePools from isf. Treat repeated capi-provider failures as a problem on isf. |

7. Virtualization

| apiVersion | kind | Check |
| --- | --- | --- |
| hco.kubevirt.io/v1beta1 | HyperConverged | Available and Degraded conditions |
| kubevirt.io/v1 | VirtualMachine | Total, Running, Stopped, and any in error states, grouped by namespace |
| cdi.kubevirt.io/v1beta1 | DataVolume | Any not Succeeded |

8. Warning events

Warning events from the last hour in the namespaces with problems found above, grouped by reason. Treat repeated probe failures and BackOff as problems, not noise.

Report format

1. Summary table with one row per area (Platform, Fusion core, Storage, Backup, Disaster recovery, Hosted clusters, Virtualization): status (OK, Warning, Problem, Not configured or Not checked) and a one-line reason.
2. Overall status: Healthy only if no area is Warning or Problem and nothing important is Not checked. Otherwise Warning or Problem.
3. For each Warning and Problem: what is wrong, the evidence (the resource and field you read), the likely impact, and read-only oc commands to investigate further.
4. A list of what was not checked, with the exact error for each.
5. The fusion-hci-systems skill may be used to explain what a finding means, but never as evidence of the current state.

Run the check in rounds (required)

The full check does not fit in one answer. Always split it into rounds, one round per answer, and stop after each round:

- Round 1: Platform and Fusion core.
- Round 2: Storage, Backup and Disaster recovery.
- Round 3: Hosted clusters, Virtualization and Warning events.
- Round 4: The final summary table and overall status, built from the summaries of rounds 1 to 3.

After each round, write a short summary of that round (OK, Warning or Problem per area, with the key evidence), then ask the user to say "continue". Do not start the next round in the same answer.

How to fetch data cheaply

- Use resources_list (table output) first for every resource type. Only use resources_get (full YAML) on single resources that look unhealthy in the list, or when a needed status field is not in the table.
- Never use resources_get on all HostedClusters, FusionServiceInstances or HealthManagers. Get only the ones you need, one at a time.
- For pods, use pods_list_in_namespace with only the namespaces that matter (openshift-storage, ibm-backup-restore, ibm-spectrum-fusion-ns). For the clusters-* namespaces, list only the capi-provider pods with labelSelector, or only pods with high restart counts.
- For events, use events_list on one namespace at a time, and only for namespaces where you already found a problem.