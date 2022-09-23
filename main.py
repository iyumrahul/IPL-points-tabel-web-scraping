from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd


def get_url(year):
    base_url, input = 'https://www.iplt20.com/points-table/men/', str(year)
    ipl_pointsTable_url = base_url + input
    return ipl_pointsTable_url


# Enter the year to get the points table
url = get_url(2022)


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

    # get tag
    def get_outer_tag():
        outer_tag = driver.find_elements(By.CLASS_NAME, 'ih-pt-tab-bg')
        outerTag = outer_tag[0]
        inner_tag = outerTag.find_elements(By.CLASS_NAME, 'team0')
        return inner_tag

    Tag = get_outer_tag()

    # definig a function to get the data column wise
    def get_position_col():
      tags = Tag
      Place=[]
      for i in tags:
        place = i.find_elements(By.TAG_NAME, 'td')[0].text
        Place.append(place)
      return Place
    def get_Team_col():
      tags = Tag
      Team=[]
      for i in tags:
        team = i.find_elements(By.TAG_NAME, 'td')[1].text
        Team.append(team)
      return Team
    def get_Pld_col():
      tags = Tag
      Pld=[]
      for i in tags:
        pld = i.find_elements(By.TAG_NAME, 'td')[2].text
        Pld.append(pld)
      return Pld
    def get_Won_col():
      tags = Tag
      Won=[]
      for i in tags:
        won = i.find_elements(By.TAG_NAME, 'td')[3].text
        Won.append(won)
      return  Won
    def get_Lost_col():
      tags = Tag
      Lost=[]
      for i in tags:
        lost = i.find_elements(By.TAG_NAME, 'td')[4].text
        Lost.append(lost)
      return  Lost
    def get_Tied_col():
      tags = Tag
      Tied=[]
      for i in tags:
        tied = i.find_elements(By.TAG_NAME, 'td')[5].text
        Tied.append(tied)
      return Tied
    def get_No_Result_col():
      tags = Tag
      No_Result=[]
      for i in tags:
        noResult = i.find_elements(By.TAG_NAME, 'td')[6].text
        No_Result.append(noResult)
      return No_Result
    def get_Net_RR_col():
      tags = Tag
      Net_RR=[]
      for i in tags:
        net_rr = i.find_elements(By.TAG_NAME, 'td')[7].text
        Net_RR.append(net_rr)
      return Net_RR
    def get_For_col():
      tags = Tag
      _For=[]
      for i in tags:
        _for = i.find_elements(By.TAG_NAME, 'td')[8].text
        _For.append(_for)
      return  _For
    def get_Against_col():
      tags = Tag
      Against=[]
      for i in tags:
        against = i.find_elements(By.TAG_NAME, 'td')[9].text
        Against.append(against)
      return Against
    def get_Pts_col():
      tags = Tag
      Pts=[]
      for i in tags:
        points = i.find_elements(By.TAG_NAME, 'td')[10].text
        Pts.append(points)
      return Pts
    def get_Form_col():
      tags = Tag
      Form=[] 
      for i in tags:
        form = i.find_elements(By.TAG_NAME, 'td')[11].text.replace('\n','')
        x = list(form)
        Form.append(list(x))
      return Form
    
    # defining the function to get all the details of the column 
    def get_data():
      position_column,team_name_column,played_column,won_column=get_position_col(),get_Team_col(),get_Pld_col(),get_Won_col()
      lost_column,tied_column,no_result_column,net_run_rate_column=get_Lost_col(),get_Tied_col(),get_No_Result_col(),get_Net_RR_col()
      for_column,against_column,pts_column,form_column=get_For_col(),get_Against_col(),get_Pts_col(),get_Form_col()  
     
      return {'Position':position_column,'Team':team_name_column,'Pld':played_column,'Won':won_column,
              'Lost':lost_column,'Tied':tied_column,'No_result':no_result_column,'Net_RR':net_run_rate_column,
              'For':for_column,'Against':against_column,'Points':pts_column,'Form':form_column }
          
    # function calling
    dictonary_data = get_data()

    df = pd.DataFrame(dictonary_data)
    df.to_csv('IPL T20 points Tabel 2022', index=None)
    print(df)
