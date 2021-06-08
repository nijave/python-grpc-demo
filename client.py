import time
import uuid

import grpc

from echo_server.echo_pb2 import TextMessage
from echo_server.echo_pb2_grpc import EchoServiceStub


class Timer(object):
    def __init__(self, description):
        self.description = description

    def __enter__(self):
        self.start = time.time()

    def __exit__(self, type, value, traceback):
        diff = time.time() - self.start
        if diff < 1:
            diff = str(round(diff*1000, 3)) + "ms"
        print(f"{self.description}: {diff}")


with open("listen_addr.txt", "r") as f:
    channel = grpc.insecure_channel(f.read().strip())
client = EchoServiceStub(channel)

def make_message(content="Text message"):
    return TextMessage(
        timestamp=int(time.time()*1e6),
        id=str(uuid.uuid4()),
        content=content,
    )

def message_stream(count=5, sleep=1):
    for i in range(count):
        yield make_message(
            content=f"Message {i+1}"
        )
        time.sleep(sleep)

with Timer("EchoMany"):
    for response in client.EchoMany(message_stream(count=1000, sleep=0)):
        print(response)