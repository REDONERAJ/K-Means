from flask import Flask, render_template, request
import joblib

app = Flask(__name__)
kmeans, scaler, features = joblib.load('synthetic_kmeans_model.pkl')

@app.route("/", methods=["GET", "POST"])
def index():
    cluster = None
    if request.method == "POST":
        try:
            values = [float(request.form[f]) for f in features]
            scaled_values = scaler.transform([values])
            cluster = int(kmeans.predict(scaled_values)[0])
        except:
            cluster = "Invalid input"
    return render_template("index.html", features=features, cluster=cluster)

if __name__ == "__main__":
    app.run(debug=True)
