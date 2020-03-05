from flask import Flask, render_template
application = Flask(__name__)

app = Flask(__name__, static_url_path='/static')
	
@app.route('/')
def index():
	myName = "Jamie"
	return render_template('index.html', name=myName)
	
@app.route('/')
def inspiration():
	myName = "Jamie"
	return render_template('inspiration.html', name=myName)
	
@app.route('/')
def homepage():
	myName = "Jamie"
	return render_template('homepage.html', name=myName)

#-- Bottom -- 
if __name__ =="__main__":
    app.run(debug=True, port=8080)