from flask import *
from werkzeug.exceptions import *
#from werkzeug.utils import *
from bs4 import BeautifulSoup as bs
from requests import get, post
import random
import os, math, json, random, re, html_text, pytesseract, base64, time, smtplib, html5lib

app = Flask(__name__)

@app.errorhandler(RequestURITooLarge)
def TobzZ(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps({
        "code": e.code,
        "name": e.name,
        "description": e.description,
    })
    response.content_type = "application/json"
    return response

def tp(text):
    return text.rstrip('\n').lstrip('\n')

@app.route('/vcard/ririt.html', methods=['GET','POST'])
def api():
        return render_template('ririt.html')

@app.errorhandler(404)
def error(e):
        return render_template('error.html'), 404
if __name__ == '__main__':
        app.run(host='0.0.0.0', port=int(os.environ.get('PORT','5000')),debug=True)
