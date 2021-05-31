import logging

logging.basicConfig(level=logging.INFO)

class Decorator(object):
    def __init__(self):
        pass

    def hand_div(self,arg):
        def _hand_div(func):
            def wrapper(*args,**kwargs):
                logging.info(arg)
                func(*args,kwargs)
                logging.info(arg)
            return wrapper
        return _hand_div