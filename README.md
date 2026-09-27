# Resume Bullet Point Optimizer 🚀

An AI-powered tool that transforms weak resume bullet points into impactful, quantifiable statements using Google Gemini API.

## Demo

**Before:** `Worked on Python project at CNRS`

**After:** `Engineered robust Python-based data pipelines at CNRS, optimizing research workflows and reducing computational processing time by 35%`

## Features

- ✅ AI-powered optimization using Google Gemini 3.8 Flash
- ✅ Clean web interface built with Streamlit
- ✅ Instant results

## Tech Stack

- Python
- Google Gemini API (gemini-3.8-flash)
- Streamlit
- python-dotenv

## Installation

1. Clone the repository
```bash
git clone https://github.com/mohyieddine-kamal/resume-bullet-optimizer.git
cd resume-bullet-optimizer
```

2. Create a virtual environment
```bash
python -m venv resume
source resume/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create your `.env` file
```bash
cp .env.example .env
```

5. Add your Gemini API key to `.env`
```
GEMINI_API_KEY=your_api_key_here
```

6. Run the app
```bash
streamlit run app.py
```

## Author

Mohyieddine KAMAL — [GitHub](https://github.com/mohyieddine-kamal)
