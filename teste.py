from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import subprocess

# Caminho para o executável do Chrome
#chrome_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

# Executa o Chrome com o modo de depuração ativado
#subprocess.run([chrome_path, '--remote-debugging-port=9222'])

#ou executa o código abaixo no cmd

exit(0)

#"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

driver = webdriver.Chrome(options=chrome_options)

#link do moodle
driver.get("https://graduacao.mackenzie.br/login/index.php")

#clica no login do moodle
driver.find_element("xpath", "/html/body/div[2]/div[2]/div/div/section/div/div/div/div/div[2]/div/div[1]/a").click()

input("algo")
driver.quit()