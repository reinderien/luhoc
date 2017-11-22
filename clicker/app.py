from flask import Flask, request, render_template

# Flask app.
app = Flask(__name__)

# Counter
count = 0

# Home page.
@app.route("/", methods=["GET", "POST"])
def index():
    global count

    if request.method == "POST":
        count += 1

    return render_template("index.html", count=count)
