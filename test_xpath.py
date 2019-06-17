import requests
from lxml import etree



url = "https://www.ubergizmo.com/articles/quad-bayer-camera-sensor/"
get_page = requests.get(url)
page = get_page.text
tree = etree.parse(page)

