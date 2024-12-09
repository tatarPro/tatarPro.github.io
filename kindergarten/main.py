from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def index():
    user = "очередняра"
    return render_template('index.html', title='Домашняя страница', username=user)

@app.route("/gartens")
def gartens():
    user = "очередняра"
    return render_template('gartens.html', title='Сады', username=user)

@app.route("/credits")
def credits():
    user = "очередняра"
    return render_template('credits.html', title='Аккредитация', username=user)

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')