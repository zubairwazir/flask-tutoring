from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    names = ['Khalid', 'Zubair', 'Shah Seb', 'Shehzad']
    return render_template("index.html", names=names)

@app.route("/test")
def test():
    i=10
    return render_template("index.html", i=i)


if __name__ == "__main__":
    app.run(debug=True)
