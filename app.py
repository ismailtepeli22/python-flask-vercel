from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<p>Hello, vercel World!</p>"

@app.route("/about")
def about():
    return "<p>Hello, about!</p>"

if __name__=="__main__":
    app.run(debug=True)