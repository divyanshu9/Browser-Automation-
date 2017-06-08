from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
import sys

#capabilities = webdriver.DesiredCapabilities().FIREFOX
#capabilities["marionette"] = False
#binary = FirefoxBinary(r'/usr/lib/firefox/firefox')
#driver = webdriver.Firefox(firefox_binary=binary, capabilities=capabilities)

driver = webdriver.Chrome()
driver.get("https://www.omdbapi.com")
assert "OMDb" in driver.title
elem = driver.find_element_by_name("t")
elem.clear()
def capture(query):
	elem.clear()
	print "\n Trying query: %s \n" % (query)
	elem.send_keys("")
	elem.send_keys(query)
	elem.send_keys(Keys.RETURN)
	assert "No results found." not in driver.page_source
	data = driver.find_element_by_css_selector('pre.alert-success')
	
	try:
		text = data.text
		text = text +","+"\n"
		text = text.encode('ascii', 'ignore').decode('ascii')
		print(text)
		with open("mvdb.json", "a") as f:
			f.write("\n"+text)
		#file("mvdb.json", "w").write(text)
	except Error:
		print "Error"
		sys.exit()
#driver.close()

def search():
	global query
	for query in querys:
		capture(query)

def check():
	print "in check"
	global querys
	try:
		list = open("namelist2.txt", "r")
		querys = list.readlines()
		k=0
		while k<len(querys):
			querys[k] = querys[k].strip()
			k+=1
	except IOError:
		print "\n check the name list\n"
		sys.exit(1)
	search()
		
if __name__ == '__main__':
	check()
