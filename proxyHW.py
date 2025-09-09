from abc import ABC, abstractmethod


class Server(ABC):
    @abstractmethod
    def handle_request(self, request):
        pass

class RealServer(Server):
    def handle_request(self, request):
        return f"Processing request: {request}"


class LoggingProxy(Server):
    def __init__(self, real_server):
        self.real_server = real_server

    def handle_request(self, request):
        print(f"[LOG] New request received: {request}")
        result = self.real_server.handle_request(request)
        print(f"[LOG] Response: {result}")
        return result


if __name__ == "__main__":
    real_server = RealServer()
    proxy_server = LoggingProxy(real_server)

    response = proxy_server.handle_request("User login")
    print("Final Response:", response)
