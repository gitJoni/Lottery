import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.veikkaus.fi/fi/tulokset#!/tulokset/eurojackpot")

rivit = 0
monta_rivia_luetaan = 500

with open("Eurojackpotnumerot.txt", 'w') as tiedosto:
    while rivit < monta_rivia_luetaan:
        try:
            earlier_numbers = driver.find_element_by_xpath("""//*[@id="ejackpot-date-selector"]/div/button[1]/i""")
            earlier_numbers.click()
        except:
            break
        time.sleep(0.5)
        numbers = driver.find_elements_by_class_name("game-result")

        teksti = numbers[0].text

        teksti = teksti.split("\n")
            
        for rivi in teksti:
            if rivi.isdigit():
                tiedosto.write(str(rivi) + ' ')
        tiedosto.write('\n')
        rivit += 1