from mongoengine import *
from flask import Flask, render_template

connect('mydb')
app = Flask(__name__, static_url_path='/static', template_folder='/templates')

class User(Document):
	email = StringField()
	first_name = StringField()
	last_name = StringField()

class Country(Document):
	name = StringField()
	
	
jamie = User(first_name='Jamie', last_name='Anderson')
jamie.save()

newzealand = Country(name='New Zealand')
newzealand.save()
	
for u in User.objects:
	u['first_name'] = 'Changed'
	u.save()
	
@app.route('/users', methods=['GET'])
def index():
	users = User.objects
	return users.to_json()
	return render_template('index.html', name=myName)
	
@app.route('/inspiration')
def inspiration():
	myName = "Jamie"
	return render_template('about.html', name=myName)
	
@app.route('/')
def homepage():
	myName = "Jamie"
	return render_template('homepage.html', name=myName)

#-- Bottom -- 
if __name__ =="__main__":
    app.run(debug=True, port=8080)