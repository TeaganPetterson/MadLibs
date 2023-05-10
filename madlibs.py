"""A madlib game that compliments its users."""

from random import choice

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    "awesome",
    "terrific",
    "fantastic",
    "neato",
    "fantabulous",
    "wowza",
    "oh-so-not-meh",
    "brilliant",
    "ducky",
    "coolio",
    "incredible",
    "wonderful",
    "smashing",
    "lovely",
]

FILES = [
    "madlib.html",
    "madlib2.html",
    "madlib3.html"
]

@app.route("/")
def start_here():
    """Display homepage."""

    return "<a href='/hello'>Hi this is the home page</a>"


@app.route("/hello")
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route("/greet")
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")
    compliment = choice(AWESOMENESS)

    return render_template("compliment.html", person=player, compliment=compliment)

@app.route("/game")
def show_madlib_form():
    """play a game if the user so chooses"""

    playAGame = request.args.get("playAGame")

    if playAGame == "No": 
        return render_template("goodbye.html")
    else:
        return render_template("game.html")

@app.route("/madlib")
def show_madlib():
    choiceSite = choice(FILES)
    return render_template(
        choiceSite, 
        one = request.args.get("1"), 
        two = request.args.get("2"), 
        three = request.args.get("3"), 
        four = request.args.get("4"),
        five = request.args.get("5"), 
        six = request.args.get("6"),
        seven = request.args.get("7"),
        eight = request.args.get("8"),
        nine = request.args.get("9"),
        ten = request.args.get("10"),
        eleven = request.args.get("11"),
        twelve = request.args.get("12"),
        thirteen = request.args.get("13"),
        fourteen = request.args.get("14"),
        fifteen = request.args.get("15"),
        sixteen = request.args.get("16"),
        seventeen = request.args.get("17")
        )

if __name__ == "__main__":
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True, host="0.0.0.0", port="3000")
