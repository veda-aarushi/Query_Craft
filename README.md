#  QueryCraft

**QueryCraft** is a dynamic, full-stack SQL learning playground for practicing real-world SQL challenges with live automatic validation.

Built to strengthen SQL query skills with an interactive, self-paced, and fun learning experience.

---

##  Features

🔹 Dynamic SQL challenges (randomized, not hardcoded)
🔹 Real-time validation: compares user queries with expected output
🔹 "Next Question" feature for continuous practice
🔹 Beautiful, responsive UI (React + TailwindCSS)
🔹 Backend API powered by Flask, Flask-CORS, SQLAlchemy
🔹 SQLite database for sample data and problems

---

## 📚 Tech Stack

| Layer            | Technology                          |
|------------------|--------------------------------------|
| Frontend         | React.js, Tailwind CSS, Axios        |
| Backend          | Flask, Flask-CORS, SQLAlchemy        |
| Database         | SQLite (`problems.db`, `sample.db`)  |
| Hosting (planned)| Render (Backend), Vercel (Frontend)  |

---

## 🛠 Setup Instructions

### 🔹 1. Clone the repository

```bash
git clone https://github.com/veda-aarushi/Query_Craft.git
cd Query_Craft
🔹 2. Backend Setup (Flask)
bash
Copy
Edit
cd backend

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Load SQL Problems into the database
python load_problems_from_csv.py

# Start Flask server
python app.py
The backend will run at:
http://localhost:5000

🔹 3. Frontend Setup (React)
bash
Copy
Edit
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
The frontend will run at:
http://localhost:3000

 Screenshots
(Add UI screenshots here to showcase the playground experience.)

Future Enhancements
 Add XP system and leaderboards

 Filter questions by difficulty (Easy / Medium / Hard)

 Add authentication (Login/Signup)

 Admin panel for uploading new SQL problems

 Full deployment to Vercel (frontend) + Render (backend)

📁 Project Structure
pgsql
Copy
Edit
Query_Craft/
├── backend/
│   ├── app.py
│   ├── validate_query.py
│   ├── load_problems_from_csv.py
│   ├── problems.db
│   ├── problems.csv
│   ├── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.js
│   │   ├── SQLPlayground.js
│   │   └── index.css
│   ├── package.json
│
├── README.md
└── .gitignore

Author
Built with passion for learning by
Veda Aarushi
