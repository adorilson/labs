import webbrowser
import time
from datetime import datetime

agora = datetime.now()
proximo_minuto = agora.minute + 1
while (agora.minute!=proximo_minuto):
    print(60 - agora.second)
    time.sleep(1)
    agora = datetime.now()

webbrowser.open('http://twitter.com')
