from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverMAneger
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

driver = webdriver.Chrome()
