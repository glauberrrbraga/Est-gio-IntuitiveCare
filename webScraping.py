import time
import requests
from selenium import webdriver

# Grab content from URL
url = "http://www.ans.gov.br/prestadores/tiss-troca-de-informacao-de-saude-suplementar"

# Launch Google Chrome
driver = webdriver.Chrome("C:\\Users\\glaub\\OneDrive\\Documentos\\Teste Estagio\\chromedriver.exe") 
option = webdriver.ChromeOptions()
prefs = {"plugins.always_open_pdf_externally": True}
option.add_experimental_option("prefs",prefs)
driver =  webdriver.Chrome(options = option)

# Find the PDF 
driver.get(url);
# Close first popup
driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div/div/div[1]/button/span').click()
# Browse to next page
driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div[2]/div[2]/a').click() 
# Close second popup
driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div/div/div/div[1]/button/span').click() 
# Download PDF
driver.find_element_by_xpath('/html/body/div[9]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[3]/a').click()
time.sleep(20)
driver.close()





