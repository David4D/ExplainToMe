from flask import jsonify, request
from flask import Blueprint

from . utils import get_summary

api = Blueprint('api', __name__)

@api.route('/summary', methods=['POST'])
def summary():
    posted = request.get_json()
    if posted:
        url = posted.get('url', 'https://www.wsj.com/articles/how-panera-solved-its-mosh-pit-problem-1496395801')
        max_sent = posted.get('max_sent', 10)
    else:
        url = request.values.get('url', 'https://www.wsj.com/articles/how-panera-solved-its-mosh-pit-problem-1496395801')
        max_sent = request.values.get('max_sent', 10)
    language = 'english'
    session_data = get_summary(url, max_sent, language)
    return jsonify(**session_data)
