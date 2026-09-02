# Natural Language SQL Data Agent (SQLite Mode)

This project implements a Natural Language SQL Data Analyst Agent using LangGraph, Python, and SQLite.

## Project Structure
```
├── data/                  # CSV datasets
├── database/              # SQLite schema, data loading script, and reference
├── src/                   # Source code (agent logic, SQL tools, safety, memory)
├── tests/                 # Automated pytest unit tests
├── outputs/               # Saved test case outputs and execution logs
├── evidence/              # Usage logs and architecture documentation
├── .env.example           # Environment template
├── requirements.txt       # Dependencies
└── README.md              # Project guide
```

## Quick Start Setup

1. **Setup Virtual Environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

2. **Install Dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Configure Environment:**
   Set these user environment variables with your Tiger AI Gateway / LLM API parameters.
   Do not commit credentials to the repository. `TIGER_AI_GATEWAY_MODEL` is optional:
   ```powershell
   [Environment]::SetEnvironmentVariable("TIGER_AI_GATEWAY_URL", "<gateway-url>", "User")
   [Environment]::SetEnvironmentVariable("TIGER_AI_GATEWAY_API_KEY", "<api-key>", "User")
   [Environment]::SetEnvironmentVariable("TIGER_AI_GATEWAY_MODEL", "gpt-4o-mini", "User")
   ```
   Restart the terminal after setting persistent user variables.

4. **Initialize Database & Load Data:**
   ```powershell
   python database/load_data.py
   ```

5. **Run Tests:**
   ```powershell
   pytest
   ```

6. **Start Interactive CLI Agent:**
   ```powershell
   python src/app.py
   ```
