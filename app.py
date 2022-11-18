import json
import requests
from bs4 import BeautifulSoup
from flask import Flask, jsonify, request as req

app = Flask(__name__)
# avoid utf-8 encoding error on response
app.config['JSON_AS_ASCII'] = False

def error_response(status, msg):
    return jsonify(error=msg), status

@app.errorhandler(500)
def resource_not_found(e):
    return error_response(500, str(e))

@app.route('/linkedin')
def get_linkedin_video_url():
    # example = 'https://www.linkedin.com/posts/karina-sivolap-b31490227_javascript-frontend-developer-activity-6998914666747834368-v3SB/'
    args = req.args
    video_url = args.get('video_url')

    if (video_url is None):
        return error_response(400, 'video_url is required')

    page = requests.get(video_url)
    soup = BeautifulSoup(page.content, 'html.parser')

    video_div = soup.find('video')

    if (video_div is None):
        return error_response(400, 'video_url is not a valid LinkedIn video url')

    data_sources = json.loads(video_div['data-sources'])
    
    return jsonify({ 'url': data_sources[0]['src'] })