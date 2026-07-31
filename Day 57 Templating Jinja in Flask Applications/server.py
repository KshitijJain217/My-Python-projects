from flask import Flask, render_template
import random
import datetime
import requests
app = Flask(__name__)
today = datetime.date.today().year
API_KEY = "from 'https://agify.io/store' and 'https://genderize.io/store'"


@app.route('/')
def home():
    random_number = random.randint(1, 9)
    return render_template('index.html', num=random_number, current_year=today)


@app.route('/guess/<username>')
def guess(username):
    # 1. Make the API requests
    agify_response = requests.get(f"https://api.agify.io?name={username}")
    gender_response = requests.get(f"https://api.genderize.io?name={username}")

    # 2. Extract JSON data safely
    age_data = agify_response.json() if agify_response.status_code == 200 else {}
    gender_data = gender_response.json() if gender_response.status_code == 200 else {}

    # 3. Pull out the specific values
    age = age_data.get("age", "unknown")
    gender = gender_data.get("gender", "unknown")

    # 4. Pass the variables (not response objects) to the template
    return render_template("guess.html", user_name=username, age=age, gender=gender)


@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/a302b1a4fcb3b718c769"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("blog.html", posts=all_posts)


if __name__ == '__main__':
    app.run(debug=True)
