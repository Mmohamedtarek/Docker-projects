# FastAPI Web App Stack (Production-Ready with Docker Compose)

This project is a **production-ready containerized Python web application** built with **FastAPI**, using a **PostgreSQL** database, **Redis** caching, and **Nginx** as a reverse proxy. It is orchestrated using **Docker Compose** with a multi-stage Dockerfile and Alpine-based images for minimal size and enhanced security.

---

## Stack Overview

- **FastAPI** – High-performance web framework
- **PostgreSQL** – Relational database
- **Redis** – Caching layer
- **Nginx** – Reverse proxy
- **Docker Compose** – Container orchestration
- **Trivy / Docker Scout** – Container security scanning tools
- **Alpine Linux** – Lightweight base images

---

## Architecture

```
+-------------+         +------------------+         +---------------+
|   Client    +-------> |     NGINX        +-------> |  FastAPI App  |
+-------------+         +------------------+         +-------+-------+
                                                       |       |
                                                +------+   +---+------+
                                                | Redis |   | Postgres|
                                                +-------+   +----------+

---

## How to Build & Run

### Build and start the services
```bash
docker compose build
docker compose up


## After startup, the app will be available at:

http://localhost:8080


## Security Scanning

Using Trivy:

$sudo trivy image fastapi-app-app
2025-05-02T19:49:37+03:00	INFO	[vuln] Vulnerability scanning is enabled
2025-05-02T19:49:37+03:00	INFO	[secret] Secret scanning is enabled
2025-05-02T19:49:37+03:00	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-05-02T19:49:37+03:00	INFO	[secret] Please see also https://trivy.dev/v0.62/docs/scanner/secret#recommendation for faster secret detection
2025-05-02T19:49:37+03:00	INFO	Detected OS	family="alpine" version="3.21.3"
2025-05-02T19:49:37+03:00	INFO	[alpine] Detecting vulnerabilities...	os_version="3.21" repository="3.21" pkg_num=37
2025-05-02T19:49:37+03:00	INFO	Number of language-specific files	num=1
2025-05-02T19:49:37+03:00	INFO	[python-pkg] Detecting vulnerabilities...

Report Summary

┌──────────────────────────────────────────────────────────────────────────────────┬────────────┬─────────────────┬─────────┐
│                                      Target                                      │    Type    │ Vulnerabilities │ Secrets │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ fastapi-app-app (alpine 3.21.3)                                                  │   alpine   │        1        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/PyYAML-6.0.2.dist-info/METADATA           │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/annotated_types-0.7.0.dist-info/METADATA  │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/anyio-4.9.0.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/asyncpg-0.30.0.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/click-8.1.8.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/fastapi-0.115.12.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/h11-0.16.0.dist-info/METADATA             │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/httptools-0.6.4.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/idna-3.10.dist-info/METADATA              │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/pip-25.0.1.dist-info/METADATA             │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/pydantic-2.11.4.dist-info/METADATA        │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/pydantic_core-2.33.2.dist-info/METADATA   │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/python_dotenv-1.1.0.dist-info/METADATA    │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/redis-6.0.0.dist-info/METADATA            │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/sniffio-1.3.1.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/starlette-0.46.2.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/typing_extensions-4.13.2.dist-info/METAD- │ python-pkg │        0        │    -    │
│ ATA                                                                              │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/typing_inspection-0.4.0.dist-info/METADA- │ python-pkg │        0        │    -    │
│ TA                                                                               │            │                 │         │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/uvicorn-0.34.2.dist-info/METADATA         │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/uvloop-0.21.0.dist-info/METADATA          │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/watchfiles-1.0.5.dist-info/METADATA       │ python-pkg │        0        │    -    │
├──────────────────────────────────────────────────────────────────────────────────┼────────────┼─────────────────┼─────────┤
│ usr/local/lib/python3.12/site-packages/websockets-15.0.1.dist-info/METADATA      │ python-pkg │        0        │    -    │
└──────────────────────────────────────────────────────────────────────────────────┴────────────┴─────────────────┴─────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)


fastapi-app-app (alpine 3.21.3)

