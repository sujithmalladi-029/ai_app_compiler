# AI App Compiler & Validation Engine

## Overview

AI App Compiler is a compiler-inspired system that converts natural language application requirements into structured, validated, and executable application configurations.

The system follows a multi-stage generation pipeline:

```text
User Prompt
     │
     ▼
Intent Extractor
     │
     ▼
System Designer
     │
     ▼
Schema Generator
     │
     ▼
Validation Engine
     │
     ▼
Repair Engine
     │
     ▼
Runtime Simulator
     │
     ▼
Executable App Configuration
```

Unlike simple prompt-based generation, this project introduces validation, repair, and execution-awareness to ensure reliability and consistency.

---

## Features

### Intent Extraction

Converts natural language requirements into structured application intent.

Example:

Input:

```text
Build a CRM with login, contacts, dashboard and payments.
Admins can see analytics.
```

Output:

```json
{
  "app_type": "CRM",
  "features": [
    "login",
    "contacts",
    "dashboard",
    "payments"
  ],
  "roles": [
    "admin",
    "user"
  ]
}
```

---

### System Design Layer

Transforms extracted intent into application architecture.

Generated artifacts include:

* Entities
* Pages
* User Roles
* Permissions

Example:

```json
{
  "entities": ["User", "Contact"],
  "pages": ["Dashboard", "Login", "Contacts"],
  "role_permissions": {
    "admin": ["manage_users", "view_analytics"],
    "user": ["view_contacts"]
  }
}
```

---

### Schema Generation

Generates:

#### UI Schema

```json
{
  "pages": [
    {
      "name": "Dashboard",
      "components": []
    }
  ]
}
```

#### API Schema

```json
{
  "endpoints": [
    {
      "path": "/contacts",
      "method": "GET",
      "table": "contact"
    }
  ]
}
```

#### Database Schema

```json
{
  "tables": [
    {
      "name": "contact",
      "columns": [
        {
          "name": "id",
          "type": "integer"
        }
      ]
    }
  ]
}
```

#### Authentication Schema

```json
{
  "roles": {
    "admin": ["manage_users"],
    "user": ["view_contacts"]
  }
}
```

---

## Validation Engine

The Validation Engine ensures:

* Required sections exist
* Database tables are present
* Authentication roles are valid
* API-to-Database consistency
* Cross-layer correctness

Validation checks include:

* Missing UI pages
* Missing API endpoints
* Missing DB tables
* Missing roles
* API references to non-existent tables

---

## Repair Engine

Instead of regenerating the entire output, the system performs targeted repairs.

Example:

```text
Validation Error
        │
        ▼
Error Classification
        │
        ▼
Targeted Repair
        │
        ▼
Revalidation
```

This improves reliability and minimizes unnecessary regeneration.

---

## Runtime Simulator

The Runtime Simulator verifies whether the generated configuration can be executed.

Checks include:

* Pages exist
* APIs exist
* Database tables exist
* Authentication rules exist

Example Output:

```json
{
  "status": "PASS",
  "errors": []
}
```

---

## Evaluation Framework

Benchmarking is performed using multiple application prompts.

Metrics tracked:

* Success Rate
* Runtime Pass Rate
* Validation Results
* Repair Operations
* Latency

Example:

```text
Success Rate: 5/5
Average Latency: 0.0 seconds
```

---

## Project Structure

```text
ai_app_compiler/
│
├── frontend/
├── pipeline/
├── schemas/
├── validators/
├── repair/
├── runtime/
├── evaluation/
├── docs/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Streamlit Interface

The project provides a Streamlit-based interface where users can:

1. Enter application requirements
2. Generate application configuration
3. View:

   * Intent
   * Architecture
   * UI Schema
   * API Schema
   * DB Schema
   * Auth Schema
4. Run validation and runtime simulation

---

## Installation

Clone the repository:

```bash
git clone https://github.com/sujithmalladi-029/ai_app_compiler.git
```

Navigate to the project:

```bash
cd ai_app_compiler
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run Streamlit Application

```bash
python -m streamlit run frontend/streamlit_app.py
```

---

## Run Benchmark

```bash
python evaluation/benchmark.py
```

---

## Future Improvements

* LLM-based Intent Extraction
* Advanced Schema Generation
* Dynamic API Generation
* Real Runtime Deployment
* Database Migration Generation
* Multi-Agent Validation
* Production Deployment

---

## Author

Malladi Sujith Babu

GitHub: https://github.com/sujithmalladi-029
