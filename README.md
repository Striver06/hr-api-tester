# HR API Tester 

A pytest-based API testing framework for validating HR Suite backend services.  
Designed to provide **fail-fast validation**, **clear failure classification**, and **dependency-aware testing** without using Postman.

---

## Features

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
│
├── config/
│ └── env.yaml # Environment configuration (URLs, tokens)
│
├── core/
│ ├── client.py # Reusable API client
│ └── auth.py # Authentication helpers
│
├── utils/
│ └── data_factory.py # Test payload generators
│
├── tests/
│ ├── test_auth.py # Auth API tests
│ ├── test_attendance.py # Attendance API tests
│ ├── test_employees.py # Employee creation tests
│ ├── test_payroll.py # Payroll tests
│ └── test_rag.py # RAG dependency tests
│
├── pytest.ini
├── requirements.txt
└── README.md
