###############################################################################
# Copyright (c) 1984,2015 MarketShare Data Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
###############################################################################
# File: NessusRestTest.py
# Function: To test Nessus Rest API operation
###############################################################################
# Steps
#   Establish a connection to Nessus
#   Request a list of plugin "Families"
#   Close the connection
###############################################################################

import json, requests

url = 'https://localhost:8834/session'

params = dict(
    username='test',
    password='password'
)
print (params)
print ("\nOpening Nessus session")
resp = requests.post(url=url, params=params, verify=False) # Certificate verify failed!
data = json.loads(resp.text)
print (data) # it works!  can also print (resp.content)
params = data
print (params)

print ("\nCalling Nessus API to list families")
url = 'https://localhost:8834/plugins/families'
resp = requests.get(url=url, params=params, verify=False) # Certificate verify failed!
print ("response.text:")
print (resp.text)
data = json.loads(resp.text)
print (data)

print ("\nClosing Nessus session")
resp = requests.delete(url=url, params=params, verify=False) # Certificate verify failed!
data = json.loads(resp.text)
print (data)
print ("End Program")
