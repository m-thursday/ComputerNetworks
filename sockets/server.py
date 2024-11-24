'''
Max Thursby
010967047
'''
from base64 import b64encode
from base64 import b64decode
import socket
import time

#Handles ATM cases
def atm(o, amount, total):
	if o == 'B':
		print("check balance")
		return total
	if o == 'W':
		print("withdrawl")
		if amount < total:
			return (total - int(amount))
		else:
			return total
	if o == 'D':
		print("deposit")
		return (total + int(amount))
	if o == 'E':
		print("Exiting")
	else:
		return -1

#Sets up the server	
def server():
	#socket set up
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = '127.0.0.1'
	port = 20001

	#connection set up
	s.bind((host,port))
	s.listen(5)
	
	total = 100

	while True:
		#accept connections
		c, addr = s.accept()
		
		while True:
		#try and except to make sure server is able to handle client requests
			try:
				#attempt to read data from the buffer
				tmp = c.recv(1024)
				#allows graceful disconnect from client
				if not tmp:
					print(f"connection closed: {addr}")
					break
				#decode the client data for use
				cData = tmp.decode()
				#checks for exit flag
				if cData[0] == 'E':
					print(f"Exit Case, final total: {total}")
					break
				#runs ATM functions on total and client data
				total = atm(cData[0],int(cData[1:]), total)
				#sends updated total back to client
				c.sendall(str(total).encode())
				
			except Exception as e:
				print(f"Error: {e}")
				break
	
		c.close()
		# final terminator to close out the loop looking for connections
		if cData[0] == 'E':
			break		

if __name__ == '__main__':
	server()
	
	
