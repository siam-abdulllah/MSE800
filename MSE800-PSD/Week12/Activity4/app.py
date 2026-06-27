import os

from flask import Flask, render_template, request, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None

    if request.method == "POST":
        file = request.files["image"]
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))
        image_url = url_for("static", filename=f"uploads/{filename}")

    return render_template("index.html", image_url=image_url)


if __name__ == "__main__":
    app.run(debug=True)
