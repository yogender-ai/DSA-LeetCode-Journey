# Sandbox

Small experiments outside DSA, kept here so nothing gets lost.

| Folder | What it is | Run |
|:--|:--|:--|
| `ml-basics/` | NumPy array basics, reading an image into an array with OpenCV | `pip install numpy opencv-python` — put any `image.png` next to the script |
| `kafka-order-service/` | Kafka + Zookeeper via Docker Compose, async producer sending an `orders` event | `docker compose up -d` then `pip install aiokafka && python producer.py` |
