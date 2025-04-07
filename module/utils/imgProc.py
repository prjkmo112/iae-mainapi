import io
import base64
from PIL import Image

from module.logger import logger

class ImgProc:
    @staticmethod
    def img_np2byte(npimg, format=None):
        img = Image.fromarray(npimg)
        byteimg = io.BytesIO()
        img.save(byteimg, format)

        return byteimg

    @staticmethod
    def img_byte2base64(byteimg):
        base64img = base64.b64encode(byteimg).decode("utf-8")
        return base64img
