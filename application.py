from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.get("/")


def home():
    return render_template("base.html")
if __name__ == "__main__":
    app.debug = True
    app.run()
