from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    # RULE 1- remember to put HTML file in Templates folder
    # RULE 2 - put static file like Images, CSS and Javascript files in a static folder to use
    return render_template("index-test.html")
# To edit your HTML file directly from website instead of code -
# Got to Inspect -> Console -> and type -> document.body.contentEditable=true (this is Javascript)
# --> and voila edit directly from website , Then Download the HTML file to your computer and replace the HTML file in your templates folder with the new one.

if __name__ == "__main__":
    app.run(debug=True)