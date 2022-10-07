from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd

#  url making for each year
year_list = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,2020, 2021, 2022]

def get_url(year):
    base_url, input = 'https://www.iplt20.com/points-table/men/', str(year)
    ipl_pointsTable_url = base_url + input
    return ipl_pointsTable_url

# Enter the year to get the points table
def url_of_years():
  URL=[]
  for years in year_list:
    URL.append(get_url(years))
  return URL
url=url_of_years()

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
    #driver.get(url)
    print('Page title:', driver.title)

    # get tag
    def get_outer_tag():
        outer_tag = driver.find_elements(By.CLASS_NAME, 'ih-pt-tab-bg')
        outerTag = outer_tag[0]
        inner_tag = outerTag.find_elements(By.CLASS_NAME, 'team0')
        return inner_tag

    # definig a function to get the data column wise
      
    def get_position_col():
        tags = get_outer_tag()
        Place = []
        for i in tags:
            place = i.find_elements(By.TAG_NAME, 'td')[0].text
            Place.append(place)
        return Place

    def get_Team_col():
        tags = get_outer_tag()
        Team = []
        for i in tags:
            team = i.find_elements(By.TAG_NAME, 'td')[1].text
            Team.append(team)
        return Team

    def get_Pld_col():
        tags = get_outer_tag()
        Pld = []
        for i in tags:
            pld = i.find_elements(By.TAG_NAME, 'td')[2].text
            Pld.append(pld)
        return Pld

    def get_Won_col():
        tags = get_outer_tag()
        Won = []
        for i in tags:
            won = i.find_elements(By.TAG_NAME, 'td')[3].text
            Won.append(won)
        return Won

    def get_Lost_col():
        tags = get_outer_tag()
        Lost = []
        for i in tags:
            lost = i.find_elements(By.TAG_NAME, 'td')[4].text
            Lost.append(lost)
        return Lost

    def get_Tied_col():
        tags = get_outer_tag()
        Tied = []
        for i in tags:
            tied = i.find_elements(By.TAG_NAME, 'td')[5].text
            Tied.append(tied)
        return Tied

    def get_No_Result_col():
        tags = get_outer_tag()
        No_Result = []
        for i in tags:
            noResult = i.find_elements(By.TAG_NAME, 'td')[6].text
            No_Result.append(noResult)
        return No_Result
    def get_Net_RR_col():
        tags = get_outer_tag()
        Net_RR = []
        for i in tags:
            net_rr = i.find_elements(By.TAG_NAME, 'td')[7].text
            Net_RR.append(net_rr)
        return Net_RR
    def get_For_col():
        tags = get_outer_tag()
        _For = []
        for i in tags:
            _for = i.find_elements(By.TAG_NAME, 'td')[8].text
            _For.append(_for)
        return _For

    def get_Against_col():
        tags =get_outer_tag()
        Against = []
        for i in tags:
            against = i.find_elements(By.TAG_NAME, 'td')[9].text
            Against.append(against)
        return Against

    def get_Pts_col():
        tags = get_outer_tag()
        Pts = []
        for i in tags:
            points = i.find_elements(By.TAG_NAME, 'td')[10].text
            Pts.append(points)
        return Pts

    def get_Form_col():
        tags = get_outer_tag()
        Form = []
        for i in tags:
            form = i.find_elements(By.TAG_NAME,'td')[11].text.replace('\n','')
            Form.append(form)
        return Form

    # defining the function to get all the details of the column in dictonaries

      
    def get_data(url):
      dictonary={'position_column':[],'Team': [],'Pld':[],'Won': [],'Lost':[],'Tied':[],
                 'No_result': [],'Net_RR': [],'For': [],'Against': [],'Points':[],'Form':[],'Year':[] }
      for i in url:
          driver.get(i)
          dictonary['position_column'].extend(get_position_col())
          dictonary['Team'].extend(get_Team_col())
          dictonary['Pld'].extend(get_Pld_col())
          dictonary['Won'].extend( get_Won_col())
          dictonary['Lost'].extend(get_Lost_col())
          dictonary['Tied'].extend(get_Tied_col())
          dictonary['No_result'].extend( get_No_Result_col())
          dictonary['Net_RR'].extend(get_Net_RR_col())
          dictonary['For'].extend(get_For_col())
          dictonary['Against'].extend(get_Against_col())
          dictonary['Points'].extend(get_Pts_col())
          dictonary['Form'].extend(get_Form_col())
          #dictonary['Year'].extend(get_year_col())
  
      return dictonary

    # function calling

    # store the resulting out put in a variable
    dictonary_data = get_data(url)

    # dataframe to get data of year 2022-points tabel in tablur form
    df = pd.DataFrame(dictonary_data)
    df.to_csv('IPL T20 points Tabel', index=None)
    print(df)
