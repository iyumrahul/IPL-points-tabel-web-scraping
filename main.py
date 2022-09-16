from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

ipl_pointTable_url = 'https://www.iplt20.com/points-table/men/2022'


def get_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


if __name__ == "__main__":
    print('Creating Driver')
    driver = get_driver()

    print('Feteching the page')
    driver.get(ipl_pointTable_url)
    print('Page title:', driver.title)
    
    print("##########################")

    # get Point list tabel by class name
    outer_tag=driver.find_elements(By.CLASS_NAME,'ih-pcard-wrap')
    print(len(outer_tag))
    outerTag=outer_tag[0]
    inner_tag=outerTag.find_elements(By.CLASS_NAME,'team0')
    print(len(inner_tag))

    print("###########################")

    position=[]
    

    for tag in inner_tag:
      print(tag.text[0][0])
    print("##########################")
    for tag in inner_tag[1:][0:]:
      print(tag.text)
   
   
      
   
    


    
      
      