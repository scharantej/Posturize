
# Import the necessary modules.
from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application.
app = Flask(__name__)

# Define the routes for the application.
@app.route("/")
def index():
    """
    Render the landing page.
    """
    return render_template("index.html")

@app.route("/module1")
def module1():
    """
    Render the first module page.
    """
    return render_template("module1.html")

@app.route("/module2")
def module2():
    """
    Render the second module page.
    """
    return render_template("module2.html")

@app.route("/module3")
def module3():
    """
    Render the third module page.
    """
    return render_template("module3.html")

@app.route("/module4")
def module4():
    """
    Render the fourth module page.
    """
    return render_template("module4.html")

@app.route("/quiz")
def quiz():
    """
    Render the quiz page.
    """
    return render_template("quiz.html")

@app.route("/results", methods=["POST"])
def results():
    """
    Render the results page.
    """
    # Get the user's answers from the request.
    answers = request.form.getlist("answer")

    # Calculate the user's score.
    score = 0
    for answer in answers:
        if answer == "correct":
            score += 1

    # Render the results page.
    return render_template("results.html", score=score)

# Run the application.
if __name__ == "__main__":
    app.run(debug=True)
