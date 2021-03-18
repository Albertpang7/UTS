import socket

s = socket.socket ()
host = socket.gethostname ()
port = 8080
s.bind((host,port))
s.listen(1)
print(host)
print("Menunggu koneksi ... ")
conn, addr = s.accept()
print(addr, "Sudah terkoneksi ke server")

filename = input(str("Please enter the filename of the file : "))
file = open (filename, 'rb')
file_data=file.read(1024)
conn.send(file_data)
print("Data telah terkirim") 
