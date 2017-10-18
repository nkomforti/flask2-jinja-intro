"""A madlib game that compliments its users."""

from random import choice, sample

from flask import Flask, render_template, request

# "__name__" is a special Python variable for the name of the current module.
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza',
    'oh-so-not-meh', 'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful',
    'smashing', 'lovely',
]


@app.route('/')
def start_here():
    """Display homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Say hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user with compliment."""

    player = request.args.get("person")

    compliments = sample(AWESOMENESS, 3)

    return render_template("compliment.html",
                           person=player,
                           compliments=compliments)


@app.route('/game')
def show_madlib_form():
    """"""

    game_choice = request.args.get("game_choice")
    player = request.args.get("person")

    if game_choice == 'no':
        return render_template("goodbye.html", player=player)

    else:
        return render_template("game.html", AWESOMENESS=AWESOMENESS)


@app.route('/madlib', methods=["POST"])
def show_madlib():
    """ """

    person = request.form.get("person")
    noun = request.form.get("noun")
    color = request.form.get("color")
    adjective = request.form.get("adjective")

    # import pdb; pdb.set_trace()
    compliments = request.form.getlist("compliment")

    madlib_template = choice(["madlib.html", "madlib2.html", "madlib3.html"])


    html = render_template(madlib_template, person=person, noun=noun,
                           color=color, adjective=adjective, compliments=compliments)
    return html


if __name__ == '__main__':
    # Setting debug=True gives us error messages in the browser and also
    # "reloads" our web app if we change the code.

    app.run(debug=True)
