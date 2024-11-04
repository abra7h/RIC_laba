# функции, связанные с выполнением запроса в базу данных

from database.DBcm import DBContextManager

def select_list(db_config: dict, _sql: str):
    result = ()
    schema = []
    with DBContextManager(db_config) as cursor:
        if cursor is None:
            raise ValueError('Курсор не создан')
        else:
            cursor.execute(_sql)
            result = cursor.fetchall()
            print(cursor.description)
            # в cursor.description[0] лежат имена полей из таблицы

            schema = [item[0] for item in cursor.description]

    return result, schema


def select_dict(db_config: dict, _sql: str):
    result, schema = select_list(db_config, _sql)
    result_dict = []
    for item in result:
        result_dict.append(dict(zip(schema, item)))
    print(result_dict)
    return result


