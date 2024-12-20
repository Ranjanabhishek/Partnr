import json

class Singleton:
    _instances = {}
    def __call__(cls):
        if cls not in cls._instances:
            cls._instances = super().__call__()
        return cls._instances

class RedisConnection(self, Singleton):
    def __init__(self):
        self.connect = {}
    redis_connect  = Singleton()\
    return redis_connect
   
class DBConnect(self, Singleton):
    def __init__(self):
        self.connect = {}
    db_connect  = Singleton()
    return db_connect
   

#used singleton pattern here to create a single instace of all connection throught the application