---
name: fusion-hci-systems
description: "IBM Fusion HCI 2.13.x / 2.14.x product expert. Use when answering questions about IBM Fusion HCI architecture, hardware, installation, storage (Global Data Platform / Fusion Data Foundation), services (Backup & Restore, Data Cataloging, Content-Aware Storage, Software Hub, watsonx.data), disaster recovery, high availability, upgrading, troubleshooting, and accelerating AI workloads on Fusion infrastructure. Also use when generating knowledge-base content for ai-tools/product-context/fusion or planning new documentation hierarchies. Trigger phrases: fusion hci, ibm fusion, global data platform, fusion data foundation, content-aware storage, CAS, gdp, isf, storage scale, fusion upgrade, fusion install, fusion troubleshoot, fusion services, fusion ha, fusion dr, accelerating ai on fusion, model as a service fusion, mcp fusion, watsonx.data fusion."
---

# IBM Fusion HCI 2.13.x / 2.14.x — Product Expert

Knowledge base built from the official IBM Fusion HCI 2.13.x and 2.14.x documentation. Use this skill to answer product questions about either release, generate documentation content, and enrich the `ai-tools/product-context/fusion` knowledge hierarchy.

> **Version coverage:** This skill covers both 2.13.x and 2.14.x. Content defaults to 2.14 (current). Where behaviour differs between releases, a `> **Changed in 2.14:**` or `> **2.14 only:**` callout marks the difference. For a full list of what changed, see [`release-delta.md`](chapters/release-delta.md).

---

## What IBM Fusion HCI Is

**IBM Fusion HCI** is a purpose-built, hyper-converged infrastructure appliance that combines bare-metal Red Hat OpenShift Container Platform with IBM Fusion software. It integrates compute, networking, and storage resources into a single rack-based unit, optimized for containerized workloads, AI, and hybrid cloud data management.

Two deployment models:
- **IBM Fusion HCI** — appliance form-factor, hardware + software co-delivered
- **IBM Fusion** — software-only, runs on existing customer hardware

---

## Architecture Mental Model

```
┌─────────────────────────────────────────────────────┐
│                  Fusion Services Layer               │
│  GDP · FDF · B&R · Data Cataloging · CAS · Software Hub │
├─────────────────────────────────────────────────────┤
│             Fusion Infrastructure Mgmt Layer         │
│   Node lifecycle · Networking · Storage mgmt · UI    │
├─────────────────────────────────────────────────────┤
│        Fusion Base (OpenShift Container Platform)    │
│   Serviceability · Observability · Event manager     │
├─────────────────────────────────────────────────────┤
│                 Hardware Layer                       │
│   Compute servers · GPU servers · Switches · PDUs    │
└─────────────────────────────────────────────────────┘
```

**Key principle:** Every layer builds on OpenShift. Fusion is *not* a hypervisor replacement — it is an OpenShift-native data and lifecycle management platform.

---

## Core Frameworks

### 1. Storage Type Decision Framework

Two mutually exclusive storage backends — choose one per cluster:
- **Global Data Platform (GDP / IBM Storage Scale)** — file + object, erasure coding, Metro-DR (sync replication, <40ms RTT). Best for AI/HPC/analytics and Metro-DR scenarios.
- **Fusion Data Foundation (FDF / Ceph-based)** — block + file + object, replica-3 or erasure coding (FDF 4.21+), Regional-DR (async). Best for general containerized workloads and Regional-DR.

**Rule:** GDP = Metro-DR only. FDF = Regional-DR only. Never mix DR topologies in one cluster.

### 2. Installation Stages Model

IBM Fusion HCI installation is a two-stage sequential process:
- **Stage 1 (Network Setup)** — SSR-led: switches, VLANs, bond aggregation, DHCP/DNS, NTP. Outputs: service node URL for Stage 2.
- **Stage 2 (Software Installation)** — Customer-led: license acceptance, registry config, OpenShift cluster bootstrap, Fusion operator install.

Post-install: add nodes → configure storage → install services.

### 3. Upgrade Sequence Rule

Strict ordering is mandatory:
1. IBM Fusion HCI management software
2. Storage service (GDP or FDF)
3. Backup & Restore
4. IBM Data Cataloging
5. OpenShift Container Platform (optional)

Skipping or reordering causes failures. Hotfix review is required before any upgrade.

### 4. Service Tier Model

