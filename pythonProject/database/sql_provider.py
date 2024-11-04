import os
from string import Template

class SQLProvider:

    def __init__(self, file_path):
        self.scripts = {}
        # генерация всех файлов и каталогов заданного пути
        for file in os.listdir(file_path):
            _sql = open(f'{file_path}/{file}').read()
            self.scripts[file] = Template(_sql) # adding to dictionary

    # **kwargs используется для передачи произвольного числа аргументов, которые будут собраны в словарь
    def get(self, file, **kwargs):
        sql = self.scripts[file].substitute(**kwargs) # заменяем значение в шаблоне
        return sql