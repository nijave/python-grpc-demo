import grpc
import logging
import time

import concurrent.futures

from echo_server.echo_pb2 import TextMessage
from echo_server import echo_pb2_grpc

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class EchoService(
    echo_pb2_grpc.EchoServiceServicer
):
    def Echo(self, request, context):
        logger.info("Got request %s with context %s", type(request), context)
        return TextMessage(
            timestamp=int(time.time()*1e6),
            id=request.id,
            content=request.content
        )
    
    def EchoMany(self, request, context):
        for msg in request:
            yield self.Echo(msg, context)


if __name__ == "__main__":
    logger.info("Initializing server")
    server = grpc.server(concurrent.futures.ThreadPoolExecutor(max_workers=2))
    echo_pb2_grpc.add_EchoServiceServicer_to_server(
        EchoService(), server
    )
    with open("listen_addr.txt", "r") as f:
        server.add_insecure_port(f.read().strip())
    logger.info("Starting server")
    server.start()
    logger.info("Waiting for termination")
    server.wait_for_termination()
