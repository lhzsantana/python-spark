import redis
import random
import datetime
from flask import Flask
app = Flask(__name__)

r = redis.Redis(host='127.0.0.1', port=6379, db=0)

LAST_PREFIX="last"
COUNTER_PREFIX="counter"
WINDOW_PREFIX="window"
DAILY_PREFIX="daily"
LIST_PREFIX="list"
all_genders = ['male', 'female', 'kids', 'unisex']

def save_access(clientId, gender):
	r.set(LAST_PREFIX+str(clientId), gender)
	r.incr(COUNTER_PREFIX+":"+str(clientId)+":"+gender)
	r.incr(WINDOW_PREFIX+":"+str(clientId)+":"+gender)
	r.incr(WINDOW_PREFIX+":"+DAILY_PREFIX+":"+str(clientId)+":"+gender)
