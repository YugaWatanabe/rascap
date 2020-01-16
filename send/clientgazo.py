import socket
import datetime
import numpy as np
from PIL import Image

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # サーバを指定
    s.connect(('127.0.0.1', 50090))
    # サーバにメッセージを送る　
    s.sendall(b'please picture!!')
    # ネットワークのバッファサイズは921600。サーバからの文字列を取得する
    data = s.recv(921600)
    #print(repr(data))

    pil_img = np.fromstring(data,dtype=np.uint8)

    #形状を復元する
    pil_img = np.reshape(pil_img,(288, 352, 3)) 

    #配列から画像に変換
    pil_img = Image.fromarray(pil_img)
    #RGBであることを確認
    print(pil_img.mode)

    #画像を保存する
    now = datetime.datetime.now()
    pil_img.save(now.strftime('image/client_%Y%m%d%H%M.jpg'))