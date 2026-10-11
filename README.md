# Puja Sharma — Personal Engineering Portfolio

A modern, production-quality personal portfolio website engineered with **Python Flask**, modern responsive CSS3, and vanilla JavaScript. Visually inspired by high-end design aesthetics (clean whitespace, sharp typography, dark charcoal contrast, subtle micro-animations, and recruiter-focused storytelling).

---

## 🧭 Live Demo & Local Host

When running locally, access the portfolio at:
👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📁 Project Structure

```text
portfolio/
│
├── app.py                      # Flask backend application & data dictionary
├── requirements.txt            # Python dependencies (Flask, etc.)
├── generate_assets.py          # Helper script to create asset placeholders
├── README.md                   # Setup guide and instructions
├── .gitignore                  # Git exclusions for venv and caches
├── venv/                       # Python virtual environment (ignored in git)
│
├── templates/
│   ├── base.html               # Base layout, header, footer, SEO & modal
│   └── index.html              # Main single-page portfolio sections
│
├── static/
│   ├── css/
│   │   └── style.css           # Custom modern responsive stylesheet
│   ├── js/
│   │   └── script.js           # Scroll spy, case study modals, contact handler
│   ├── images/
│   │   ├── profile.jpg         # Profile photograph (replace with your photo)
│   │   ├── project-rag.jpg     # RAG project card graphic
│   │   ├── project-ocr.jpg     # OCR pipeline card graphic
│   │   ├── project-automation.jpg # QA Automation card graphic
│   │   └── project-qualcomm.jpg   # Qualcomm SDK card graphic
│   └── documents/
│       └── resume.pdf          # Downloadable resume PDF
│
└── screenshots/                # Optional screenshots for GitHub preview
```

---

## 🚀 Quickstart Guide

### 1. Prerequisites
Ensure **Python 3.9+** is installed on your computer:
```bash
python --version
```

### 2. Create the Virtual Environment
Navigate to the portfolio directory and create a virtual environment:
```bash
# On Windows:
python -m venv venv
```

### 3. Activate the Virtual Environment
```bash
# On Windows (PowerShell):
.\venv\Scripts\Activate.ps1

# On Windows (Command Prompt):
.\venv\Scripts\activate.bat

# On macOS / Linux:
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
```

### 5. Run the Website
```bash
python app.py
```
Open your browser and navigate to:
```text
http://127.0.0.1:5000
```

---

## 🖼️ Where to Place Your Images & Files

All media assets are stored inside the `static/` directory:

| Asset | File Location | Purpose & Guidance |
|---|---|---|
| **Your Profile Photo** | `static/images/profile.jpg` | Replace with a high-resolution, professional portrait photograph (square or 4:5 aspect ratio recommended). |
| **Industrial RAG Project** | `static/images/project-rag.jpg` | Replace with a screenshot or architecture diagram of the RAG system. |
| **PDF OCR Pipeline** | `static/images/project-ocr.jpg` | Replace with a screenshot or visual of document processing. |
| **Mobile QA Automation** | `static/images/project-automation.jpg` | Replace with a test report or Appium test execution visual. |
| **Qualcomm SDK Exploration** | `static/images/project-qualcomm.jpg` | Replace with an edge AI or Qualcomm SDK architecture diagram. |
| **Resume PDF** | `static/documents/resume.pdf` | Replace with your finalized single-page or two-page resume in PDF format. |

> **Graceful Image Fallback:** If an image is missing or cannot be loaded, the website automatically falls back to an elegant monogram or styled icon badge without broken icons.

---

## ✏️ How to Update Your Personal Information

All portfolio text, experiences, projects, case studies, and contact details are organized cleanly in **two places**:

1. **Backend Python Data Dictionary (`app.py`)**:
   Open `app.py` in your favorite editor. The `PORTFOLIO_DATA` dictionary contains:
   - Personal information (Name, Title, Location, Email, LinkedIn, GitHub)
   - Statistics (CGPA, Experience, Roles, Honors)
   - Work Process steps
   - Experience timeline and responsibilities
   - Detailed project case studies (Problem, Approach, Technologies, Contribution, Outcome)
   - Categorized skills
   - Education and Certifications

2. **Template Customization (`templates/index.html` & `templates/base.html`)**:
   You can easily modify template markup, section orders, or add additional links.

### How to Add Your GitHub URL
In `app.py`, find the `personal` section and replace `"[ADD GITHUB URL]"` with your actual link:
```python
"github": "https://github.com/your-username",
```
Then in `templates/base.html` and `templates/index.html`, replace `href="#"` with `href="{{ data.personal.github }}"`.

---

## 🚢 How to Deploy

### Option A: Render (Free & Fast)
1. Push your repository to GitHub.
2. Sign in to [Render.com](https://render.com/).
3. Click **New +** -> **Web Service**.
4. Connect your GitHub repository.
5. Set the settings:
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app` (add `gunicorn` to `requirements.txt`)
6. Click **Deploy**.

### Option B: PythonAnywhere (Beginner Friendly)
1. Create a free account at [PythonAnywhere.com](https://www.pythonanywhere.com/).
2. Open a Bash console and git clone your repository.
3. Create a virtualenv with `mkvirtualenv --python=/usr/bin/python3.10 portfolio-env`.
4. Run `pip install -r requirements.txt`.
5. Go to the **Web** tab, configure the WSGI configuration file pointing to `app.py`, and reload the app.

### Option C: Railway
1. Push your repository to GitHub.
2. Create a new project on [Railway.app](https://railway.app/).
3. Connect your repository. Railway automatically detects `requirements.txt` and `app.py` and deploys it with zero configuration.

---

## 📄 License & Attribution
Designed & Engineered for **Puja Sharma**.  
© 2026 Puja Sharma. All rights reserved.
