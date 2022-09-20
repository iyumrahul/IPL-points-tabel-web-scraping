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

    # get inner tag data
    def get_data():
        tags = Tag
        Place,Team,Pld,Won,Lost,Tied,No_Result,Net_RR,_For,Against,Pts,Form=[],[],[],[],[],[],[],[],[],[],[],[]
        for i in tags:
            place = i.find_elements(By.TAG_NAME, 'td')[0].text
            Place.append(place)

            team = i.find_elements(By.TAG_NAME, 'td')[1].text
            Team.append(team)

            pld = i.find_elements(By.TAG_NAME, 'td')[2].text
            Pld.append(pld)

            won = i.find_elements(By.TAG_NAME, 'td')[3].text
            Won.append(won)

            lost = i.find_elements(By.TAG_NAME, 'td')[4].text
            Lost.append(lost)

            tied = i.find_elements(By.TAG_NAME, 'td')[5].text
            Tied.append(tied)

            noResult = i.find_elements(By.TAG_NAME, 'td')[6].text
            No_Result.append(noResult)

            net_rr = i.find_elements(By.TAG_NAME, 'td')[7].text
            Net_RR.append(net_rr)

            _for = i.find_elements(By.TAG_NAME, 'td')[8].text
            _For.append(_for)

            against = i.find_elements(By.TAG_NAME, 'td')[9].text
            Against.append(against)

            points = i.find_elements(By.TAG_NAME, 'td')[10].text
            Pts.append(points)

            form = i.find_elements(By.TAG_NAME, 'td')[11].text.strip()
            x = list(form)
            Form.append(list(x))
        return {
            'PLACE': Place,
            'TEAM': Team,
            'PLAYED': Pld,
            'WON': Won,
            'LOST': Lost,
            'TIED': Tied,
            'N/R': No_Result,
            'NET_RUN_RATE': Net_RR,
            'FOR': _For,
            'AGAINST': Against,
            'POINTS': Pts,
            'FORM': Form
        }

    # function calling
    dictonary_data = get_data()

    df = pd.DataFrame(dictonary_data)
    df.to_csv('IPLT20 points Tabel', index=None)
    print(df)
