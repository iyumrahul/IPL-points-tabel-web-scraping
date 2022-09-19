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
    outer_tag=driver.find_elements(By.CLASS_NAME,'ih-pt-tab-bg')
    
    outerTag=outer_tag[0]

    inner_tag_col1=outerTag.find_elements(By.CLASS_NAME,'table-qualified')
    inner_tag_col2=outerTag.find_elements(By.CLASS_NAME,'ih-t-color')
    
    inner_tag_col3=outerTag.find_elements(By.TAG_NAME,'tr')
    
    position=[]
    
    for col1 in inner_tag_col1:
      print(col1.text)
    print("##########################")
    
    for col2 in inner_tag_col2:
      print(col2.text)
    print("###########################")

    for col3 in inner_tag_col3:
      print(col3.find_elements(By.XPATH,"//td[@class='ng-binding']")[0].text)

    print("###########################")
    for col4 in inner_tag_col3:
      print(col4.find_elements(By.XPATH,"//td[@class='ng-binding']")[1].text)
    for col5 in inner_tag_col3:
      print(col5.find_elements(By.XPATH,"//td[@class='ng-binding']")[2].text)
    for col6 in inner_tag_col3:
      print(col6.find_elements(By.XPATH,"//td[@class='ng-binding']")[3].text)
    for col7 in inner_tag_col3:
      print(col7.find_elements(By.XPATH,"//td[@class='ng-binding']")[4].text)
    for col8 in inner_tag_col3:
      print(col8.find_elements(By.XPATH,"//td[@class='ng-binding']")[5].text)
    for col9 in inner_tag_col3:
      print(col9.find_elements(By.XPATH,"//td[@class='ng-binding']")[6].text)
    for col10 in inner_tag_col3:
      print(col10.find_elements(By.XPATH,"//td[@class='ng-binding']")[7].text)
    for col11 in inner_tag_col3:
      print(col11.find_elements(By.XPATH,"//td[@class='ng-binding']")[8].text)
      
    
    
    
   
   
      
   
    


    
      
      