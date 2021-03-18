import socket
s = socket.socket()
host = input(str("Tolong masukkin host dari pengirim : "))
port=8080
s.connect((host,port))
print("Connected...")

filename = input(str("Tolong masukkan nama file : "))
file = open(filename, "wb")
file_data = s.recv(1024)
file.write(file_data)
file.close()

print ("File telah diterima")
