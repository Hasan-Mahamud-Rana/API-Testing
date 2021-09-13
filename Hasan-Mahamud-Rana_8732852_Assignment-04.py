# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:54:48 2021

@author: Hasan Mahamud Rana
"""

#-----------------------------------------------------------------------------#
# 2. Create and run Python scripts
#-----------------------------------------------------------------------------#

"""
Sample code from Postman

import requests

url = "https://disease.sh/v3/covid-19/all"
payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)
print(response.text)

"""
# Basic setup
import requests
payload = {}
headers = {}
baseURL = 'https://disease.sh/v3/covid-19/'

def endpoints(param):
    return baseURL + param

def response(url):
    return requests.get(url, headers=headers, data=payload)

def responseText(param):
    url = endpoints(param)
    res = response(url)
    return res.text


# 1. COVID-19: Worldometers / Get global COVID-19 totals
GetGlobalCOVID19Totals = responseText('all')
print(GetGlobalCOVID19Totals)


# 2. COVID-19: Worldometers / Get COVID-19 totals for all US States
GetCOVID19TotalsForAllUSStates = responseText('states')
print(GetCOVID19TotalsForAllUSStates)


# 3. COVID-19: JHUCSSE / Get COVID-19 totals for all US counties
GetCOVID19TotalsForAllUSCounties = responseText('jhucsse/counties')
print(GetCOVID19TotalsForAllUSCounties)


# 4. COVID-19: JHUCSSE / Get COVID-19 time series data for all countries and their provinces
GetCOVID19TimeSeriesDataForAllCountries = responseText('historical')
print(GetCOVID19TimeSeriesDataForAllCountries)


# 5. COVID-19: NYT / All states
GetCOVID19NYTAllStates = responseText('nyt/states')
print(GetCOVID19NYTAllStates)


# 6. COVID-19: NYT / US Nationwide Data
GetCOVID19USNationWideData = responseText('nyt/usa')
print(GetCOVID19USNationWideData)


# 7. COVID-19: Apple / All countries
GetCOVID19AppleAllCountries = responseText('apple/countries')
print(GetCOVID19AppleAllCountries)


# 8. COVID-19: Apple / Single country by name
GetCOVID19AppleAllCountriesCanada = responseText('apple/countries/Canada')
print(GetCOVID19AppleAllCountriesCanada)


# 9. COVID-19: Government
GetGovernment = responseText('gov') 
print(GetGovernment)


# 10. COVID-19: Vaccine
GetVaccine = responseText('vaccine') 
print(GetVaccine)
