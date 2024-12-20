import json

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class RedisConnection(metaclass=SingletonMeta):
    """
    Singleton Redis Connection class.
    """
    def __init__(self):
        self.connect = {} 

    def get_connection(self):
        return self.connect


class DBConnect(metaclass=SingletonMeta):
    """
     Singleton DB Connection class.
    """

    def __init__(self):
        self.connect = {} 

    def get_connection(self):
        return self.connect

if __name__ == "__main__":
    redis1 = RedisConnection()
    redis2 = RedisConnection()

    db1 = DBConnect()
    db2 = DBConnect()
