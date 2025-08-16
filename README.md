
# Resume Optimizer

A Flask web application that helps users optimize their resumes for job applications by calculating an ATS score and providing suggestions for improvement using the Gemini API.

## Features

- **User Authentication:** Secure user registration and login.
- **Resume Upload:** Upload resumes in PDF or DOCX format.
- **Job Description Input:** Paste job descriptions for analysis.
- **ATS Score Calculation:** Get an ATS score in percentage.
- **Resume Analysis:** Receive a detailed breakdown of your resume's strengths and weaknesses.
- **Suggestions for Improvement:** Get suggestions on how to improve your resume, with highlighted sections.
- **Modern UI:** A clean and modern user interface with light and dark modes.

## Technologies Used

- **Backend:**
    - Flask
    - Flask-SQLAlchemy
    - Flask-Login
- **Database:**
    - SQLite
- **Frontend:**
    - HTML
    - CSS
    - JavaScript
- **API:**
    - Google Gemini API

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd resume-optimizer
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Create a `.env` file:**
    Create a `.env` file in the root of the project and add your Gemini API key:
    ```
    GEMINI_API_KEY=YOUR_API_KEY_HERE
    ```

5.  **Initialize the database:**
    ```bash
    flask --app app.py init-db
    ```

6.  **Run the application:**
    ```bash
    flask --app app.py --debug run
    ```

    The application will be running at `http://127.0.0.1:5000`.
