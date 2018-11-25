# Python and Spark
Delevoped as a PoC to background periodic task and a Spark streaming PoC

## Create virtual environment and import dependencies
$ virtualenv -p python3 python-spark
$ cd python-spark  
$ pip import redis  
$ pip import pyspark  

## Python
To run the periorid task do:  
$ python daily.py 1,2,3  

## Spark
### Download and start Spark cluster
Refer to https://spark.apache.org/docs/latest/index.html#downloading
./sbin/start-master.sh  
./sbin/start-slave.sh <master-spark-URL>  

### Run streaming.py
./bin/spark-submit streaming.py localhost 9000  

### Test creating messages in the socket
$ nc -lk 9999  
$ 1 male  
$ 2 female  
$ 3 kids  
$ 4 unisex  
