from mongoengine import *
from flask import Flask, render_template
import os
import csv

connect('mydb')
app = Flask(__name__)
app.config.from_object('config')
#Class to store user data in the database
class User(Document):
	email = StringField()
	first_name = StringField()
	last_name = StringField()
#Class to store country data in the database
class Country(Document):
	name = StringField()
	data = DictField()
	
@app.route('/countries', methods=['GET'])
def getCountries():
	countries = Country.objects
	return countries.to_json(), 200

@app.route('/loadData', methods=['GET']) #utility route that loads data from the .csv files and adds them to the database collection.
def loadData():
	for file in os.listdir(app.config['FILES_FOLDER']):
		filename = os.fsdecode(file)
		path = os.path.join(app.config['FILES_FOLDER'],filename)
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
						# if the country already exists, replace the blank country with the existing country from the db, and replace the blank dict with the current countries
						country = Country.objects.get(name = data[key])
						dict = country['data']                
				else:
					print (key)
					print (data[key])
					f = filename.replace(".csv","") # we want to trim off the ".csv" as we can't save anything with a "." as a mongodb field name
					if f in dict: # check if this filename is already a field in the dict
						dict[f][key] = data[key] # if it is, just add a new subfield which is key : data[key] (value)
					else:
						dict[f] = {key:data[key]} # if it is not, create a new object and assign it to the dict
				country['data'] = dict
			country.save()
	return Country.objects.to_json(), 200

@app.route('/') #All 3 routes redirect to the index page
@app.route('/index')
@app.route('/home')
def index():
	return render_template('index.html'), 200	
	
@app.route('/inspiration')
def inspiration():
	return render_template('inspiration.html'), 200
	
#-- Bottom -- 
if __name__ =="__main__":
    app.run(host='0.0.0.0', port=80)
