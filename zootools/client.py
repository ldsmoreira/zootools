import pdb
import socket
import time
import zootools.requests.methods as methods


BUFFER_SIZE = 4096


class Client:

  def __init__(self, host: str, port: int, group: str = "default"):
    self.host = host
    self.port = port
    self.group = group

  def connect(self):
    self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.conn.connect((self.host,self.port))
    return self

  def disconnect(self):
    self.conn.close()

  def _receivedata(self, n) -> bytes:

      RESPONSE_SIZE = n
      fragments = []
      while True: 
        chunk = self.conn.recv(BUFFER_SIZE)
        if chunk:
          fragments.append(chunk)
        if len(chunk) == RESPONSE_SIZE: 
          break

      arr = b''.join(fragments)
      return arr

  
  def _receivesize(self) -> int:
    data_size = self.conn.recv(8)
    data_size = int.from_bytes(data_size, "little")
    return data_size

  def receive(self):
    data_size = self._receivesize()
    return self._receivedata(data_size)

    


  def send(self, bytes: bytes) -> int:
    self.conn.sendall(bytes)
    response = self.receive()
    print(response)

  def get(self, key: str):

    self.send(methods.getfmt(key, self.group))

  def set(self, key: str, data : bytes):

    self.send(methods.setfmt(key, data, self.group))


def client(host: str = '127.0.0.1', port : int = 9009, group: str = "default"):

  return Client(host, port, group).connect()

  


# cli = Client('127.0.0.1', 9009)
# cli.connect()
# for i in range(20):
#   cli.set(key="/home/xap", data = b'lucasmoreira')
# cli.send(b'get /home/xap 12\n\nlucas::toma\nleo::toma\narthur::toma\n\nmoreiralucas')
