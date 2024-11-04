import hashlib
from base64 import b64decode
from hashlib import md5

from flask import Blueprint, session, redirect, url_for, current_app, request, render_template

from database.select import select_dict
from sem4.app4 import provider
from sem5.external_app.database.sql_provider import SQLProvider

blueprint_auth = Blueprint('auth_bp', __name__, template_folder='templates')
provider = SQLProvider()


def create_basic_auth_token(login, password):
    credentials_b64 = b64decode(f'{login}:{password}'.encode('ascii')).decode('ascii')
    print('creditional=', credentials_b64)
    token = f'Basic {credentials_b64}'







@blueprint_auth.route('/login', methods=['GET', 'POST'])
def auth_index():
    if request.method == 'POST':
        print(request.form)

        username = request.form['username']
        password = request.form['password']
        print(hashlib.md5(password.encode()).hexdigest())
        print(username, password)
        _sql = f"""select id, user_group, user_name, pass from users
                       where user_name = '{username}'"""
        try:
            result = select_dict(current_app.config['db_config'], _sql)[0]
        except:
            return render_template('login.html', error="Неверный логин")
        print(result)
        if result[3] == hashlib.md5(password.encode()).hexdigest():
            user_group = result[1]
            user_id = int(result[0])
            session['user_group'] = user_group
            session['user_id'] = user_id

            print('Выполнена аутентификация')

            return redirect(url_for('main_session'))
        else:
            return render_template('login.html', error="Неверный пароль")
            print("Неверный пароль")

    return render_template('login.html')
