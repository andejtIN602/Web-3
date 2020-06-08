from mongoengine import *
from flask import Flask, render_template
import os
import csv

connect('mydb')
app = Flask(__name__)
app.config.from_object('config')

class User(Document):
	email = StringField()
	first_name = StringField()
	last_name = StringField()

class Country(Document):
	name = StringField()
	data = DictField()
	
jamie = User(first_name='Jamie', last_name='Anderson')
jamie.save()

newzealand = Country(name='New Zealand')
newzealand.save()
	
for u in User.objects:
	u['first_name'] = 'Changed'
	u.save()

@app.route('/countries', methods=['GET'])
def getCountries():
	countries = Country.Object
	return countries.to_json(), 200
	
@app.route('/')
def index():
	return render_template('index.html'), 200
	
@app.route('/inspiration')
def inspiration():
	return render_template('inspiration.html'), 200
	
#-- Bottom -- 
if __name__ =="__main__":
    app.run(host='0.0.0.0', port=80)
