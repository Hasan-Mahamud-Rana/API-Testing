# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 17:54:48 2021

@author: Hasan Mahamud Rana
"""
# Basic setup
import requests

baseURL = 'https://disease.sh/v3/covid-19/'

def endpoints(param):
    return baseURL + param

def response(url):
    return requests.get(url)

def responseText(param):
    url = endpoints(param)
    return response(url)

# content of test_Covid19.py
class TestClass:
    def test_GetGlobalCOVID19__Totals(self):
        # 1. COVID-19: Worldometers / Test Get global COVID-19 totals
        res = responseText('all')
        assert res.status_code == 200

    def test_GetCOVID19_TotalsForAllUSStates__California(self):
        # 2. Get COVID-19 totals for US State California
        res = responseText('states')
        res_body = res.json()
        assert res_body[0]['state'] == 'California'

    def test_GetCOVID19_TotalsForAllUSCounties__HasValue(self):
        # 3. COVID-19: JHUCSSE / Get COVID-19 totals for all US counties
        res = responseText('jhucsse/counties')
        res_body = res.json()
        assert len(res_body) > 1

    def test_GetCOVID19_TimeSeriesDataForAllCountries__Canada(self):
        # 4. COVID-19: JHUCSSE / Get COVID-19 time series data for all countries and their provinces
        res = responseText('historical/Canada')
        res_body = res.json()
        assert res_body['country'] == 'Canada'

    def test_GetCOVID19_NYTAllStates__Alabama(self):
        # 5. COVID-19: JHUCSSE / Get COVID-19 time series data for all countries and their provinces
        res = responseText('nyt/states/Alabama')
        res_body = res.json()
        assert res_body[0]['state'] == 'Alabama'

    def test_GetCOVID19_USNationWideData__NoDeath(self):
        # 6. COVID-19: NYT / US Nationwide Data         
        res = responseText('nyt/usa')
        res_body = res.json()
        NoDeath = 0
        for item in res_body:
            if item['deaths'] == 0:
                NoDeath += 1
        assert NoDeath > 0

    def test_GetCOVID19_AppleAllCountries__Argentina(self):
        # 7. COVID-19: Apple / All countries
        res = responseText('apple/countries/Argentina')
        res_body = res.json()
        assert res_body['country'] == 'Argentina'
       
    def test_GetCOVID19_AppleAllCountries__RegionInsideCountry(self):
        # 8. COVID-19: Apple / Region inside country
        res = responseText('apple/countries/Canada')
        res_body = res.json()
        assert res_body['country'] == 'Canada'   

    def test_GetGovernment(self):
        # 9. COVID-19: Government
        res = responseText('gov')
        res_body = res.json()
        assert len(res_body) > 0

    def test_GetVaccine_TotalCandidates(self):
        # 10. COVID-19: Vaccine
        res = responseText('vaccine')
        res_body = res.json() 
        assert int(res_body['totalCandidates']) > 0


    def test_GetCOVID19_TotalsCasesFor__NorthAmerica(self):
        # 11. COVID-19: Worldometers / Get COVID-19 totals for North America
        res = responseText('continents/North America')
        res_body = res.json() 
        assert res_body['cases'] > 1000    

    def test_GetCOVID19_TodayDeaths_Canada(self):
        # 12. Get COVID-19 todays death for Canada
        res = responseText('countries/Canada')
        res_body = res.json()
        assert res_body['todayDeaths'] >= 0

    def test_GetCOVID19_TotalsForUSCounties__alaska(self):
        # 13. COVID-19: JHUCSSE / Get COVID-19  data for all counties in a specified US state
        res = responseText('historical/usacounties/alaska')
        res_body = res.json()
        assert res_body[0]['province'] == 'alaska'

    def test_GetTherapeutics_TrialData(self):
        # 14. Get therapeutics trial data from RAPS
        res = responseText('therapeutics')
        res_body = res.json()
        assert int(res_body['totalCandidates']) > 0

    def test_GetNYTCounties__Autauga(self):
        # 15. Get NYT data for Autauga
        res = responseText('nyt/counties/Autauga')
        res_body = res.json()
        assert res_body[0]['county'] == 'Autauga'

    def test_GetGovernment__NewZealand(self):
        # 16. COVID-19: Government
        res = responseText('gov/New Zealand')
        res_body = res.json()
        assert len(res_body) > 0

    def test_GetVaccine_Countries__Albania(self):
        # 17. COVID-19: Vaccine for coutries country 
        res = responseText('vaccine/coverage/countries/Albania')
        res_body = res.json() 
        assert res_body['country'] == 'Albania'

    def test_GetVaccine_States__Delaware(self):
        # 18. COVID-19: Vaccine for coutries country 
        res = responseText('vaccine/coverage/states/Delaware')
        res_body = res.json() 
        assert res_body['state'] == 'Delaware'

    def test_GetInfluenza_USPHL(self):
        # 19. Get Influenza report data for the 2019 and 2020 outbreaks from the US Center for Disease Control, reported by US public health labs
        res = response('https://disease.sh/v3/influenza/cdc/USPHL')
        res_body = res.json() 
        assert len(res_body['data']) > 0

    def test_GetInfluenza_CDC(self):
        # 20. Get Influenza-like-illness data for the 2019 and 2020 outbreaks from the US Center for Disease Control
        res = responseText('influenza/cdc/ILINet')
        assert res.status_code == 200