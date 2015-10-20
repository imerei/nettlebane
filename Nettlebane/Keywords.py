from selenium import webdriver
import xpathRepo #xpathRepo.py must be stored in the same directory in order to be imported
import csv

class TestCase:
  """A list of actions that can be used to design test cases"""

  def launchBrowser(self):
      try:
          print "Launching browser..."
          self.driver = webdriver.Firefox()
          print "Pass"
      except:
          print "Fail: Unable to launch browser."

  def visitSite(self):
      try:
          print "Visiting website..."
          site = "http://www.meetup.com"
          print "Website is " + site
          driver = self.driver
          driver.get(site)
          print "Pass"
      except:
          print "Fail: Unable to visit site."

  def assertTitle(self):
      try:
          print "Asserting title..."
          return "Meetup" in self.driver.title
          print "Pass"
      except:
          print "Fail: Unable to find title."

  def click_Login(self):
      try:
          print "Clicking on element..."
          print "Element is " + xpathRepo.logIn #This can be found and edited in xpathRepo.py
          driver = self.driver
          driver.find_element_by_xpath(xpathRepo.logIn).click()
          print "Pass"
      except:
          print "Fail: Unable to click on element."

  def click_Submitbtn(self):
      try:
          print "Clicking on element..."
          print "Element is " + xpathRepo.submit
          driver = self.driver
          driver.find_element_by_xpath(xpathRepo.submit).click()
          print "Pass"
      except:
           print "Fail: Unable to click on element."

  def inputEmail(self):
      try:
          f = open('stored_data.csv') #This is where credentials are stored so that it is not hardcoded
          for row in csv.reader(f):
              email = row[0]
          print "Entering email address..."
          print "Data is " + email
          driver = self.driver
          driver.find_element_by_xpath(xpathRepo.emailID).send_keys(email)
          print "Pass"
      except:
           print "Fail: Unable to input data"

  def inputPwd(self):
        try:
            f = open('stored_data.csv') #Please note, this is stored as plain text so be careful
            for row in csv.reader(f):
                pwd = row[1]
            print "Entering password..."
            print "Data is " + pwd
            driver = self.driver
            driver.find_element_by_xpath(xpathRepo.pwd).send_keys(pwd)
            print "Pass"
        except:
            print "Fail: Unable to input data"

  def quitBrowser(self):
      try:
          print "Closing browser..."
          self.driver.quit()
          print "Browser closed."
      except:
          print "Unable to quit browser."