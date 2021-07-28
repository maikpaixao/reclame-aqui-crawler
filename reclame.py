import requests
from bs4 import BeautifulSoup
from selenium import webdriver

class ReclameAqui:
  def __init__(self):
    self.driver = webdriver.Firefox(executable_path='/home/maikpaixao/Downloads/geckodriver') #add your path
    self.driver.set_window_size(1120, 800)
    self.texts = []

  def extract(self, url):
    self.driver.get(url)
    complains = self.driver.find_elements_by_css_selector("a.link-complain-id-complains")
    complains_links = [complain.get_attribute('href') for complain in complains]

    for link in complains_links[:2]:
      self.driver.get(link)
      text = self.driver.find_element_by_css_selector("div.complain-body p").text
      self.texts.append(text)

    self.driver.close()

if __name__ == '__main__':
  crawler =  ReclameAqui()
  crawler.extract("https://www.reclameaqui.com.br/empresa/kanui/lista-reclamacoes/")
  
  for text in crawler.texts:
    print(text)
    print('==========')
