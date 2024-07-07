#Multi page info web Scraping
import requests
from bs4 import BeautifulSoup
mobile_name_list=[]
mobile_price_list=[]
mobile_feature_list=[]
page_number=int(input("how many page information you want: "))
for page in range(1, page_number+1):
        url=f"https://www.flipkart.com/search?q=mobile&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&as-pos=1&as-type=HISTORY&page={page}"
        check_status=requests.get(url)
        print("Successful established a connection status code is",check_status.status_code)
        html_data=BeautifulSoup(check_status.content,'html.parser')

        mobile_names=html_data.find_all('div',class_='KzDlHZ')
        for mobile in mobile_names:
            mobile_name_list.append(mobile.text)
        print(mobile_name_list)
        mobile_prices=html_data.find_all('div',class_='Nx9bqj _4b5DiR')
        for price in mobile_prices:
            mobile_price_list.append(price.text)
        print(mobile_price_list)
        mobile_features=html_data.find_all('div',class_="_6NESgJ")
        for i in mobile_features:
            mobile_feature_list.append(i.text)
        print(mobile_feature_list)
        d1={'Mobile Name':mobile_name_list,
        'Mobile Price':mobile_price_list,
        'Mobile Features':mobile_feature_list}
print(d1)
import pandas as pd
mobile_data=pd.DataFrame(d1)
mobile_data.to_excel('Mobile Info.xlsx')
