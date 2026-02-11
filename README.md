
# Microsoft AI-102 Certification Studies
> Repository dedicated to labs and projects developed during the **DIO Bootcamp: Microsoft Azure AI Fundamentals**.

This repository contains implementation examples, API integrations, and hands-on labs focused on the **AI-102: Designing and Implementing a Microsoft Azure AI Solution** exam requirements.

---

## 🚀 Featured Project: Azure Document Translator
A production-ready Python implementation that leverages **Azure Cognitive Services** to translate `.docx` files while maintaining document structure.

### Key Features
* **Batch Processing**: Optimized for performance by batching paragraph requests to the Azure Translator API.
* **Security First**: Environment variable integration to prevent API key exposure.
* **OOA Design**: Built using Object-Oriented principles for better maintainability.
* **Error Handling**: Robust exception management for API connectivity and file I/O.

---

## 🛠️ Technologies & Tools
* **Language:** Python 3.x
* **Cloud:** Microsoft Azure (Cognitive Services / Translator)
* **Libraries:** * `requests`: For REST API communication.
  * `python-docx`: For manipulation of Microsoft Word files.
  * `python-dotenv`: For secure environment variable management.

---

## 📂 Project Structure
```text
├── Lab01-Translator/
│   ├── translator.py       # Main logic (Refactored Version)
│   ├── requirements.txt    # Project dependencies
│   └── .env.example        # Template for API credentials
└── README.md
