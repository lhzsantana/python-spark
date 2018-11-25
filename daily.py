import redis
import sys
r = redis.Redis(host='127.0.0.1', port=6379, db=0)

LAST_PREFIX="last"
DAILY_PREFIX="daily"
COUNTER_PREFIX="counter"
WINDOW_PREFIX="window"
LIST_PREFIX="list"
all_genders = ['male', 'female', 'kids', 'unisex']

def control_window(clientIds):
	for clientId in clientIds:
    		for gender in all_genders:
			gender_sum=0
			gender_value=0
			key = WINDOW_PREFIX+":"+DAILY_PREFIX+":"+clientId+":"+gender
			if r.exists(key):
				gender_value= r.get(key)
			r.lpop(LIST_PREFIX+":"+WINDOW_PREFIX+":"+clientId+":"+gender)
			r.rpush(LIST_PREFIX+":"+WINDOW_PREFIX+":"+clientId+":"+gender, gender_value)
			for day in r.lrange(LIST_PREFIX+":"+WINDOW_PREFIX+":"+clientId+":"+gender, 0, 7):
				gender_sum+=int(day)
				r.set(WINDOW_PREFIX+":"+clientId+":"+gender, gender_sum)

if __name__ == "__main__":
	control_window(sys.argv[1].split(","))


