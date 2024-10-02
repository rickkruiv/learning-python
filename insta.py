from selenium import webdriver
from selenium.webdriver.common.by import By
import time

navegador = webdriver.Chrome('chromedriver.exe')

#p1: entrar no site
navegador.get('https://www.instagram.com/')
time.sleep(5)
#p2: fazer login
navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("po.rique")
time.sleep(1.5)
navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("henrique2006*")
time.sleep(1.5)
navegador.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]').click()
time.sleep(10)

#p3: nop save
navegador.find_element(By.XPATH, '//*[@id="mount_0_0_Bi"]/div/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/div/div/section/div/button')

time.sleep(10)

#p4: nop notific

#p5: clicar pesquisar

#p6: pesquisar

#p7: clicar no perfil

#p8: seguir
