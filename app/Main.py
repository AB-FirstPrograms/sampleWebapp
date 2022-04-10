from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def head():
    return "<h1 style='color:black'>Hello! Welcome to sample flask code</h1>"


@app.route("/html")
def html():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=5001)