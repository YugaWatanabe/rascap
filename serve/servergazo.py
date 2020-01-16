import socket
import picpic

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.bind(('127.0.0.1', 50090))

    s.listen(1)

    while True:
        soc, addr = s.accept()

        print(str(addr)+"と接続")
        with soc:
            while True:

                data = soc.recv(921600)

                if not data:
                    break

                print("data: {}, addr: {}".format(data, addr))

                img, imgname = picpic.imgcon()

                soc.sendall(img)

                print(imgname)


    
