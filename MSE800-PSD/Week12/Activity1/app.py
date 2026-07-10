from flask import Flask

app = Flask(__name__)

TITLE = "Flask Project"


def page(content):
    return f"""<!DOCTYPE html>
<html>
<head><title>{TITLE}</title>
<style>
    body {{
        background-color: grey;
    }}
    h1 {{
        color: white;
    }}
    p {{
        color: red;
    }}
    a {{
        color: pink;
    }}
</style>  
</head>
<body>
<h1>Welcome to my Flask project</h1>
{content}
</body>
</html>
"""


@app.route("/")
def hello_flask():
    return page("<p>Hello, Flask!</p>")


@app.route("/bye")
def bye():
    return page("<p>Bye, Flask!</p>")


@app.route("/greet/<name>")
def greet(name):
    return page(f"<p>This is, {name}!</p>")


@app.route("/multi/<name>/<int:num>")
def multi(name, num):
    return page(
        f"<p>This is, {name}! It starts at {num} a.m. and ends at {num + 2} a.m.</p>"
        f'<a href="https://blackboard.up.education/ultra/courses/_9035_1/cl/outline">Class content link.</a>'
    )


@app.route("/learning/<name>")
def learning(name):
    return page(
        f"<p>I am learning {name}! </p>"
        f'<a href="https://blackboard.up.education/ultra/courses/_9035_1/cl/outline">Flask content link.</a>'
    )


if __name__ == "__main__":
    app.run(debug=True, port=5001)
