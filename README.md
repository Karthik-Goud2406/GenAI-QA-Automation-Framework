# GenAI QA Automation Framework 🚀

A robust QA automation framework using **Pytest**, **Allure**, and **GitHub Actions**.  
Designed to showcase GenAI-driven testing workflows for portfolio and professional applications.

---

## 🔧 Features

- ✅ Pytest test suite with modular structure  
- 📊 Allure report generation and CI artifact upload  
- ⚙️ GitHub Actions workflow for automated testing  
- 🧠 GenAI integration-ready (LangChain, SkyReels-V2, etc.)

---


## ⚙️ Setup Instructions

```bash
git clone https://github.com/Karthik-Goud2406/GenAI-QA-Automation-Framework.git
cd GenAI-QA-Automation-Framework
pip install -r requirements.txt
pytest --alluredir=reports/
allure generate reports/ -o reports_html --clean

```

Karthik Goud Aspiring GenAI QA Analyst
LinkedIn: https://www.linkedin.com/in/karthik-goud-2812882a7

CI/CD Workflow

Triggered on push to main
Runs Pytest test suite
Generates Allure report
Uploads report as artifact in GitHub Actions

<img width="1365" height="657" alt="image" src="https://github.com/user-attachments/assets/0874d3ee-dd45-4c24-b85a-a817197c981b" />


Technologies Used

Python 3.13
Pytest
Allure CLI
GitHub Actions
LangChain (optional integration)
SkyReels-V2 (optional GenAI module)


GenAI-QA-Automation-Framework/
├── tests/
│   └── test_login.py
├── reports/
├── reports_html/
├── .github/
│   └── workflows/
│       └── tests.yml
├── requirements.txt
└── README.md





