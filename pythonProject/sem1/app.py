from flask import Flask, render_template
from pymysql import connect, OperationalError

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello world from flask!'

@app.route('/static')
def static_index():
    return render_template('static.html')

@app.route('/dynamic')
def dynamic_index():
    prod_title = 'Товары мясного отдела'
    products = [
        {'prod_name': 'говядина', 'prod_measure': 'кг', 'prod_price': 900},
        {'prod_name': 'свинина', 'prod_measure': 'кг', 'prod_price': 1200},
        {'prod_name': 'баранина', 'prod_measure': 'кг', 'prod_price': 1500}
    ]
    return render_template('dynamic.html', prod_title=prod_title, products=products)



@app.route('/product')
def product_index():
    try:
        conn = connect(host='127.0.0.1', user='root', password='root', database='supermarket')
        cursor = conn.cursor()
        # return 'Все успешно'

    except OperationalError as err:
        print(err.args)
        return 'Ошибка подключения'

    if cursor:
        sql = f"""select prod_name, prod_measure, prod_price from product
                where prod_category = 1"""

        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
        return 'Все отлично'



if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)