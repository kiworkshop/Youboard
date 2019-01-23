from flask import Flask
from flask_pymongo import PyMongo
import channel_scraper

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'youboard'
app.config['MONGO_URI'] = 'mongodb://youboard:youboard2019@ds155614.mlab.com:55614/youboard'

mongo = PyMongo(app)

@app.route('/channel-scraper')
def scrap_channel():
    channel_collection = mongo.db.channel
    channel_collection.remove({ })
    channels = channel_scraper.channel_scrap()
    for channel in channels:
        channel_collection.insert(channel)
    return 'Completed to scrap channels!'

if __name__ == '__main__':
    app.run(debug=True)