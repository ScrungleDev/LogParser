# LogParser 
**A Modular Log Parsing & Analysis Tool in Python**

LogParser is a production-minded Python tool for parsing, normalizing, and analyzing heterogeneous log files at scale. It is designed to reflect real-world engineering concerns: extensibility, schema consistency, performance, and debuggability.

This project is not a toy script—it models how log ingestion and analysis tools are actually built in support engineering, backend, and SRE-adjacent environments.

---

## Why This Project Exists

Logs are often:
- Large
- Inconsistent
- Partially structured
- Painful to debug manually

Most real systems produce *multiple* log formats at once (JSON, plaintext, web server logs). LogParser demonstrates how to:
- Ingest diverse logs
- Normalize them into a single schema
- Perform meaningful filtering and aggregation
- Surface actionable insights

---

## Key Engineering Concepts Demonstrated

- **Pluggable architecture** (parser interfaces, extensibility)
- **Data normalization & schema design**
- **Streaming & memory-conscious processing**
- **Robust error handling for malformed data**
- **CLI tooling with real UX considerations**
- **Testable, modular Python code**

This mirrors the kind of work done in:
- Support engineering
- Backend debugging
- Incident analysis
- Observability tooling

---

## Features

### Log Ingestion
- Parse individual files or entire directories
- Stream logs line-by-line (no full-file loading)

### Supported Formats
- JSON logs
- Regex-based plaintext logs
- Apache / Nginx-style access logs

### Normalized Log Schema
All logs are converted into a consistent internal structure:

```json
{
  "timestamp": "2026-01-31T14:22:11",
  "level": "ERROR",
  "source": "auth",
  "message": "Failed login for user=admin",
  "metadata": {
    "ip": "10.0.0.5",
    "user": "admin"
  }
}
