year_list = [2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019,2020, 2021, 2022]

def get_year_col(year):
        Year=[]
        for i in year:
          if i==2022 or i==2011:
            for j in range(10):
              Year.append(i)
          elif i==2012 or i==2013:
            for j in range(9):
              Year.append(i)  
          else:
            for j in range(8):
              Year.append(i)
            
        return Year
    
Years=get_year_col(year_list)
print(Years)
print(len(Years))

