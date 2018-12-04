import pymongo

class MongoDBHelper:
    """数据库操作"""

    def __init__(self, collection_name=None):
        # 启动mongo
        self._client = pymongo.MongoClient('localhost', 27017)
        # 使用test数据库
        self._test = self._client['test']
        # 创建指定的集合
        self._name = self._test[collection_name]

    def insert_item(self, item):
        """插入数据"""
        self._name.insert_one(item)

    def find_item(self):
        """查询数据"""
        data = self._name.find()
        return data


def main():
    mongo = MongoDBHelper('collection')
    mongo.insert_item({'a': 1})


if __name__ == '__main__':
    main()