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
	
jamie = User(email='andejt1@student.op.ac.nz', first_name='Jamie', last_name='Anderson')
jamie.save()

newzealand = Country(name='New Zealand')
newzealand.save()
	
for u in User.objects:
	u['first_name'] = 'Changed'
	u.save()

@app.route('/countries', methods=['GET'])
def getCountries():
	countries = Country.objects
	return countries.to_json(), 200

@app.route('/loadData', methods=['GET'])
def loadData():
	for file in os.listdir(app.config['FILES_FOLDER']):
		filename = os.fsdecode(file)
		path = os.path.join(app.config['FILES_FOLDER'],data1.csv)
		f = open(path)
		r = csv.DictReader(f) 
		d = list(r)
		for data in d:
			country = Country() # a blank placeholder country
			dict = {} # a blank placeholder data dict
			for key in data: # iterate through the header keys
				if key == "country":
					if Country.objects(name = data[key]).count() == 0: 
						country['name'] = data[key]
					else:
						# if the country already exists, replace the blank country with the existing country from the db, and replace the blank dict with the current country's
						country = Country.objects.get(name = data[key])
						dict = country['data']                
				else:
					f = filename.replace(".csv","") # we want to trim off the ".csv" as we can't save anything with a "." as a mongodb field name
					if f in dict: # check if this filename is already a field in the dict
						dict[f][key] = data[key] # if it is, just add a new subfield which is key : data[key] (value)
					else:
						dict[f] = {key:data[key]} # if it is not, create a new object and assign it to the dict
					country['data'] = dir
				country.save()
	return Country.objects.to_json(), 200

@app.route('/')
def index():
	return render_template('index.html'), 200
	
@app.route('/inspiration')
def inspiration():
	return render_template('inspiration.html'), 200
	
#-- Bottom -- 
if __name__ =="__main__":
    app.run(host='0.0.0.0', port=80)
