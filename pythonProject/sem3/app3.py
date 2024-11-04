import json,os
from flask import Flask, render_template, request

from database.select import select_list, select_dict
from database.sql_provider import SQLProvider
from sem3.model_route import model_route

app = Flask(__name__)


# f = open('../data/db_config.json')
# db_config = f.read()
# print(db_config)
# f.close()

# template with
with open('../sem5/external_app/data/db_config.json') as f:
    app.config['db_config'] = json.load(f)

    #   db_config = json.load(f)
    # print(db_config)

# объединение нескольких путей
provider = SQLProvider(os.path.join(os.path.dirname(__file__), 'sql'))

@app.route('/', methods=['GET'])
def product_handler():
    return render_template('input_category.html')


@app.route('/', methods=['POST'])
def product_result_handler():
    user_data = request.form
    print(user_data)
    dict_user_data = dict(user_data)
    print(dict_user_data)
    res_info = model_route(app.config['db_config'],request.form, provider)
    print('res_info_result=', res_info.result)
    if res_info.status:
        prod_title = 'Результаты из БД'
        return render_template('dynamic.html', prod_title=prod_title, products=res_info.result)
    else:
        return 'Что-то пошло не так'

# @app.route('/', methods=['GET', 'POST'])
# def query_index():
#     # _sql = f"""select prod_name, prod_measure, prod_price from product
#     #            where prod_category = {prod_category}"""
#     # result = select_dict(app.config['db_config'], _sql)
#     # result = select_list(db_config, _sql)
#
#     if request.method == 'GET':
#         return render_template('input_category.html')
#     else:
#         prod_category = request.form.get('prod_category')
#         _sql = provider.get('product.sql', prod_category=prod_category)
#         products = select_dict(app.config['db.config'], _sql)
#
#         if products:
#             prod_title = 'Результат из БД'
#             return render_template('dynamic.html', prod_title = prod_title, products = products)
#         else:
#             return 'Что-то пошло не так'


if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5001)