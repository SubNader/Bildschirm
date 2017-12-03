import io
import time
import socket
import pyscreenshot as ImageGrab
from gzip import zlib
class client:

	# Constructor
	def __init__(self, address, port, packet_size=4096000):
		self.address = address
		self.port = port
		self.packet_size = packet_size

	# Socket creation
	def create_socket(self):
		while True:
			try:
				connection = (self.address, self.port)
				sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
				sock = socket.create_connection(connection)
				sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, self.packet_size)
				sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
				return sock
			except:
				print "[!] Error creating socket .... trying again"
				time.sleep(2)

	# Start client
	def start(self):


		sock = self.create_socket()
		while True:
			try:
				steam_buffer = io.BytesIO()
			  ImageGrab.grab().save(steam_buffer,'PNG')
			  screenshot = steam_buffer.getvalue()
			  # Compress screenshot
			  screenshot = zlib.compress(screenshot)
			  sock.sendall(screenshot)
			  time.sleep(0.1)
			 except:
				print "[!] Error starting client.... trying again"
				time.sleep(2)

if __name__ == '__main__':
	elclient = client('127.0.0.1',9595)
	elclient.start()
