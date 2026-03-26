from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run()

# EXERCISE-3
# import time
#
#
# def speed_calc_decorator(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         print(f"{func.__name__} run speed: {end_time - start_time}s")
#         return result
#
#     return wrapper
#
#
# @speed_calc_decorator
# def fast_function():
#     for i in range(1000000):
#         i * i
#
# @speed_calc_decorator
# def slow_function():
#     for i in range(10000000):
#         i * i
#
# fast_function()
# slow_function()

# EXERCISE-1
# def outer_function():
#     print("i am outer")
#
#     def inner_function():
#         print("i am inner")
#
#     return inner_function
#
#
# outer_function()
# outer_function()()

# EXERCISE-2
# import time
#
#
# def delay_decorator(afunction):
#     def wrapper_function():
#         time.sleep(2)
#         afunction()
#     return wrapper_function
#
#
#
# def say_hello():
#     print("Hello")
#
# @delay_decorator
# def say_goodbye():
#     print("Goodbye")
#
# say_hello()
# say_goodbye()