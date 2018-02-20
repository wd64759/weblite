"""
    weblite.core
    ~~~~~~~~~~~~

    This module implements the main Weblite portal.

    :copyright: (c) 2018 by Wei
    :license: ISC
"""


from flask import Flask, request, session, g, redirect, url_for, abort, \
    render_template, flash, send_from_directory
import sqlite3

app = Flask(__name__)
# app = Api(app)
app.config.from_object('webliteconfig')
# to load different property files by the given %env% variable in run time
env_loaded = app.config.from_envvar('env', silent=True)
if not env_loaded:
    print('the int configuration is NOT loaded from the $env parameter')


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


def connect_db():
    """ Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE_URI'])
    rv.row_factory = sqlite3.Row
    return rv


def get_db():
    if not hasattr(g, 'mydb'):
        g.mydb = connect_db()
    return g.mydb


@app.teardown_appcontext
def close_db(error):
    """close and release resource when app is down"""
    if hasattr(g, 'mydb'):
        g.mydb.close()


def init_db():
    db = get_db()
    with app.open_resource('db/init.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


@app.cli.command('initdb')
def initdb_cmd():
    """ cli.command() decorator registers a new cmd with flask script and will create an app context """
    init_db()
    print('db init completed')


@app.route('/')
def show_entries():
    db = get_db()
    cur = db.execute('select * from entries order by id desc')
    entries = cur.fetchall()
    return render_template('show_entries.html', entries=entries)


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)

    db = get_db()
    db.execute('insert into entries(title, text) value(?,?)', [request.form['title'], request.form['text']])
    db.commit()
    flash('new entry posted')
    return redirect(url_for('show_entries'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    print('login page request')
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['SECRET_KEY']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['SECRET_CODE']:
            error = 'Invalid password'
        else:
            session['login_id'] = True
            flash('you logged in')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You logged out')
    return redirect(url_for('show_entries'))