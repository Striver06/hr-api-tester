# HR API Tester 🧪

A pytest-based API testing framework for validating HR Suite backend services.  
Designed to provide **fail-fast validation**, **clear failure classification**, and **dependency-aware testing** without using Postman.

---

## 🚀 Features

- ✅ Pre-flight backend health check (`/api/health`)
- ✅ Token-based authenticated API testing
- ✅ Clear failure classification:
  - **500** → Backend Error
  - **404** → Endpoint Missing
  - **SKIP** → Dependency Down
- ✅ Dependency-aware tests (e.g. RAG service)
- ✅ Clean, CI-ready pytest structure
- ❌ No UI tools (Postman) required

---

## 📂 Project Structure

hr_api_tester/
├── config/            # env & endpoint config
├── core/              # API client, auth, assertions, reporting
├── tests/             # pytest tests + conftest
├── utils/             # payloads, db checks
├── pytest.ini
├── requirements.txt
├── README.md


---

## ⚙️ Prerequisites

- Python **3.10+**
- HR Suite backend running locally or remotely
- Access token for authenticated APIs

---
Avoid manual Postman testing
Catch backend issues early
Provide actionable feedback to backend teams
Enable CI/CD API validation
