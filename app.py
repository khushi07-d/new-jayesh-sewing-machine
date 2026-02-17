from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# This is for Google verification file
@app.route("/google30f660431520df61.html")
def google_verification():
    return send_from_directory(".", "google30f660431520df61.html")

if __name__ == "__main__":
    app.run()
