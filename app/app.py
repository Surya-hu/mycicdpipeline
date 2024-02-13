from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Welcome to Devops and CICD Jenkins App created Surya K by Guvi.in IIT Madras ch-09 and new commit pushed'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
