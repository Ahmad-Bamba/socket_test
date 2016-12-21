import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8008))
print(s.send("I like to program. I do it every day. Even if I didn't, that would be ok! :)".encode("utf-8")))
print("end of program")
