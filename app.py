from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'prod'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:a.yuvAc*@localhost/sticky'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rrzgfxwihjdrdp:8bd3d1e3a3f6ddebe2a177a2e75916b0e6d1f2898ee6b25dc986ed542b9757d9@ec2-3-218-149-60.compute-1.amazonaws.com:5432/d2niobfat2fb6a'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class AccountInfo(db.Model):
    __tablename__ = 'accountInfo'
    email = db.Column(db.String(200), primary_key=True)
    password = db.Column(db.String(200))
    username = db.Column(db.String(200), primary_key=True)

    def __init__(self, email, password, username):
        self.email = email
        self.password = password
        self.username = username

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signUp.html')

@app.route('/createaccount', methods=['POST'])
def createaccount():
    email = request.form['email']
    password = request.form['password']
    username = request.form['username']
    if email == '' or password == '' or username == '':
        return render_template('signUp.html', message='Please enter requiered fields')
    # if 
    if db.session.query(AccountInfo).filter(AccountInfo.username == username).count() == 0 and db.session.query(AccountInfo).filter(AccountInfo.email == email).count() == 0:
        data = AccountInfo(email, password, username)
        db.session.add(data)
        db.session.commit()
        return render_template('login.html')
    return render_template('signUp.html', message='Sorry! Your username or email was already taken')


@app.route('/mainpage', methods=['POST'])
def mainpage():
    username = request.form['username']
    password = request.form['password']
    user = AccountInfo.query.filter_by(username=username, password=password).first()
    if user == None:
        return render_template('login.html', message='You have entered the wrong username or password')
    return render_template('index.html')

if __name__ == '__main__':
    app.run()