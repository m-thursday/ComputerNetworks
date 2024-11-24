'''
Max Thursby
010967047
'''
from base64 import b64encode
from base64 import b64decode
import socket
import time

def inputCheck(o, oList):
    if o.isnumeric():
        o = int(o)
        while o not in oList:
            print(f"{o} is numeric but not an option, please try again ")
            o = input(">>> ")
            if o.isnumeric():  # Recheck after user input
                o = int(o)
            else:
                return inputCheck(o, oList)
        return o
    else:
        print(f"{o} is not an option, please try again ")
        o = input(">>> ")
        return inputCheck(o, oList)

def updateCheck():
	tmp = input("Update amount: ")
	if tmp.isnumeric():
		return str(tmp)
	else:
		print(f"{tmp} is not an integer, please try again")
		return updateCheck()

# Menu for simple GUI
def menu():
	oList = [1, 2, 3, 4]
	print("\n--------Menu--------")
	print("1: Check Balance")
	print("2: Withdraw")
	print("3: Deposit")
	print("4: Exit")
	print("--------------------")
	o = input(">>> ")
	o = inputCheck(o, oList)		
	return o
	
# Basic table to update based on flag
def switch(o): #send data in format [ 1 byte flag | X bytes update data ]
	if o == 1: # Flag  b
		return "B0"
	if o == 2: # w
		tmp = updateCheck()	
		return "W" + str(tmp)
	if o == 3: # d
		tmp = updateCheck()
		return "D" + str(tmp)
	if o == 4: # e
		return "E0"
		
def client():
	#socket set up
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = '127.0.0.1'
	port = 20001

	#connection
	s.connect((host,port))

	while True:
		o = menu()
		msg = switch(o)
		str(msg)
		#receive data for action
		s.sendall(msg.encode())
		if msg == "E0":
			print(f"Exit Case, final total: {total}")
			break
		total = s.recv(1024).decode()
		print("\n------------------------------")
		print(f" Current Balance: {total}")
		enter = input("-----------------press enter to continue::")
		
		

if __name__ == '__main__':
	client()
	

