import Keywords #Keywoards.py must be stored in the same directory in order to be imported
from Keywords import TestCase

print "Starting test..."

test_steps = Keywords.TestCase()

#All functions are defined and can be edited in Keywords.py
test_steps.launchBrowser()
test_steps.visitSite()
test_steps.assertTitle()
test_steps.click_Login()
test_steps.inputEmail()
test_steps.inputPwd()
test_steps.click_Submitbtn()
test_steps.quitBrowser()