from flask import Flask
application = Flask(__name__)

if __name__ =="__main__":
    app.run(debug=True, port=8080)

@app.route('/')
def hello_world():
    return 'Hello, World!'