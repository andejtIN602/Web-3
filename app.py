from mongoengine import *
from flask import Flask, render_template

connect('mydb')
app = Flask(__name__)
app.config.from_object('config')

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
	
@app.route('/')
def index():
	path = os.path.join(app.config['FILES_FOLDER'],"data1.csv")
	f = open(path)
	r = csv.reader(f)
	d = list(r)
	for data in d:
		print(data)
	return render_template('index.html')
	
@app.route('/inspiration')
def inspiration():
	return render_template('inspiration.html')
	
#-- Bottom -- 
if __name__ =="__main__":
    app.run(host='0.0.0.0', port=80)
