## import dependencies 

from flask import Flask, render_template, redirect
import pymongo
import scrape_mars

app = Flask(__name__)

conn = 'mongodb://localhost:27017'  
client = pymongo.MongoClient(conn)
mongo = PyMongo(app)

@app.route('/')
def home():

    marsData = 

    return render_template('index.html', marsData)



@app.route('/scrape')
def scraping():
    db = client.mars
    mars = db.mars_data
    marsData = scrape_mars.scrape()
    mars.update({}, marsData, upsert=True)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)