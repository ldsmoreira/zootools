import pdb
import socket
import time


BUFFER_SIZE = 4096


class Client:

  def __init__(self, host: str, port: int):
    self.host = host
    self.port = port

  def connect(self):
    self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    self.conn.connect((self.host,self.port))

  def disconnect(self):
    self.conn.close()

  def _receivedata(self, n) -> bytes:
      # Helper function to recv n bytes or return None if EOF is hit
      # pdb.set_trace()
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
    self.conn.send(bytes)
    response = self.receive()
    print(response)

cli = Client('127.0.0.1', 9009)
cli.connect()
cli.send(b'get /home/xap 12\n\nlucas::toma\nleo::toma\narthur::toma\n\nmoreiralucas')