Total: 1 (UNKNOWN: 0, LOW: 0, MEDIUM: 0, HIGH: 1, CRITICAL: 0)

┌─────────────┬────────────────┬──────────┬────────┬───────────────────┬───────────────┬───────────────────────────────────────────────────────┐
│   Library   │ Vulnerability  │ Severity │ Status │ Installed Version │ Fixed Version │                         Title                         │
├─────────────┼────────────────┼──────────┼────────┼───────────────────┼───────────────┼───────────────────────────────────────────────────────┤
│ sqlite-libs │ CVE-2025-29087 │ HIGH     │ fixed  │ 3.48.0-r0         │ 3.48.0-r1     │ sqlite: Integer Overflow in SQLite concat_ws Function │
│             │                │          │        │                   │               │ https://avd.aquasec.com/nvd/cve-2025-29087            │
└─────────────┴────────────────┴──────────┴────────┴───────────────────┴───────────────┴───────────────────────────────────────────────────────┘


$sudo trivy image redis:8.0-rc1-alpine3.21

2025-05-02T19:45:42+03:00	INFO	[vuln] Vulnerability scanning is enabled
2025-05-02T19:45:42+03:00	INFO	[secret] Secret scanning is enabled
2025-05-02T19:45:42+03:00	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-05-02T19:45:42+03:00	INFO	[secret] Please see also https://trivy.dev/v0.62/docs/scanner/secret#recommendation for faster secret detection
2025-05-02T19:45:42+03:00	WARN	No OS package is detected. Make sure you haven't deleted any files that contain information about the installed packages.
2025-05-02T19:45:42+03:00	WARN	e.g. files under "/lib/apk/db/", "/var/lib/dpkg/" and "/var/lib/rpm"
2025-05-02T19:45:42+03:00	INFO	Detected OS	family="alpine" version="3.21.3"
2025-05-02T19:45:42+03:00	INFO	[alpine] Detecting vulnerabilities...	os_version="3.21" repository="3.21" pkg_num=0
2025-05-02T19:45:42+03:00	INFO	Number of language-specific files	num=0

Report Summary

┌──────────────────────────────────────────┬────────┬─────────────────┬─────────┐
│                  Target                  │  Type  │ Vulnerabilities │ Secrets │
├──────────────────────────────────────────┼────────┼─────────────────┼─────────┤
│ redis:8.0-rc1-alpine3.21 (alpine 3.21.3) │ alpine │        0        │    -    │
└──────────────────────────────────────────┴────────┴─────────────────┴─────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected)


$sudo trivy image nginx:stable-alpine-perl

2025-05-02T19:45:09+03:00	INFO	[vuln] Vulnerability scanning is enabled
2025-05-02T19:45:09+03:00	INFO	[secret] Secret scanning is enabled
2025-05-02T19:45:09+03:00	INFO	[secret] If your scanning is slow, please try '--scanners vuln' to disable secret scanning
2025-05-02T19:45:09+03:00	INFO	[secret] Please see also https://trivy.dev/v0.62/docs/scanner/secret#recommendation for faster secret detection
2025-05-02T19:45:10+03:00	INFO	Detected OS	family="alpine" version="3.21.3"
2025-05-02T19:45:10+03:00	INFO	[alpine] Detecting vulnerabilities...	os_version="3.21" repository="3.21" pkg_num=70
2025-05-02T19:45:10+03:00	INFO	Number of language-specific files	num=0

Report Summary

┌──────────────────────────────────────────┬────────┬─────────────────┬─────────┐
│                  Target                  │  Type  │ Vulnerabilities │ Secrets │
├──────────────────────────────────────────┼────────┼─────────────────┼─────────┤
│ nginx:stable-alpine-perl (alpine 3.21.3) │ alpine │        0        │    -    │
└──────────────────────────────────────────┴────────┴─────────────────┴─────────┘
Legend:
- '-': Not scanned
- '0': Clean (no security findings detected) 

## Project Structure

.
├── app/
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── nginx/
│   ├── default.conf
│   └── nginx.conf
├── docker-compose.yml
└── README.md

