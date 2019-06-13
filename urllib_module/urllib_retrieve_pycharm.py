import os
# import urllib
from urllib import request

url = 'https://i0.wp.com/cdnssl.ubergizmo.com/wp-content/uploads/2019/06/google-pixel-4-render-640x364.png?resize=640%2C364&ssl=1'

opener = request.build_opener()

request.install_opener(opener)

path = os.getcwd()

request.urlretrieve(url, path + '/test2.jpg')

print("Downloaded file at %s" % path)