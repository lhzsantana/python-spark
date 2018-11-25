import redis
r = redis.Redis(host='127.0.0.1', port=6379, db=0)

LAST_PREFIX="last"
COUNTER_PREFIX="counter"
WINDOW_PREFIX="window"
LIST_PREFIX="list"
all_genders = ['male', 'female', 'kids', 'unisex']

def control_window(clientId):
    for gender in all_genders:
	gender_sum=0
	r.lpop(LIST_PREFIX+":"+WINDOW_PREFIX+":"+str(clientId)+":"+gender)
	r.rpush(LIST_PREFIX+":"+WINDOW_PREFIX+":"+str(clientId)+":"+gender, r.get(WINDOW_PREFIX+":"+DAILY_PREFIX+":"+str(clientId)+":"+gender)))
	for day in r.lrange(LIST_PREFIX+":"+WINDOW_PREFIX+":"+str(clientId)+":"+gender, 0, 7):
		gender_sum+=day
	r.set(WINDOW_PREFIX+":"+str(clientId)+":"+gender, gender_sum)
