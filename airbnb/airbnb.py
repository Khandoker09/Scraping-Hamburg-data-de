
import undetected_chromedriver as uc
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime
from lxml import etree
import pandas as pd
from tqdm import tqdm
driver = uc.Chrome()

def airbnb():
    try:

       airbnb1='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MCwiaXRlbXNfb2Zmc2V0IjowLCJ2ZXJzaW9uIjoxfQ%3D%3D'
       airbnb2='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoxOCwidmVyc2lvbiI6MX0%3D'
       airbnb3='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjozNiwidmVyc2lvbiI6MX0%3D'
       airbnb4='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0Ijo1NCwidmVyc2lvbiI6MX0%3D'
       airbnb5='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0Ijo3MiwidmVyc2lvbiI6MX0%3D'
       airbnb6='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0Ijo5MCwidmVyc2lvbiI6MX0%3D'
       airbnb7='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoxMDgsInZlcnNpb24iOjF9'
       airbnb8='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoxMjYsInZlcnNpb24iOjF9'
       airbnb9='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoxNDQsInZlcnNpb24iOjF9'
       airbnb10='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoxNjIsInZlcnNpb24iOjF9'
       airbnb11='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoxODAsInZlcnNpb24iOjF9'
       airbnb12='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoxOTgsInZlcnNpb24iOjF9'
       airbnb13='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoyMTYsInZlcnNpb24iOjF9'
       airbnb14='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoyMzQsInZlcnNpb24iOjF9'
       airbnb15='https://www.airbnb.de/s/Hamburg/homes?tab_id=home_tab&refinement_paths%5B%5D=%2Fhomes&flexible_trip_lengths%5B%5D=one_week&monthly_start_date=2023-08-01&monthly_length=3&price_filter_input_type=0&price_filter_num_nights=5&channel=EXPLORE&date_picker_type=calendar&source=structured_search_input_header&search_type=filter_change&query=Hamburg&place_id=ChIJuRMYfoNhsUcRoDrWe_I9JgQ&federated_search_session_id=d765c168-f0b2-4b0d-ad5e-a8c7a10db871&pagination_search=true&cursor=eyJzZWN0aW9uX29mZnNldCI6MywiaXRlbXNfb2Zmc2V0IjoyNTIsInZlcnNpb24iOjF9'

       driver.get(airbnb15)
       time.sleep(20)
       landowner_name1 =[]
       rating1=[]
       property_type1=[]
       price1=[]
       property_name1=[]

       landowner_name = driver.find_elements(By.XPATH,"//span[@class='t6mzqp7 dir dir-ltr']")
       for item in landowner_name:
              landowner_name1.append(item.text)
       ratings = driver.find_elements(By.XPATH,"//span[@class='r1dxllyb dir dir-ltr']")
       for rating in ratings:
              rating1.append(rating.text)

       property_name=driver.find_elements(By.XPATH,"//div[@class='t1jojoys dir dir-ltr']")
       for pn in property_name:
              property_name1.append(pn.text)

       price = driver.find_elements(By.XPATH,"//div[@class='_1jo4hgw']")
       for prices in price:
              price1.append(prices.text)


       data={'Property Name':property_name1,'Landowner Name': landowner_name1,'Price':price1, 'Avarate Rating':rating1}#, 'Location': location3, 'Companyname':company4}
       df = pd.DataFrame.from_dict(data, orient='index')
       df = df.transpose()
       # # Create a DataFrame from the extracted data
       # print(df)
       current_date = datetime.datetime.now()
       filename = str('Airbnbn_Hamburg_page_15')+str('_')+str(current_date.day)+str('_')+str(current_date.month)+str('_')+str(current_date.year)
       pd.DataFrame(df).to_excel(str(filename + '.xlsx'),index=False)

    except Exception as e:
        
        print(e)

if __name__ == "__main__":
         airbnb()

