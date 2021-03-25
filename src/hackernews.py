import requests, json
from kafka import KafkaProducer
import logging
import sys
from prometheus_client import start_http_server, Summary, Counter
import random
import time

# set log
logger = logging.getLogger("beststories-logger")
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# init kafka producer
producer = KafkaProducer(bootstrap_servers='kafka-0.kafka-headless.default.svc.cluster.local:9092')

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('beststories_kafka_duration', 'Time beststories kafka producer spent sending messages')
counter = Counter('beststories_hackernews_counter', 'Times of beststories visiting HackerNews')

# Decorate function with metric.
@REQUEST_TIME.time()
def send_id_to_kafka(id):
    producer.send('beststories', str(id).encode())
    # add logs
    logger.info("kafka producer sending beststories id: " + str(id))
    producer.flush()

if __name__ == '__main__':
  # get ids from hackernews
  response = requests.get('https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty')
  ids = json.loads(response.text)
  # Increment by 1
  counter.inc()
  # add logs
  logger.info("got beststories ids from HackerNews")

  # Start up the server to expose the metrics.
  start_http_server(8080)

  # send id with kafka producer
  for id in ids:
    send_id_to_kafka(id)