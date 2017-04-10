from flask import Flask, render_template

# create instance of flask class
app = Flask(__name__)

# map the URL "/" to python function index
@app.route("/")
def index():
	return render_template("index.html")

@app.route("/about")
def about():
	return render_template("about.html")


if __name__ == "__main__":
	app.run(debug=True)