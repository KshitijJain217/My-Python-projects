from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


# different routes using the app.route decorator
@app.route("/bye")
def say_bye():
    return "Bye"


# creating variable paths and converting the path to a specified data type
@app.route("/username/<path:name>/<int:number>")
def say_username(name, number):
    return f"hello there {name}, you are {number} years old"


if __name__ == '__main__':
    # run app in debug mode to auto-reload
    app.run(debug=True)
