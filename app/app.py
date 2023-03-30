from flask import Flask

app = Flask(__name__)



# Point de terminaison de prediction()
@app.route("/predict")
def predict():
    return "Estimation du modèle"



# Point de terminaison de monitoring
@app.route("/health")
def health():
    return "monitoring modèle"

if __name__ == "__main__":
    app.run(debug=True)
