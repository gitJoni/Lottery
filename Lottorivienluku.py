import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.veikkaus.fi/fi/tulokset#!/tulokset/lotto")

rivit = 0
time.sleep(1)
monta_rivia_luetaan = 100

with open("Lottonumerot.txt", 'w') as tiedosto:
    while rivit < monta_rivia_luetaan:
        earlier_numbers = driver.find_element_by_xpath("""//*[@id="lotto-date-selector"]/div/button[1]/i""")
        earlier_numbers.click()
        time.sleep(0.2)
        numbers = driver.find_elements_by_class_name("game-result")

        teksti = numbers[0].text

        teksti = teksti.split("\n")
            
        for rivi in teksti:
            if rivi.isdigit():
                tiedosto.write(str(rivi) + ' ')
        tiedosto.write('\n')
        rivit += 1