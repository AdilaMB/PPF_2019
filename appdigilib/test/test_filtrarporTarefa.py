# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys

class TestFiltrarporTarefa():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_filtrarporTarefa(self):
    self.driver.get("http://127.0.0.1:8000/")
    self.driver.set_window_size(1299, 608)
    self.driver.find_element(By.ID, "CLUSTERING").click()
    self.driver.find_element(By.ID, "HIGHTLIGHT").click()
    self.driver.find_element(By.ID, "LABELED").click()
    if EC.text_to_be_present_in_element((By.ID, 'content1'), 'Automated extraction and visualization of quality'):
      print("Sucess")
    print("Error")
  
