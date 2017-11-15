#! /usr/bin/python
# -*- coding: UTF-8 -*-

#  Copyright 2017 Luiko Czub, TestLink-API-Python-client developers
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
# ------------------------------------------------------------------------

import os.path
import pytest
from testlink import TestlinkAPIClient, TestlinkAPIGeneric, TestLinkHelper

# example text file attachment = this python file
# why not using os.path.realpath(__file__)
# -> cause __file__ could be compiled python file *.pyc, if the test run is 
#    repeated without changing the test code
ATTACHMENT_EXAMPLE_TEXT= os.path.join(os.path.dirname(__file__), 
                                      os.path.basename(__file__))

#attachemantFile = open(ATTACHMENT_EXAMPLE_TEXT, 'r')

@pytest.fixture()
def attachmentFile():
    ''' open readonly attachment sample before test and close it afterwards '''
    aFile = open(ATTACHMENT_EXAMPLE_TEXT, 'r')
    yield aFile
    aFile.close()
    
    
@pytest.fixture(scope='session')
def api_generic_client():
    ''' Init TestlinkAPIGeneric Client with connection parameters defined in 
        environment variables
        TESTLINK_API_PYTHON_DEVKEY and TESTLINK_API_PYTHON_DEVKEY
    ''' 
    return TestLinkHelper().connect(TestlinkAPIGeneric)

@pytest.fixture(scope='session')
def api_general_client():
    ''' Init TestlinkAPIClient Client with connection parameters defined in 
        environment variables
        TESTLINK_API_PYTHON_DEVKEY and TESTLINK_API_PYTHON_DEVKEY
    ''' 
    return TestLinkHelper().connect(TestlinkAPIClient)

@pytest.fixture(scope='session', params=[TestlinkAPIGeneric, TestlinkAPIClient])
def api_client(request):
    ''' Init Testlink API Client class defined in fixtures parameter list with
        connection parameters defined in environment variables
        TESTLINK_API_PYTHON_DEVKEY and TESTLINK_API_PYTHON_DEVKEY
        
        Tests will be call for each Testlink API Client class, defined in 
        fixtures parameter list
    ''' 
    return TestLinkHelper().connect(request.param)

