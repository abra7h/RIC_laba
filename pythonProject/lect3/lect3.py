import json
from flask import Flask, render_template
from database.select import select_list, select_dict
from query.route import blueprint_query


app = Flask(__name__)


# f = open('../data/db_config.json')
# db_config = f.read()
# print(db_config)
# f.close()

# template with
with open('../sem5/external_app/data/db_config.json') as f:
    app.config['db_config'] = json.load(f)

    # db_config = json.load(f)
    # print(db_config)

app.register_blueprint(blueprint_query, url_prefix='/query')


@app.route('/')
def main_menu():
    return render_template('main_menu.html')


@app.route('/')
def product_index():
    prod_category = 1
    _sql = f"""select prod_name, prod_measure, prod_price from product
               where prod_category = {prod_category}"""
    result = select_dict(app.config['db_config'], _sql)
    # result = select_list(db_config, _sql)

    if result:
        prod_title = 'Резульатта из БД'
        return render_template('dynamic.html', prod_title = prod_title, products = result)
    else:
        return 'Результат не получен'


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5001)