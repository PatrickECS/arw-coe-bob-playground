---
name: lab-health-check
description: General health check and troubleshooting of the Arrow EU lab OpenShift clusters (dgx, wxai, gaudi2, ove01, northcode, timestamp, epical01, wxorch02 and others) using the openshift-lab MCP server. Use when asked what is wrong with a cluster, why something fails, or for a status report of one or all lab clusters.
---

Environment

- The openshift-lab MCP server has one context per cluster. Use the context list from the server as the list of clusters, do not assume it.
- isf is the management cluster. It runs IBM Fusion HCI and hosts the HyperShift control planes of the other clusters.
- dgx runs GPU workloads, RHOAI model serving and the self-hosted IBM Bob.
- ove01 runs OpenShift Virtualization VMs, including admin jump hosts, and is itself a nested hosted cluster.
- Access is read-only. Never claim to have changed anything. Suggest oc commands for the user instead.
- Never print passwords, tokens, API keys or private keys.

When to use another skill

- For isf, or any question about Fusion HCI, its storage, services or backups, use the fusion-health-check skill instead. In an all-clusters check, run fusion-health-check for isf and this skill for the other clusters.
- For background on Fusion features, the fusion-hci-systems skill can explain, but it is never evidence of the current state.

Rules

- Report only what you actually read. If a check fails or a resource cannot be read, write "Not checked" with the reason. Never write Healthy without having read the resources that prove it.
- If a cluster cannot be reached (timeout, connection refused), report it as Unreachable and continue with the others. Do not treat that as a problem inside the cluster.

Checks for one cluster

1. ClusterVersion (config.openshift.io/v1): version and the Available, Progressing and Failing conditions.
2. ClusterOperators (config.openshift.io/v1): list any with Available=False, Degraded=True or Progressing=True.
3. Nodes: the Ready condition and MemoryPressure, DiskPressure, PIDPressure. Usage figures alone do not prove a node is healthy.
4. Pods in all namespaces that are not Running or Succeeded, grouped by namespace. Call out CrashLoopBackOff, ImagePullBackOff, Pending and high restart counts.
5. PVCs that are not Bound.
6. Warning events from the last hour, grouped by reason and namespace. Treat repeated probe failures and BackOff as problems, not noise.
7. Only when relevant to the question or the cluster: on dgx, check InferenceServices and LLMInferenceServices (serving.kserve.io) and the ibm-bob-app namespace. On ove01, check VirtualMachines (kubevirt.io) not Running.

Check for all clusters

1. Run fusion-health-check for isf.
2. For each other cluster, do a short check: reachability, ClusterVersion, ClusterOperators, nodes not Ready, and the number of pods not running.
3. Go deeper with the full checks only on clusters that show problems.

Report format

1. Summary table: cluster, status (OK, Warning, Problem, Unreachable or Not checked), main issues in one line.
2. For each Warning and Problem: what is wrong, the evidence (the resource and field you read), the likely impact, and read-only oc commands to investigate further.
3. Healthy clusters get one line only.
4. A short list of what was not checked, and why.