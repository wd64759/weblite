"""
    weblite.core
    ~~~~~~~~~~~~

    This module implements the main Weblite portal.

    :copyright: (c) 2018 by Wei
    :license: ISC
"""

import logging
import sqlite3

from flask import Flask, g, render_template, send_from_directory
from weblite.lite_service import lite_service

# over all setting for logging and other environment related context
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

app = Flask(__name__)
# app = Api(app)
app.config.from_object('webliteconfig')
# to load different property files by the given %env% variable in run time
env_loaded = app.config.from_envvar('env', silent=True)
if not env_loaded:
    logging.warning('the int configuration is NOT loaded from the $env parameter')


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


@app.route('/pages/<path>')
def send_page(path):
    print('get your request {}'.format(path))
    return send_from_directory('views', path)


@app.route('/js/<path>')
def send_js(path):
    return send_from_directory('js', path)


@app.teardown_appcontext
def close_db(error):
    """close and release resource when app is down"""
    if hasattr(g, 'db_session'):
        g.db_session.close()


def init_db_with_script():
    """ initiate the db with the given SQL file """
    db = sqlite3.connect(app.config['DATABASE_URI'])
    db.row_factory = sqlite3.Row
    with app.open_resource('db/init.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


@app.cli.command('initdb')
def init_db_cmd():
    """ cli.command() decorator registers a new cmd with flask script and will create an app context """
    init_db_with_script()


@app.route('/')
def home():
    return render_template('home.html')


app.register_blueprint(lite_service)
