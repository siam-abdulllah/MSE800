from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/bmi/<username>", methods=["GET", "POST"])
def bmi_calculator(username):
    if request.method == "POST":
        weight_raw = request.form.get("weight", "").strip()
        height_raw = request.form.get("height", "").strip()

        try:
            weight = float(weight_raw)
            height = float(height_raw)
        except ValueError:
            return render_template(
                "index.html",
                username=username,
                error="Weight and height must be valid numbers.",
            )

        if weight <= 0 or height <= 0:
            return render_template(
                "index.html",
                username=username,
                error="Weight and height must be greater than zero.",
            )

        bmi = weight / (height ** 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi <= 24.9:
            category = "Normal weight"
        elif bmi <= 29.9:
            category = "Overweight"
        else:
            category = "Obese"

        print(f"Your BMI is: {round(bmi, 2)}")
        print(f"You are classified as: {category}")

        return render_template("result.html", username=username, bmi=round(bmi, 2), category=category)

    return render_template("index.html", username=username)


if __name__ == "__main__":
    app.run(debug=True)
