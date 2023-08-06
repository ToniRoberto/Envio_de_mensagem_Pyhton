#importar as bibliotecas
import pywhatkit
import keyboard
import time
from datetime import datetime

#definir os contatos
contato = ['+contato numero 1', '+contato numero 2']

#definir intervalo
while len(contato) >= 1:
    #enviar mensagem
    pywhatkit.sendwhatmsg(contato[0], 'Você esta recebendo uma mensagem automatizada!', datetime.now().hour,datetime.now().minute + 2)
    del contato[0]
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')