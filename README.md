# Bob — Apache httpd Container on IBM Fusion On-prem

This repository hosts a simple static webpage served by an Apache httpd container, running on IBM Fusion on-prem at the Arrow Experience Center.

## Contents

- `Dockerfile` — Builds an Apache httpd 2.4 (Alpine) container serving `index.html`
- `index.html` — Webpage about Bob running in IBM Fusion on-prem at the Arrow Experience Center
- `README.md` — This file

## Build and Run

Build the image:

```bash
docker build -t bob-apache .
```

Run the container:

```bash
docker run --rm -p 8080:80 bob-apache
```

Open http://localhost:8080 in your browser.

## Deployment on IBM Fusion on-prem

Deploy this container to IBM Fusion on-prem infrastructure at the Arrow Experience Center following your organization's container deployment process.

## About

This page is about Bob, an AI-powered software engineering agent, running as a containerized workload on IBM Fusion on-prem in the Arrow Experience Center.