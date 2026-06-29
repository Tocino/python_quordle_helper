from flask import Flask, render_template, request
from logic import process_text

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = None

    if request.method == "POST":
        user_text = request.form.get("user_text")
        result = process_text(user_text)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)