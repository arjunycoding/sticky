from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signUp.html')

@app.route('/createaccount', methods=['POST'])
def createaccount():
    return render_template('login.html')

@app.route('/mainpage', methods=['POST'])
def mainpage():
    return render_template('index.html')
if __name__ == '__main__':
    app.run()