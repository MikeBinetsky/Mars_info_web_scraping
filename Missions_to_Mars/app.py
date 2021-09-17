## import dependencies 

from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

app = Flask(__name__)

## Create pymongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017"
mongo = pymongo(app)

@app.route('/')
def home():

    marsData = mongo.db.mars.find_one()

    return render_template('index.html', marsData)



@app.route('/scrape')
def scraping():
    
    mars = mongo.db.mars

    marsData = scrape_mars.scrape()

    mars.update({}, marsData, upsert=True)

    return redirect('/')

if __name__ == "__main__":
    app.run()