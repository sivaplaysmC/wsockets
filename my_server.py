import socket


conn = socket.socket(socket.AF_INET , socket.SOCK_STREAM) 
ip = "localhost" ; port = 6969
conn.bind((ip , port))
print(f"server to {ip , port}")
conn.listen()
conne , addr = conn.accept()
with conn :
    print(f"connected by {addr}")
    while True :
        data = conne.recv(1024)
        stri = data.decode()
        stri = stri.strip("\n")
        print(f"Receieved {stri}")
        if not data :
            break
        inp = ("You Said " + data.decode("UTF-8")).encode()
        conne.sendall(inp)

conn.close()
