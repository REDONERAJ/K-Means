# 📊 Synthetic K-Means Clustering Web App

This project is a **Flask-powered web application** that uses a **K-Means clustering model** to assign new data points to one of three clusters.  

The dataset is generated **synthetically** using `sklearn.datasets.make_blobs` with 3 features, so it is fully **offline**, stable, and produces clear, well-separated clusters.

---

## 🚀 Features
- **No external dataset dependency** — works completely offline.
- **3 numeric features** with well-separated clusters for meaningful predictions.
- User-friendly Flask web interface with example placeholders for quick testing.
- Predicts and displays the **cluster ID** for any 3-feature numeric input.

---

## 📂 Project Structure
```synthetic-kmeans-clustering/
│
├── model.py # Generates synthetic data, trains model, saves model+scaler+features
├── app.py # Flask web app that loads model and predicts clusters
├── synthetic_kmeans_model.pkl # Saved model, scaler, and features
├── templates/
│ └── index.html # Web form UI with example placeholders
├── requirements.txt # Python dependencies
└── README.md # Project documentation
```
---

## 🔧 Installation
1. **Clone this repository**  
```git clone <your-repo-url>
cd synthetic-kmeans-clustering
```
2. **Install dependencies**  
```pip install -r requirements.txt

```
3. **Train the model**  
```python model.py
```

4. **Run the web app**  
```python app.py
```

5. **Open in Browser**  
Navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🖥 Example Inputs for Testing
Here are sample inputs that should produce different clusters:

| Cluster | Feature 1 | Feature 2 | Feature 3 |
|---------|-----------|-----------|-----------|
| **0**   | `1.5`     | `-2.0`    | `3.2`     |
| **1**   | `5.8`     | `2.1`     | `-1.4`    |
| **2**   | `-3.2`    | `6.0`     | `0.5`     |

---

## ⚙ Requirements
Flask
scikit-learn
pandas
numpy
joblib


---