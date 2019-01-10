from flask import Flask, render_template, send_from_directory
app = Flask(__name__, template_folder="./templates")

@app.route("/")
def home():
    return render_template('index.html')

@app.route('/css/<path:filename>')
def send_css(filename):
    return send_from_directory('./templates/css', filename)

@app.route('/js/<path:filename>')
def send_js(filename):
    return send_from_directory('./templates/js', filename)

@app.route('/img/<path:filename>')
def send_img(filename):
    return send_from_directory('./templates/img', filename)

@app.route('/data/<path:filename>')
def send_data(filename):
    return send_from_directory('./templates/data', filename)