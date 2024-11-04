import json
from flask import Flask, render_template, Blueprint, current_app
from database.select import select_list, select_dict


blueprint_query = Blueprint('query_bp', __name__, template_folder='templates')

# app = Flask(__name__)
#
#
# # f = open('../data/db_config.json')
# # db_config = f.read()
# # print(db_config)
# # f.close()
#
# # template with
# with open('../data/db_config.json') as f:
#     app.config['db_config'] = json.load(f)
#
#     # db_config = json.load(f)
#     # print(db_config)


@blueprint_query.route('/')
def query_index():
    prod_category = 1
    _sql = f"""select prod_name, prod_measure, prod_price from product
               where prod_category = {prod_category}"""
    products = select_dict(current_app.config['db_config'], _sql)
    # result = select_list(db_config, _sql)

    if products:
        prod_title = 'Резульатта из БД'
        return render_template('dynamic.html', prod_title = prod_title, products = products)
    else:
        return 'Результат не получен'
