import requests
from unittest import TestCase
import re
import pytest
import time

class FestivalsAPI():
    def __init__(self):
        self.BASE_URL="https://eacp.energyaustralia.com.au/codingtest/api/v1/festivals"
    def getResponse(self,sleepTime):
        time.sleep(sleepTime)
        response=requests.request('GET',self.BASE_URL)
        return response

class TestCases(TestCase):
    response=FestivalsAPI().getResponse(3)
    ststus_code=response.status_code
    response=response.json()
    responseKeys=['name','bands']
    bandKeys=['name','recordLabel']

    def checkResponseStructure():
        response=TestCases.response
        for festivals in response:
            keys=list(festivals.keys())
            if(len(keys)!=len(TestCases.responseKeys)):
                return False
            else:
                for key in keys:
                    if(key not in TestCases.responseKeys):
                        return False
                bands=festivals['bands']
                for band in bands:
                    key_bands=list(band.keys())
                    if(len(key_bands)!=len(TestCases.bandKeys)):
                        return False
                    else:
                        for key in key_bands:
                            if(key not in TestCases.bandKeys):
                                return False
        return True
    
    @pytest.mark.run('first')
    def test_checkResponseStructure(self):
        self.assertTrue(TestCases.checkResponseStructure())

    def checkResponseAttributesAreSring():
        response=TestCases.response
        pattern=r'^([\s\d]+)$'
        for festivals in response:
            if(re.match(pattern,festivals['name']) is not None):
                return False
            for band in festivals['bands']:
                if(re.match(pattern,band['name']) is not None):
                    return False
        return True
    @pytest.mark.run('second')
    def test_checkResponseAttributesAreString(self):
        self.assertTrue(TestCases.checkResponseAttributesAreSring())

    @pytest.mark.run('last')
    def test_Throttle(self):
        try:
            for i in range(0,10):
                FestivalsAPI().getResponse(0)
            self.assertTrue(False)
        except(Exception):
            self.assertTrue(True)


                

