import sys
import urllib.request
from audio_to_text import convert_speech_to_text


page = urllib.request.urlopen('http://cdn.fbsbx.com/v/t59.3654-21/31357025_10214176070550168_934519561451995136_n.jpg/audioclip-1526072695.jpg?_nc_cat=0&oh=cf5b56a32cb8ffbf21cf21da7ec99a9f&oe=5AF875ED')

print(convert_speech_to_text(page),'en-US')




