from flask import Blueprint, redirect, url_for, render_template
from flask.globals import request

from .extensions import db
from .models import URL

short = Blueprint('short', __name__)
counter = 6

@short.route('/', methods=['POST', 'GET'])
def home():
  global counter
  if request.method == 'POST':
    url_received = request.form['nm']
    found_url = URL.query.filter_by(original_url=url_received).first()
    if found_url:
      return redirect(url_for('short.display_short_url', url=found_url.short_url))
    else:
      new_url = URL(url_received, counter)
      counter += 1
      db.session.add(new_url)
      db.session.commit()
      short_url = new_url.short_url
      return redirect(url_for('short.display_short_url', url=short_url)) # TODO - change - this is not working!
  else:
    return render_template('url_page.html')

@short.route('/<short_url>')
def redirect_to_url(short_url):
  original_url = URL.query.filter_by(short_url=short_url).first()
  if original_url:
    redirect(original_url.original)
  else:
    return 'URL does not exist'

@short.route('/display/<url>')
def display_short_url(url):
    return render_template('short_url.html', short_url_display=url)