Services are optional, additive, and independently installable:
| Service | Purpose | Depends on | Version |
|---|---|---|---|
| Global Data Platform | File/object storage | OpenShift | 2.13+ |
| Fusion Data Foundation | Block/file/object storage | OpenShift | 2.13+ |
| Backup & Restore | App protection, hub/spoke | Storage service | 2.13+ |
| Data Cataloging | Metadata indexing, AI tagging | Storage service | 2.13+ |
| Content-Aware Storage (CAS) | RAG/NLP/vector stores | GDP or FDF | 2.13+ |
| Software Hub | watsonx.ai, watsonx Orchestrate deployment | OpenShift | 2.13+ |
| Lakehouse-Table | Iceberg catalog + object storage | FDF (tech preview) | 2.13+ |
| watsonx.data | On-prem lakehouse, multi-format analytics | GDP or FDF object storage | **2.14 only** |

### 5. Disaster Recovery Topology Framework

| Type | Replication | Latency Req | Storage | HCP Support | Version |
|---|---|---|---|---|---|
| Metro-DR | Synchronous | <40ms RTT | GDP only | — | 2.13+ |
| Regional-DR | Asynchronous | No RTT limit | FDF replica-3 | 2AZ+arbiter (2.14) | 2.13+ |
| Regional-DR (EC storage classes) | Asynchronous | No RTT limit | FDF EC | — | **2.14 only** |
| Storage-agnostic DR | Asynchronous | No RTT limit | FDF or 3rd-party | — | **2.14 only** |

### 6. High Availability Modes

- **Single-rack HA** — 3+ nodes with MLAG-paired switches
- **Multi-rack HA** — multiple racks connected via spine switches
- **3-zone HA** — three independent failure domains
- **Two AZ + arbiter** — two active AZs, one tiebreaker in a third zone
- **Hosted Control Plane (HCP)** — multi-cluster with decoupled control planes

---

## Key Principles

- **Minimum viable rack**: 3 compute-storage servers (control plane nodes), 2 high-speed switches (MLAG pair), 2 management switches
- **No drive capacity mixing**: cannot mix 7.68 TB and 3.84 TB NVMe drives within a rack
- **No GPU model mixing**: cannot mix GPU card models within a single GPU server node
- **Service node**: critical lifecycle management component (Stage 1, UI, log collection, firmware upgrades); Gen1 and Gen2 racks can add a service node post-deployment without reinstallation
- **Image signing**: all IBM Fusion images are GPG-signed; verification uses `skopeo` + `gpg2`
- **Password rotation**: hardware credentials auto-rotate; external Vault integration supported
- **Call Home**: automatically opens IBM Support tickets for whitelisted Critical events

---

## AI-Enhanced Integration

### 2.14 additions

- **watsonx.data service** — on-prem lakehouse for governing and analysing enterprise data across formats; integrates with GDP and FDF object storage
- **S3 Vectors in MCG** — FDF 4.22 adds native vector storage in Multicloud Object Gateway; enables RAG pipelines without an external vector database
- **Accelerating AI with Fusion** — full platform guide for AI workloads: GitOps delivery, GPU runtimes (NVIDIA L40S / H100 NVL), MaaS, MCP data connectivity, Fusion Developer Hub, NVIDIA AI blueprints (see ch17)

### 2.13 integrations (still current)

- **MCP server for CAS** — AI assistants can query vector stores via natural language
- **IBM Data Cataloging MCP server** — unified tool catalog and data management without direct LLM-to-tool integrations
- **AI-powered content-based tagging** — LLM + GPU classify unstructured data, generate metadata tags automatically
- **Red Hat OpenShift Lightspeed** — AI-enabled observability and smart agent integration

---

## What's New in 2.14.x

Key additions in 2.14.0:
- **FDF 4.22** — erasure coding for all three storage types (RBD, CephFS, RGW); S3 Vectors in MCG; storage-agnostic DR operator; HCP on 2AZ+arbiter
- **FIPS 140-3 compliance** — FIPS 140-3 cryptographic modules for data at rest and in transit
- **New hardware** — Lenovo SR650a V4 128-core server (model 9155-C25)
- **watsonx.data service** — on-prem lakehouse (new service)
- **Alert-based Call Home** — Prometheus alerts automatically open IBM Support tickets with log bundles
- **B&R observability** — Prometheus metrics + Grafana dashboards for backup jobs and policies
- **Regional-DR expanded** — EC storage classes and HCP on 2AZ+arbiter now supported
- **Accelerating AI with Fusion** — new platform guide for running AI workloads (ch17)

---

## What's New in 2.13.x

