import requests, json
from kafka import KafkaProducer
import logging
import sys

logger = logging.getLogger("beststories-logger")
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

response = requests.get('https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty')
ids = json.loads(response.text)
logger.info("got beststories ids from HackerNews")

producer = KafkaProducer(bootstrap_servers='kafka-0.kafka-headless.default.svc.cluster.local:9092')

for id in ids:
  producer.send('beststories', str(id).encode())
  logger.info("kafka producer sending story id: " + str(id))
  producer.flush()