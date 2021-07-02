from selenium import webdriver

chrome_driver_path = "/Users/devinanderson/Documents/Chromedriver/chromedriver"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://www.python.org/")
# price = driver.find_element_by_class_name('price')
#print(price.text)
#
# search_bar = driver.find_element_by_xpath('//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]/a')
#
# print(search_bar.text)

event_times = driver.find_elements_by_css_selector(".event-widget time")
event_names = driver.find_elements_by_css_selector(".event-widget li a")
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)


driver.quit()