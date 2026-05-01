# 🏠 HouseAI – House Construction Cost Predictor

An AI-powered web application that estimates house construction costs in the Philippines using machine learning.

Built with **Next.js, Tailwind CSS, Flask, and scikit-learn**, this project demonstrates full-stack development with real-world ML integration.




## ✨ Features

- 🤖 Machine Learning-based price prediction
- 📊 Real-time cost estimation
- 📈 Interactive charts (Recharts)
- 🧠 AI explanation of predictions
- 🗂 Prediction history (localStorage)
- 🎨 Modern SaaS UI (Tailwind CSS)
- ⚡ Full-stack architecture (Next.js + Flask)

---

## 🧠 How It Works

The model predicts house construction cost based on:

- 📐 Size (sqm)
- 🛏 Bedrooms
- 📍 Location score
- 🏗 Finish level (basic / standard / high-end)
- 💰 Cost per square meter

The ML model learns patterns from synthetic Philippine construction data to estimate realistic price ranges.

---

## 📊 Model Performance

| Metric | Value |
|------|------|
| R² Score | 0.9182 |
| MAE | ₱619,000 |
| Dataset | 500 samples |
| Algorithm | Linear Regression |

---

## 🏗 Tech Stack

### Frontend
- Next.js (App Router)
- Tailwind CSS
- Recharts

### Backend
- Flask
- scikit-learn
- NumPy / Pandas

### Deployment
- Render (Frontend + API)
- GitHub

---

## 📁 Project Structure


house-price-ai/
│
├── app/ # Next.js frontend
│ ├── page.tsx # Dashboard
│ ├── predict/ # Prediction page
│ ├── api/predict/ # API proxy
│
├── ml/ # Python ML backend
│ ├── app.py
│ ├── house_price_model.pkl
│
├── components/ # UI components
│
└── README.md


---

## ⚙️ Installation (Local Setup)

### 1. Clone repo

```bash

cd house-price-ai
2. Run ML Backend (Flask)
cd ml
python -m venv venv
venv\Scripts\activate   # Windows
pip install -r requirements.txt
python app.py

Runs on:

http://127.0.0.1:5000
3. Run Frontend (Next.js)
cd ..
npm install
npm run dev

Runs on:

http://localhost:3000
🔌 API Endpoint
POST /predict
Example Request
{
  "size_sqm": 120,
  "bedrooms": 3,
  "location_score": 7,
  "finish_level": "standard",
  "cost_per_sqm": 30000
}
🚀 Deployment

This project is deployed using Render:

Backend → Flask API
Frontend → Next.js Web Service

Environment variable used:

FLASK_API_URL=https://your-api-url.onrender.com
📌 Future Improvements
📊 Real dataset integration (not synthetic)
🧠 Advanced ML models (XGBoost / Neural Networks)
📱 Mobile-first optimization
🔐 User accounts & saved predictions
📉 Real-time construction cost trends
👨‍💻 Author

EJ (Tech Unlocked)

GitHub:https://github.com/ejluv143
Portfolio: https://ej-portfolio-chi.vercel.app/
