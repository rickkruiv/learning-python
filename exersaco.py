import pyautogui as spam
import time

limite_msg = input('Insira o número de mensagens a serem enviada: ')
msg = input('Digite aqui a sua mensagem: ')

i = 0

time.sleep(2)

while int(limite_msg):
    spam.typewrite(msg)
    spam.press('Enter')

i+=1