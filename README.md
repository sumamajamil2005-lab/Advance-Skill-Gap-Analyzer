# AI-Powered Skill Gap Analyzer 🚀
## 📝 Project Overview:

Skill Gap Analyzer is a high-performance Python tool designed to bridge the gap between Resumes and Job Descriptions (JD). Unlike traditional keyword-matching systems, this tool leverages AI (Sentence Transformers) and Advanced Regex to understand the semantic context of professional skills.

It uses a Modular Architecture, replicating the core logic of modern Applicant Tracking Systems (ATS) used by Fortune 500 companies.

## ✨ Key Features:

    AI Semantic Matching: Uses the all-MiniLM-L6-v2 BERT model to recognize that "ML" is "Machine Learning" or "Postgres" relates to "SQL".

    Weighted Scoring Engine: Automatically prioritizes the Top 3 JD Skills as "Primary Requirements," giving them double weightage in the final score.

    Intelligent Normalization: A built-in dictionary handles industry abbreviations (AWS, K8s, JS) to ensure 100% matching accuracy.

    Robust Regex Extraction: Uses word boundaries (\b) to eliminate false positives (e.g., won't match "R" inside "React").

    Automated Reporting: Generates a professional summary in the console and a detailed text report in the output/ folder.

### 📂 Project Structure

```text
skill_gap_analyzer/
├── data/       # Inputs (Resume & JD)
├── matcher/    # AI Engine & Skill Logic
├── output/     # Analysis Reports
├── parsers/    # Extraction Modules
├── skills/     # Master Skill List
├── writer/     # Report Generation
└── main.py     # Application Entry Point
``` 


## 🚀 How to Use

Install Dependencies:
```
pip install sentence-transformers
```
Prepare Data:

    Paste your resume in data/resume.txt.

    Paste the job description in data/job_description.txt.

    Add relevant keywords to skills/skills_list.txt.

Run the Analyzer:

    python main.py

    Review Results:

        Check the terminal for an instant 0-100% score.

        Open output/report.txt for a deep-dive analysis.

## 🛠️ Customization

    Sensitivity: Adjust the similarity threshold (default 0.5) in matcher/ai_matcher.py.

    Normalization: Add custom tech aliases in the _SKILL_NORMALIZATION dictionary within matcher/skill_matcher.py.

## 💻 Tech Stack

    Language: Python 3.x

    AI Model: Sentence-Transformers (BERT-based)

    Pattern Matching: Advanced Regex (re)

    Architecture: Modular / Package-based