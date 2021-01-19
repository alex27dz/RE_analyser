from Class_Demo import *  # importing everything form demo python file
from Class_Crime import *  # importing everything form crime python file
from Class_Schools import *  # importing everything form schools python file

import time
import pprint
import logging
import mysql.connector
import datetime  # datetime.datetime.now()

import openpyxl
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import json  # working with json dicts
import yagmail  # importing all email file to use send function
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from openpyxl.styles import Alignment
import urllib.request

# street = '451 clear blue way'  # taken from community builder list
# city = 'mcdonough'  # taken from community builder list
# short_state = 'GA'  # taken from community builder list
# state = 'Georgia'  # input

#
# street = '1618 Lake Sims Parkway'  # taken from community builder list
# city = 'Ocoee'  # taken from community builder list
# short_state = 'FL'  # taken from community builder list
# state = 'Florida'  # input
# randomid = 'alex2'

def address_data_automate_tool(street, city, short_state, state, randomid):
    logging.basicConfig(filename='(NR)-Testlog.txt', level=logging.DEBUG, format='%(asctime)s: %(message)s')  # log file
    global_data_list_address_automate = []

    print('Demography run started')
    htl = HometownLocator(street, state, city, short_state, 'Address_data_full.xlsx')
    htl.google_Maps_Addr_Coord()
    htl.metropolitan_area_Look_Up_Tool()
    htl.metro_to_url()
    htl.params_to_dict_block(htl.HTML_to_dictionary(htl.return_block_url()))
    htl.params_to_dict_track(htl.HTML_to_dictionary(htl.return_track_url()))
    htl.params_to_dict_zip_code(htl.HTML_to_dictionary(htl.return_zip_code_url()))
    htl.params_to_dict_city(htl.HTML_to_dictionary(htl.return_city_url()))
    htl.params_to_dict_county(htl.HTML_to_dictionary(htl.return_county_url()))
    htl.params_to_dict_metro(htl.HTML_to_dictionary(htl.return_metro_url()))
    htl.printall()  # printing all dicts
    global_data_list_address_automate.append('Demography')  # adding all to general list
    global_data_list_address_automate.append(htl.return_dict_basic_info())
    global_data_list_address_automate.append(htl.return_dict_block())
    global_data_list_address_automate.append(htl.return_dict_track())
    global_data_list_address_automate.append(htl.return_dict_zip_code())
    global_data_list_address_automate.append(htl.return_dict_county())
    global_data_list_address_automate.append(htl.return_dict_city())
    global_data_list_address_automate.append(htl.return_dict_metro())
    htl.xls_new_sheet_for_search_create()  # copy all dictionaries to xls file
    htl.basic_Info_dict_to_xls()  # copy
    htl.all_dicts_to_xls()  # copy
    dict_block_SQL = htl.return_dict_block()
    dict_city_SQL = htl.return_dict_city()
    dict_metro_SQL = htl.return_dict_metro()
    county = htl.return_county_name()[:-7]
    zip_code = htl.return_zip_code_for_zillow_use()
    print('county name for schools run: {}'.format(county))
    htl.closeBrowser()
    print('Demography Run ended')

    print('Schools class started')

    school = Schools(street, state, city, short_state, 'Address_data_full.xlsx', county, zip_code)
    # getting all schools info and putting it into dictionaries
    school.homefacts_to_dict()
    school.greateschools_to_dict()
    school.schooldigger_to_dict()
    # return all dicts & add to general list
    global_data_list_address_automate.append('Schools')
    global_data_list_address_automate.append(school.return_dict_basic_info())
    global_data_list_address_automate.append(school.return_dict_greateshcools())
    global_data_list_address_automate.append(school.return_dict_schooldigger())
    global_data_list_address_automate.append(school.return_dict_homefacts())
    # copy all dictionaries to xls file
    # school.xls_new_sheet_for_search_create()
    school.all_dicts_to_xls()
    dict_schools_SQL = school.return_dict_schools_general()
    print('a')
    print(dict_schools_SQL)
    # school.closeBrowser()
    print('Schools Run ended')

    print('Crime class started')
    crime = Crime(street, state, city, short_state, 'Address_data_full.xlsx')
    # getting all the information and copy into dicts
    crime.onboardnavigator_to_dict()
    crime.city_data_to_dict()
    crime.home_facts_to_dict()
    crime.neighborhoodscout_to_dict()
    crime.bestplaces_to_dict()
    # crime.xls_new_sheet_create()
    crime.all_dicts_to_xls()
    crime.printall()
    # returning all dictionaries for general list
    global_data_list_address_automate.append('Crime')
    global_data_list_address_automate.append(crime.return_dict_basic_info())
    global_data_list_address_automate.append(crime.return_dict_onboardnavigator())
    global_data_list_address_automate.append(crime.return_dict_city_data())
    global_data_list_address_automate.append(crime.return_dict_home_facts())
    global_data_list_address_automate.append(crime.return_dict_neighborhoodscout())
    global_data_list_address_automate.append(crime.return_dict_bestplaces())
    dict_crime_SQL = crime.return_dict_crime_total()
    print('a')
    print(dict_crime_SQL)
    crime.closeBrowser()
    print('Crime Run ended')

    print('printing all dictionaries before copy to MySQL')
    print(dict_block_SQL)
    print(dict_city_SQL)
    print(dict_metro_SQL)
    print(dict_crime_SQL)
    print(dict_schools_SQL)

    addr = street + ' ' + city + ' ' + short_state

    # MySQL
    print('trying to copy to MySQL')
    try:
        print('Connecting to MySQL server')
        db = mysql.connector.connect(
            host='107.180.21.18',
            user='grow097365',
            passwd='Jknm678##Tg',
            database='equity_property'
        )
        mycursor = db.cursor()
        print(db)  # checking our connection to DB
        sql = "INSERT INTO Full_Information (id_generated, time, address, Total_Population_block, Population_Growth_2010_2019_block, Population_Growth_2019_2024_block, Median_Household_Income_block, Average_Household_Income_block, Owner_Occupied_HU_block, Renter_Occupied_HU_block, Vacant_Housing_Units_block, Median_Home_Value_block, Total_Population_city, Population_Growth_2010_2019_city, " \
              "Population_Growth_2019_2024_city, Median_Household_Income_city, Average_Household_Income_city, Owner_Occupied_HU_city, Renter_Occupied_HU_city, Vacant_Housing_Units_city, Median_Home_Value_city, Total_Population_metro, Population_Growth_2010_2019_metro, Population_Growth_2019_2024_metro, Median_Household_Income_metro, Average_Household_Income_metro, Owner_Occupied_HU_metro, " \
              "Renter_Occupied_HU_metro, Vacant_Housing_Units_metro, Median_Home_Value_metro, Crime_Index_city, US_avarage, Pic_of_graph, Total_crime_index, Violent_crime_index, Property_crime_index, Violent_crime_US_average, Property_crime_US_average, Photos_and_Maps_of_the_city, school_elementary_name, school_elementary_link, school_middle_name, school_middle_link, school_high_name, " \
              "school_high_link, school_HF_elementary_name, school_HF_elementary_link, school_HF_middle_name, school_HF_middle_link, school_HF_high_name, school_HF_high_link) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) "
        val = (randomid,
               datetime.datetime.now(),
               addr,
               dict_block_SQL['Total_Population'],
               dict_block_SQL['Population_Growth_2010_2019'],
               dict_block_SQL['Population_Growth_2019_2024'],
               dict_block_SQL['Median_Household_Income'],
               dict_block_SQL['Average_Household_Income'],
               dict_block_SQL['Owner_Occupied_HU'],
               dict_block_SQL['Renter_Occupied_HU'],
               dict_block_SQL['Vacant_Housing_Units'],
               dict_block_SQL['Median_Home_Value'],
               dict_city_SQL['Total_Population'],
               dict_city_SQL['Population_Growth_2010_2019'],
               dict_city_SQL['Population_Growth_2019_2024'],
               dict_city_SQL['Median_Household_Income'],
               dict_city_SQL['Average_Household_Income'],
               dict_city_SQL['Owner_Occupied_HU'],
               dict_city_SQL['Renter_Occupied_HU'],
               dict_city_SQL['Vacant_Housing_Units'],
               dict_city_SQL['Median_Home_Value'],
               dict_metro_SQL['Total_Population'],
               dict_metro_SQL['Population_Growth_2010_2019'],
               dict_metro_SQL['Population_Growth_2019_2024'],
               dict_metro_SQL['Median_Household_Income'],
               dict_metro_SQL['Average_Household_Income'],
               dict_metro_SQL['Owner_Occupied_HU'],
               dict_metro_SQL['Renter_Occupied_HU'],
               dict_metro_SQL['Vacant_Housing_Units'],
               dict_metro_SQL['Median_Home_Value'],
               dict_crime_SQL['Crime Index city'],
               dict_crime_SQL['US avarage'],
               dict_crime_SQL['Pic of graph'],
               dict_crime_SQL['Overall Score'],
               dict_crime_SQL['Overall score big num'],
               dict_crime_SQL['Score small procents'],
               dict_crime_SQL['Violent crime & US average'],
               dict_crime_SQL['Property crime & US average'],
               dict_crime_SQL['Photos and Maps of the city'],
               dict_schools_SQL['school - elementary name'],
               dict_schools_SQL['school - elementary link'],
               dict_schools_SQL['school - middle name'],
               dict_schools_SQL['school - middle link'],
               dict_schools_SQL['school - high name'],
               dict_schools_SQL['school - high link'],
               dict_schools_SQL['school - HF elementary name'],
               dict_schools_SQL['school - HF elementary link'],
               dict_schools_SQL['school - HF middle name'],
               dict_schools_SQL['school - HF middle link'],
               dict_schools_SQL['school - HF high name'],
               dict_schools_SQL['school - HF high link'])
        mycursor.execute(sql, val)
        db.commit()
        print('address inserted')
    except:
        print('failed to connect to sql')


# address_data_automate_tool(street, city, short_state, state, randomid)






