from flask import Flask
import random
app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Welcome to the Higher Lower Game. Guess a number between 0 and 9.</h1>" \
        "<img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"


the_number = random.randint(0,9)


@app.route("/<int:guess>")
def guess_number(guess):
    if guess > the_number:
        return "<h1> Too High. Try again. </h1>"
    elif guess < the_number:
        return "<h1>Too low. Try Again.</h1>"
    elif guess == the_number:
        return "<h1> Congratulations! You guessed the number correctly. </h1>"
    else:
        return "<h1> Invalid Input. Read insturction carefully. </h1>"


if __name__ == "__main__":
    app.run(debug=True)

