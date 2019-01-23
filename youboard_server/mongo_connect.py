from flask import Flask
from flask_pymongo import PyMongo
import channel_scraper
import video_scraper

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
    result = []
    for channel in channel_collection.find():
        result.append(channel)
    return " ".join(str(x) for x in result)

@app.route('/video-scraper')
def scrap_video():
    video_collection = mongo.db.video
    video_collection.remove({ })
    videos = video_scraper.video_scrap()
    for video in videos:
        video_collection.insert(video)
    result = []
    for video in video_collection.find():
        result.append(video)
    return " ".join(str(x) for x in result)

if __name__ == '__main__':
    app.run(debug=True)