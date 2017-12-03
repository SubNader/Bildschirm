import io
import time
import matplotlib.pyplot as plt
from socket import *
from PIL import Image
from socket import error as socket_error
from gzip import zlib
class server:

	# Constructor
	#def __init__(self, address, port, packet_size=4096):
	def __init__(self, address, port, packet_size=409600):
		self.address = address
		self.port = port
		self.packet_size = packet_size

	# Socket creation
	def create_socket(self):
		sock = socket(AF_INET, SOCK_STREAM)
		sock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
		connection_parameters = (self.address, self.port)
		print 'Starting server on %s port %s' % connection_parameters
		sock.bind(connection_parameters)
		sock.listen(1)
		return sock

	# Start server
	def run(self):
		sock = self.create_socket()
		connection, client_address = sock.accept()
		plt.ion()
		plt.axis('off')
		while True:
			stream_buffer = ''
			try:
				while True:
					try:
						received_data = connection.recv(self.packet_size)
						stream_buffer += received_data
						if len(received_data) < self.packet_size:
							#decompress recived data
							stream_buffer=zlib.decompress(stream_buffer)
							image = Image.open(io.BytesIO(stream_buffer))
							display = plt.imshow(image, interpolation='nearest', aspect='auto')
							plt.pause(0.1)
							stream_buffer = ''
							time.sleep(0.1)
					except:
						print "Failed to Render screenshot !"
			except socket_error as e:
				print 'Error encountered.\n{}\nExiting..'.format(e)
				sock.close()
				exit(1)
			finally:
				sock.close()

if __name__ == '__main__':
	elserver = server('127.0.0.1',9595)
	elserver.run()
