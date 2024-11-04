from flask import render_template, Blueprint, current_app, request
from database.select import select_dict

blueprint_query = Blueprint('query_bp', __name__, template_folder='templates')


@blueprint_query.route('/category', methods=['GET', 'POST'])

def query_category():
    if request.method == 'POST':
        category = request.form['category']
        _sql = f"""select * from product
                   where prod_category = {category}"""
        result = select_dict(current_app.config['db_config'], _sql)
        if result:
            prod_title = f'Все записи по категории {category}'
            print(result)
            return render_template('dynamic.html', prod_title=prod_title, products=result)
        else:
            return 'Результат не получен'
    else:
        return render_template('query_category.html')


@blueprint_query.route('/cost', methods=['GET', 'POST'])

def query_cost():
    if request.method == 'POST':
        cost = request.form['cost']
        print(cost)
        _sql = f"""select * from product
                   where prod_price = {cost}"""
        result = select_dict(current_app.config['db_config'], _sql)
        print(result)
        if result:
            prod_title = f'Все записи по цене {cost}'
            print(result)
            return render_template('dynamic.html', prod_title=prod_title, products=result)
        else:
            return 'Результат не получен'
    else:
        return render_template('query_cost.html')