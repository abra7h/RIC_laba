import json
import os

from werkzeug.utils import redirect

from database.sql_provider import SQLProvider
from query.route import blueprint_query
from auth.route import blueprint_auth
from flask import Flask, render_template, session, url_for

from sem4.access import group_required

app = Flask(__name__)

with open('external_app/data/db_config.json') as f:
    app.config['db_config'] = json.load(f)

provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))
print(provider)




with open('../data/db_access.json') as f:
    app.config['db_access'] = json.load(f)

app.secret_key = 'You will never guess'

app.register_blueprint(blueprint_query, url_prefix='/query')
app.register_blueprint(blueprint_auth, url_prefix='/auth')


@app.route('/')
def main_session():
    if 'user_group' in session:
        user_role = session.get('user_group')
        message = f'Вы авторизованы как {user_role}'
    else:
        message = f'Вам необходимо авторизоваться'
    return render_template('main_menu.html', message=message)


@app.route('/exit')
def exit_func():
    session.clear()
    return 'До свидания, заходите к нам ещё!'

@app.route('/logout')
def logout_func():
    session.clear()
    return redirect(url_for('main_session'))

@app.route('/requests', methods=['POST', 'GET'])
@group_required
def requests_func():
    return render_template('requests.html')


@app.route('/back_to_main', methods=['POST'])
def back_func():
    return redirect(url_for('main_session'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001)
