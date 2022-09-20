from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def get_url(year):
  base_url,input = 'https://www.iplt20.com/points-table/men/','year'
  ipl_pointsTable_url = base_url + input
  return ipl_pointsTable_url

# Enter the year to get the points table
url=get_url(2020)


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
    driver.get(url)
    print('Page title:', driver.title)

    # getouter tag
    def get_outer_tag():
      outer_tag=driver.find_elements(By.CLASS_NAME,'ih-pt-tab-bg')
      outerTag=outer_tag[0]
      return outerTag
    
    OT=get_outer_tag()  
   
    # get inner tag

    inner_tag=OT.find_elements(By.CLASS_NAME,'team0')
    for i in inner_tag:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[0].text)
      
    for i in inner_tag:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[1].text)
      
    for i in inner_tag:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[2].text)
      
    for i in inner_tag:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[3].text)

    for i in inner_tag:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[4].text)


    for i in inner_tag:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[5].text)

    for i in inner_tag:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[6].text)


    for i in inner_tag:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[7].text)


    for i in inner_tag:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[8].text)

    for i in inner_tag:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[9].text)

    for i in inner_tag:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[10].text)
    
    for i in inner_tag:
      x=i.find_elements(By.TAG_NAME,'td')[11]
      print(list(x.text.strip()))   
