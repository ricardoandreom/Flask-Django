from flask import Flask, render_template

app = Flask(__name__)

@app.route("/<name>")
def home(name):
    return render_template("index3.html", content=name, r=2)

if __name__ == "__main__":
    app.run(port=5002)

# run in the browser for example: http://127.0.0.1:5002/Ricardo