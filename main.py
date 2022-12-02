"""
Вообще, не считаю себя душнилой, но под конструктором класса подразумевают
метод new, но я полагаю, что вы имели ввиду метод init.
"""


class TreeStore:

    def __init__(self, data: list):
        if isinstance(data, list):
            self._data = data
        else:
            self._data = []

    def getAll(self):
        return self._data

    def getItem(self, id: int):
        if isinstance(id, int):
            if id <= 0:
                return 'id will be positive integer'
            try:
                return self._data[id - 1]
            except IndexError:
                return 'List index out of range'
        else:
            return ' id will be integer'

    def getChildren(self, id: int):
        return list(filter(lambda x: x['parent'] == id, self._data))

    def getAllParents(self, id: int):
        """
        В задании указано - начиная от самого элемента, чей id был передан в
        аргументе и до корневого элемента, но в Вашем примере возврщается без
        самого элемента, чей id был передан. Обращаю на это тоже внимание =)
        """
        try:
            new_data = [self._data[id - 1]]
            parent_id = self._data[id - 1]['parent']
            while True:
                new_data += list(
                    filter(lambda x: x['id'] == parent_id, self._data)
                    )
                parent_id = list(
                    filter(lambda x: x['id'] == parent_id, self._data)
                )[0]['parent']
                if parent_id == 'root':
                    return new_data
        except IndexError:
            return 'List index out of range'


items = [
    {"id": 1, "parent": "root"},
    {"id": 2, "parent": 1, "type": "test"},
    {"id": 3, "parent": 1, "type": "test"},
    {"id": 4, "parent": 2, "type": "test"},
    {"id": 5, "parent": 2, "type": "test"},
    {"id": 6, "parent": 2, "type": "test"},
    {"id": 7, "parent": 4, "type": None},
    {"id": 8, "parent": 4, "type": None}
]


ts = TreeStore(items)
print('All - ', ts.getAll())
print('Get Item - ', ts.getItem(7))
print('Get Children - ', ts.getChildren(4))
print('Get Children with empty list - ', ts.getChildren(5))
print('All Parents - ', ts.getAllParents(7))
