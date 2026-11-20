# Infrastructure

## Compute

- Platform: IBM Fusion on-prem
- Workload model: Containerized (container runtimes managed by the platform)
- Example: Apache httpd container running the IBM Bob webpage

## Platform

- IBM Fusion on-prem provides the unified infrastructure layer for deploying and managing containerized workloads.

## Storage

- Ephemeral container storage for demonstration workloads
- No persistent customer data is stored in this environment

## Networking

- Internal network for container-to-container communication
- External access via published container ports (e.g., port 80 for HTTP)
- Example: `docker run --rm -p 8080:80 bob-apache`

## Configuration note

The examples above are for demonstration purposes. Production configurations differ and must be documented separately.
