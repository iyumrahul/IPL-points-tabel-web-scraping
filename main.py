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
    
    outerTag=outer_tag[0]
    
    inner_tag_col1=outerTag.find_elements(By.CLASS_NAME,'table-qualified')

    inner_tag_col2=outerTag.find_elements(By.CLASS_NAME,'ih-t-color')
    
    middle_tag=outerTag.find_elements(By.TAG_NAME,'tr')[0]
    
    inner_tag_col3=middle_tag.find_elements(By.TAG_NAME,'td')
    

    print("###########################")

    position=[]
    

    for col1 in inner_tag_col1:
      print(col1.text)
    
    print("##########################")

    for col2 in inner_tag_col2:
      print(col2.text)

    print("###########################")
    print(inner_tag_col3)
    
    
    
      
    
   
   
      
   
    


    
      
      