# First way of using singleton

class SingletonNew:
    _instance = {}
    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

s1 = SingletonNew()
s2 = SingletonNew()

print(id(s1),  id(s2))
print(s1 is s2)


# Second way of using singleton

class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwargs):
        if cls is not cls._instance:
            cls._instance[cls] = super().__call__(*args, **kwargs)

        return cls._instance[cls]

class SingletonBase(metaclass=SingletonMeta):
    pass

class Logger(SingletonBase):
    def __init__(self):
        self.logs = []

class Database(SingletonBase):
    def __init__(self):
        self.connection = "connected to DB"


logger1 = Logger()
logger2 = Logger()
db1 = Database()
db2 = Database()

print(logger1 is logger2)
print(db1 is db2)
print(logger1 is db1)









