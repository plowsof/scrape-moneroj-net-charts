from pyvirtualdisplay import Display
from selenium import webdriver
from PIL import Image
'''
Darknet forum subscribers https://moneroj.net/dread_subscribers/
Coincards usage https://moneroj.net/coincards/
Merchants acceptance https://moneroj.net/merchants/
Merchants increase (%) https://moneroj.net/merchants_percentage/
Merchants increase (total numbers) https://moneroj.net/merchants_increase/
Coinmarketcap Rank https://moneroj.net/rank
Dominance https://moneroj.net/dominance
Marketcap https://moneroj.net/marketcap
Reddit daily comments https://moneroj.net/social6
Reddit daily posts https://moneroj.net/social7

'''

websites = ["sfmodel","merchants","merchants_percentage","merchants_increase","rank","dominance","coincards","marketcap","social6","social7"]
display = Display(visible=0, size=(1300,1000))
display.start()

driver = webdriver.Firefox()
driver.maximize_window()
driver.set_window_size(1300, 1000) 
#driver.get("https://bounties.monero.social/")
for site in websites:
	main_url = f"https://moneroj.net/{site}/"
	driver.get(main_url)
	if site == "sfmodel":
		driver.execute_script("window.scrollTo(0, 95)") 
	driver.save_screenshot(f"lol-{site}.png")
	im = Image.open(f"lol-{site}.png")
	if site == "sfmodel":
		im = im.crop((246, 18, 1276, 846))
	else:
		im = im.crop((247, 23, 1276, 851))
	im.save(f"lol-{site}.png")
