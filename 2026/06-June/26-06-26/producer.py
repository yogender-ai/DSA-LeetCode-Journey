"""
DSA Lesson · Producer

Pattern : Data Structures & Algorithms
Written : 26 Jun 2026
Time    : O(n)
Space   : O(1)
"""

import asyncio
from aiokafka import AIOKafkaProducer
async def send_message():
    producer=AIOKafkaProducer(
        bootstrap_servers='localhost:9092'

    )
    await producer.start()

    await producer.send_and_wait(
        'orders',
        b"Order created"
    )
    print("message sent successfully")

    await producer.stop()
asyncio.run(send_message())
