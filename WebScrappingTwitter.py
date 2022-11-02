from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


servico = Service(ChromeDriverManager().install())
dri = webdriver.Chrome(service=servico)
dri.maximize_window()
dri.get("https://twitter.com/ElonMusk")


dri.implicitly_wait(10)

Name = dri.find_element(by = By.XPATH, value = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span[1]/span').text 
print("O nome do usuário é {}.".format(Name))


WhenAccountGetCriated = dri.find_element(by = By.XPATH, value = '(//span[contains(text(),"Ingressou em")])[1]').text
print("O usuário {}.".format(WhenAccountGetCriated.lower()))

Aro = dri.find_element(by= By.XPATH, value = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/span').text
Followers = dri.find_element(by = By.XPATH, value = "(//a[@href='/{}/followers'])[1]".format(Aro[1:])).text
print('O usuário tem {}.'.format(Followers.lower()))

dri.quit()