Key additions in 2.13.0:
- Simplified upgrade: 2.11.x → 2.13.0 direct (specific configs, bypass 2.12.x)
- Automated service node upgrades via upgrade agent
- Integrated Vault-based secret management
- Automated hardware credential rotation
- Automated rack reset (factory restore)
- Preinstalled images (no pre-install mirroring needed for offline environments)
- CAS: MCP support, NFS data source, vector store file listing API, zero-trust network policies
- FDF 4.21: CNSA integration, erasure coding (RBD, min 6 nodes), multi-volume consistency groups
- Data Cataloging: AI-powered content tagging, one-click CAS integration, data insights dashboards
- Enhanced log sanitization (auto-masks IPs, MACs, DNS info)
- Enhanced node addition UI with prechecks (Ready/Not Ready labels)

See [`release-delta.md`](chapters/release-delta.md) for a structured comparison of all 2.13→2.14 changes.

---

## Chapter Index

| Chapter | File | Topic |
|---|---|---|
| 1 | [ch01-whats-new-and-overview.md](chapters/ch01-whats-new-and-overview.md) | What's new in 2.13.x and 2.14.x, product overview, AI integration |
| 2 | [ch02-hardware.md](chapters/ch02-hardware.md) | Hardware components: compute, GPU, switches, storage, PDUs, service node |
| 3 | [ch03-planning-and-prerequisites.md](chapters/ch03-planning-and-prerequisites.md) | Site readiness, networking, system requirements, mirroring, activation |
| 4 | [ch04-installing.md](chapters/ch04-installing.md) | Two-stage install, rack reset, Quay, validation, service install/uninstall, FIPS |
| 5 | [ch05-storage.md](chapters/ch05-storage.md) | Storage deployment combinations, PVs, storage classes, EC options |
| 6 | [ch06-fusion-services.md](chapters/ch06-fusion-services.md) | Service overview, FDF 4.22, CAS, Software Hub, Lakehouse-Table, watsonx.data |
| 7 | [ch07-global-data-platform.md](chapters/ch07-global-data-platform.md) | GDP install, config, remote mount, Scale integration, MCG |
| 8 | [ch08-backup-and-restore.md](chapters/ch08-backup-and-restore.md) | B&R architecture, policies, hub/spoke, Prometheus metrics, Grafana dashboards |
| 9 | [ch09-data-cataloging.md](chapters/ch09-data-cataloging.md) | Data Cataloging install, metadata policies, AI tagging, REST API |
| 10 | [ch10-disaster-recovery.md](chapters/ch10-disaster-recovery.md) | Metro-DR, Regional-DR (incl. EC classes), storage-agnostic DR, topology view |
| 11 | [ch11-high-availability.md](chapters/ch11-high-availability.md) | HA topologies, multi-rack, Hosted Control Plane, 2AZ+arbiter HCP |
| 12 | [ch12-advanced-workloads-and-virtualization.md](chapters/ch12-advanced-workloads-and-virtualization.md) | OpenShift Virtualization, Cloud Paks, watsonx, Maximo, Db2 Warehouse |
| 13 | [ch13-administering.md](chapters/ch13-administering.md) | Node management, storage admin, firmware upgrades, network admin |
| 14 | [ch14-user-management-and-api.md](chapters/ch14-user-management-and-api.md) | User management, IBM Fusion UI, API reference |
| 15 | [ch15-upgrading.md](chapters/ch15-upgrading.md) | Upgrade sequence, prerequisites, service upgrades, firmware, OCP upgrade, rolling upgrades |
| 16 | [ch16-troubleshooting-and-error-codes.md](chapters/ch16-troubleshooting-and-error-codes.md) | Serviceability, alert-based Call Home, events, error codes, log collection |
| 17 | [ch17-accelerating-ai.md](chapters/ch17-accelerating-ai.md) | **(2.14 only)** AI platform guide: GitOps, GPU runtimes, MaaS, MCP data access, Developer Hub, NVIDIA blueprints |
| — | [release-delta.md](chapters/release-delta.md) | Version-by-version change log: what changed between releases |

---

## Quick Reference

**Registry**: `icr.io/cpopen/isf-operator-catalog:<version>-linux.amd64`
**Namespace**: `ibm-spectrum-scale` (Scale CSI), Fusion operators in `ibm-fusion` or per-operator namespace
**Support**: `ibm.com/support` · Machine models for support cases: 9155-C10, 9155-C14, 9155-C25 *(2.14)*, 9155-G03, 9155-S01, 9155-S02, 9155-R42, 9155-TF5
**Blueprints**: AI Applications, OpenShift Virtualization, Containerized workloads — see IBM Fusion documentation portal
**Support matrix (2.13)**: https://www.ibm.com/support/pages/node/6829067
**Support matrix (2.14)**: https://www.ibm.com/support/pages/node/7081324