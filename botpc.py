import pyautogui
import time

pyautogui.PAUSE = 1
#abrir windows
pyautogui.press('win')
pyautogui.write('Login.xls')
pyautogui.press("Enter")

pyautogui.PAUSE = 3
#preencher login
pyautogui.click(x=483, y=276)
pyautogui.write('Login')

#preencher senha
pyautogui.click(x=513, y=335)
pyautogui.write('Senha')

#fazer login

pyautogui.click(x=536, y=449)
