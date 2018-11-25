import redis
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

LAST_PREFIX="last"
COUNTER_PREFIX="counter"
WINDOW_PREFIX="window"
DAILY_PREFIX="daily"
all_genders = ['male', 'female', 'kids', 'unisex']

def save_access(clientId, gender):
	r = redis.Redis(host='127.0.0.1', port=6379, db=0)
	r.set(LAST_PREFIX+str(clientId), gender)
	r.incr(COUNTER_PREFIX+":"+str(clientId)+":"+gender)
	r.incr(WINDOW_PREFIX+":"+str(clientId)+":"+gender)
	r.incr(WINDOW_PREFIX+":"+DAILY_PREFIX+":"+str(clientId)+":"+gender)

def save_rdd(rdd):
	rdd.foreachPartition(save_records)

def save_records(records):
	for record in records:
		parameters = record.split(" ")
		save_access(parameters[0], parameters[1])

#cluster connection
sc = SparkContext("local[2]", "NetworkWordCount")
ssc = StreamingContext(sc, 1)

#stream handling
genders_stream = ssc.socketTextStream("localhost", 9999)
genders_stream.foreachRDD(lambda rdd: save_rdd(rdd))

#computation
ssc.start()
ssc.awaitTermination()


