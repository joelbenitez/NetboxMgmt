#!/usr/bin/env python3

'''
This is just a test of the token API using Pynetbox
'''

import pynetbox
import requests
import urllib3
from pprint import pprint
from NetboxConfig import NETBOX_URL, NETBOX_TOKEN


#I am using a self-signed certificate cuz I am poor and this is a dev instance
#this portion gets rid of the warning messages
session = requests.Session()
session.verify = False

#likewise, Python yells at you when you don't use a self-signed cert 
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

nb = pynetbox.api(NETBOX_URL, token= NETBOX_TOKEN)

nb.http_session = session

regions = nb.dcim.regions.all()
for region in regions:
    #pprint(dict(region), indent = 4)
    print (region.id, region.slug)

