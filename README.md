# AI Resume Analyzer

An AI-powered web application that analyzes a candidate's resume against a job description using **Large Language Models (LLMs)** and **Prompt Engineering**.

The application extracts text from a PDF resume and sends the resume content along with the job description to an LLM. It then provides matching skills, missing skills, resume improvement suggestions, and interview questions.

---

## 🚀 Features

* 📄 Upload resume in PDF format
* 📝 Enter a job description
* 🤖 Analyze resume using an LLM
* 🎯 Identify matching skills
* 🔍 Identify missing skills
* 📊 Estimate resume-to-job skill match
* 💡 Generate resume improvement suggestions
* ❓ Generate interview questions
* 🔐 Environment variable support for API keys
* 🌐 Simple web interface
* 🐍 Built with Python and FastAPI

---

## 🛠️ Technologies Used

* **Python**
* **FastAPI**
* **OpenAI API**
* **Prompt Engineering**
* **Jinja2**
* **HTML5**
* **CSS3**
* **PyPDF**
* **MySQL**
* **Uvicorn**

---

## 🧠 Prompt Engineering Concepts

This project demonstrates several prompt engineering concepts:

* System prompting
* Role prompting
* Context injection
* Prompt constraints
* Task decomposition
* Temperature control
* Hallucination reduction
* Resume-to-job comparison
* Context-aware prompting

---

## 📁 Project Structure

```text
ai-resume-analyzer/

├── app/
│   ├── main.py
│   ├── prompts.py
│   ├── llm_service.py
│   ├── resume_parser.py
│   └── database.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── .env.example
├── .gitignore
├── README.md
└── requirements.txt
```

---

## ⚙️ How It Works

The application follows this workflow:

```text
User
  ↓
Upload Resume PDF
  ↓
Extract Resume Text
  ↓
Enter Job Description
  ↓
Create Prompt
  ↓
Send Resume + Job Description to LLM
  ↓
LLM Analysis
  ↓
Display Results
```

---

## 📋 Analysis Output

The application provides:

### 1. Match Percentage

An estimated comparison between the candidate's skills and the job requirements.

### 2. Matching Skills

Skills that appear in both the resume and job description.

### 3. Missing Skills

Important skills mentioned in the job description that are not found in the resume.

### 4. Relevant Experience

Experience from the resume that is relevant to the job description.

### 5. Resume Improvement Suggestions

Suggestions for improving the resume based on the provided job description.

### 6. Interview Questions

Five interview questions generated based on the job requirements.

---

## 💻 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-resume-analyzer.git
```

### 2. Open the Project

```bash
cd ai-resume-analyzer
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```text
OPENAI_API_KEY=your_actual_api_key
```

If you are using MySQL:

```text
DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_mysql_password
DB_NAME=resume_analyzer
```

### ⚠️ Security

Never upload your `.env` file to GitHub.

The project includes `.env.example` as a template.

---

## ▶️ Run the Application

Start the FastAPI server:

```bash
uvicorn app.main:app --reload
```

Open your browser:

```text
http://127.0.0.1:8000
```

---

## 🧪 Example Input

### Job Description

```text
We are looking for a Python Developer.

Requirements:

- Python
- FastAPI
- Django
- REST APIs
- MySQL
- Git
- SQL
```

Upload a resume PDF and click:

```text
Analyze Resume
```

The application will analyze the resume against the job description and display the results.

---

## 🔮 Future Improvements

The project can be extended with:

* User authentication
* Resume analysis history
* MySQL database integration
* Resume score dashboard
* Skill-gap visualization
* Multiple LLM providers
* RAG-based job knowledge
* Downloadable PDF analysis report
* Resume keyword optimization
* Job recommendation system
* Streamlit dashboard
* Admin dashboard

---

## 🎯 Learning Objectives

This project was developed to gain practical experience with:

* Python
* REST APIs
* FastAPI
* LLM integration
* Prompt Engineering
* PDF processing
* Environment variables
* MySQL
* Frontend and backend integration
* Git and GitHub

---

## 👨‍💻 Author

**Vamsi**

---

## 📜 License

This project is intended for educational and portfolio purposes.
