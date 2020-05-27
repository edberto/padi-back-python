import datetime
from . import routes
from .wrapper import wrap

@routes.route('/')
def index():
    return wrap('Hello World', 'Success', 200)                                                                                                                   