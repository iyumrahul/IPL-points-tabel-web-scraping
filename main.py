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
    
    outer_tag=driver.find_elements(By.CLASS_NAME,'ih-pt-tab-bg')
    outerTag=outer_tag[0]
  
    # get inner tag
    inner_tag_col1=outerTag.find_elements(By.CLASS_NAME,'table-qualified')
    for col1 in inner_tag_col1:
      print(col1.text)
    
    inner_tag_col2=outerTag.find_elements(By.CLASS_NAME,'ih-t-color')
    for col2 in inner_tag_col2:
      print(col2.text)
    
    inner_tag_col3=outerTag.find_elements(By.CLASS_NAME,'team0')
    for i in inner_tag_col3:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[3].text)

    for i in inner_tag_col3:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[4].text)


    for i in inner_tag_col3:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[5].text)

    for i in inner_tag_col3:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[6].text)


    for i in inner_tag_col3:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[7].text)


    for i in inner_tag_col3:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[8].text)

    for i in inner_tag_col3:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[9].text)

    for i in inner_tag_col3:
      x=i.find_elements(By.TAG_NAME,'td')
      print(x[10].text)
    
    inner_tag_col_form=outerTag.find_elements(By.CLASS_NAME,'ih-pt-fb-w')
    for col_form in inner_tag_col_form:
      print(list(col_form.text.strip()))