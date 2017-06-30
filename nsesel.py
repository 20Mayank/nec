import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#import wget

driver = webdriver.Firefox()
driver.get("https://www.nseindia.com/products/content/derivatives/equities/archieve_fo.htm")

select = Select(driver.find_element_by_id("h_filetype"))
select.select_by_value("fobhav")

d = 1
m = 1
h = 0
while m<13:
	d = 1
	while d<32:
		if m == 1:
			linkm = "JAN"
		if m == 2:
			linkm = "FEB"
		if m == 3:
			linkm = "MAR"
		if m == 4:
			linkm = "APR"
		if m == 5:
			linkm = "MAY"
		if m == 6:
			linkm = "JUN"
		if m == 7:
			linkm = "JUL"
		if m == 8:
			linkm = "AUG"
		if m == 9:
			linkm = "SEP"
		if m == 10:
			linkm = "OCT"
		if m == 11:
			linkm = "NOV"
		if m == 12:
			linkm = "DEC"
		ds = str(d)
		ms = str(m)
		if d<10:
			ds = "0" + ds
		if m<10:
			ms = "0" + ms
		Date = ds + "-" + ms + "-2016"
		link = "fo" + ds + linkm + "2016bhav.csv.zip"
		print(link)

		elem = driver.find_element_by_name("date")
		elem.clear()
		elem.send_keys(Date)
		elem.send_keys(Keys.RETURN)

		driver.find_element_by_class_name("getdata-button").click()

		driver.implicitly_wait(10)

		try:
			link = driver.find_element_by_link_text(link)
			link.click() 	
			h = h+1	
			driver.implicitly_wait(5)
		except:
			print "olla"
				
		if m==2 and d==29:
			d = d + 69
		
		elif m==4 and d==30:
			d = d + 69
		elif m==6 and d==30:
			d = d + 69
		elif m==9 and d==30:
			d = d + 69
		elif m==11 and d==30:
			d = d + 69

		d = d+1
	m = m+1 
	print(h)