from Class_Demo import *  # importing everything form demo python file
from Class_Crime import *  # importing everything form crime python file
from Class_Schools import *  # importing everything form schools python file
from zillow_API import *  # importing everything form CMA python file
from Class_Builders_tool import *  # importing everything from builders class file

from Run_file_addr_data import *
from Run_file_builders_data import *

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

# metropolitan = 'Clermont'
metropolitan = 'Tampa'
state = 'Florida'

# Builders class run
state_to_short_dict = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona':'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'NewHampshire': 'NH',
    'NewJersey': 'NJ',
    'NewMexico': 'NM',
    'NewYork': 'NY',
    'NorthCarolina': 'NC',
    'NorthDakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'RhodeIsland': 'RI',
    'SouthCarolina': 'SC',
    'SouthDakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY'
}
builders = Builders(metropolitan, state_to_short_dict[state], 'Builders.xlsx')
builders.lennar_filter_and_toolbar_info_copy()
builders.community_and_homes_all_data_to_xls_and_SQL()
builders.closeBrowser()
generated_Id_list = builders.return_Generated_Id_list()
address_list_for_automation = builders.return_community_address_list()
print('original address list {}'.format(address_list_for_automation))
print('original generated_Id_list {}'.format(generated_Id_list))


# Automation on all addresses
for i in range(len(address_list_for_automation)):
    # looking for details about the address in google
    driver = webdriver.Chrome("/Users/alexdezho/Downloads/chromedriver")
    driver.get("https://www.google.com/maps/")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="searchboxinput"]')))
    driver.find_element_by_xpath('//*[@id="searchboxinput"]').send_keys(address_list_for_automation[i])
    driver.find_element_by_xpath('//*[@id="searchbox-searchbutton"]').click()
    time.sleep(3)
    # locating the parameters for the Automation
    street = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/div[1]/h1/span[1]').text
    city = driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[2]/div[1]/div[1]/h2[1]/span').text
    city = city.split(",")
    city = city[0]
    driver.close()
    print('street - {}'.format(street))
    print('city - {}'.format(city))
    print('short state - {}'.format(state_to_short_dict[state]))
    print('state - {}'.format(state))
    print('random id - {}'.format(generated_Id_list[i]))

    address_data_automate_tool(street, city, short_state, state, generated_Id_list[i])
