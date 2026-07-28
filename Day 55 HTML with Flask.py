from flask import Flask

app = Flask(__name__)

#Decorators to add a tag around text on web page.
def make_bold(func):
    def wrapper(*args, **kwargs):
        # Copilot method
        my_text = func(*args, **kwargs)
        return f"<b>{my_text}</b>"
    return wrapper


def make_italic(func):
    def wrapper():
        # Angela yu method
        return "<em>" + func() + "</em>"
    return wrapper


def make_underline(func):
    def wrapper(*args, **kwargs):
        my_text = func(*args, **kwargs)
        return f"<u>{my_text}</u>"
    return wrapper


@app.route('/')
def hello_world():
    # Rendering HTML Elements
    return ('<h1 style="text-align: center">Hello, World!</h1>'
            '<p style="text-align: center"> <b>This is a Productive Cat</b> </p>'
            '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExeDVsaHo4ZzNnY3c2bWFrdmNiZG11d3p2cnRqaDFqMGw5d2V1aWVicSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/JIX9t2j0ZTN9S/giphy.gif" '
            'width=500 style="display: block; margin: 0 auto;">')


# different routes using the app.route decorator
@app.route("/bye")
@make_underline
@make_italic
@make_bold
def say_bye():
    return "Bye"


# creating variable paths and converting the path to a specified data type
@app.route("/username/<path:name>/<int:number>")
def say_username(name, number):
    return f"hello there {name}, you are {number} years old"


if __name__ == '__main__':
    # run app in debug mode to auto-reload
    app.run(debug=True)
