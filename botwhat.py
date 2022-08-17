#importar bibliotecas
import pywhatkit
import keyboard
import time
from datetime import datetime
#contatos que serao enviado as msg
contatos= ["+5111968568960"] #necessario inserir um numero
#definir intervalo
time.sleep(10)
while len(contatos)>=1:
 #enviar mensagens
 pywhatkit.sendwhatmsg(contatos[0], "horario marcado para as 15horas nao esquecer", datetime.now().hour,datetime.now().minute+2)
 del contatos[0]
 time.sleep(30)
 keyboard.press_and_release("ctrl + w")
#testar
