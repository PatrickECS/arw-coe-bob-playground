# Services

## Available platforms

- IBM Fusion on-prem — unified on-prem infrastructure platform for containerized workloads

## Container services

- Apache httpd — serves static webpages (example: IBM Bob webpage)
- Container runtime — runs demonstration workloads

## AI services

- IBM Bob — AI-powered software engineering agent running as a containerized workload on IBM Fusion on-prem

## Example service deployment

```bash
docker build -t bob-apache .
docker run --rm -p 8080:80 bob-apache
```

This is a demonstration configuration. Production service deployments follow separate operational procedures.
