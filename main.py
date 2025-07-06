from flask import Flask, request, render_template, jsonify
from components.cache import check_cache

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    question = data.get("question")
    threshold = float(data.get("threshold", 0.9))
    answer, is_cached = check_cache(question, threshold)
    return jsonify({"answer": answer, "cached": is_cached})

if __name__ == "__main__":
    app.run(debug=True)
