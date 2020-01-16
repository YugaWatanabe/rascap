from PIL import Image
import numpy as np
import capture

def imgcon():

    #撮影する 返り値は画像の名前
    #imgname = capture.cap()

    imgname = "202001140932.jpg"

    #PILでjpgを開いてnumpy行列に変換
    img = []
    img = np.array(Image.open('capicture/' + imgname))
    #numpy配列を文字列に変換　逆は.frombuffer(aa,dtype=int)
    img = img.tostring()

    return img, imgname

if __name__ == '__main__':
    imgcon()