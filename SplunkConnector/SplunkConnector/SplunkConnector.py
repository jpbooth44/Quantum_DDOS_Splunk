#JP Booth
#Last edited 11/28/23 10:37PM EST


from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import urllib
import httplib2
import splunklib.results
from xml.dom import minidom
import time
import re
from time import localtime,strftime
from xml.dom import minidom
import csv
import splunklib.client as client
import getpass

HOST = "10.11.17.220"
PORT = "8089" #Splunk Management Port
#PORT = 8000 #Don't use this port
USERNAME = input("Enter username: ")
PASSWORD = getpass.getpass()

# Create a Service instance and log in
service = client.connect(
    host=HOST,
    port=PORT,
    #scheme = "http", #HTTPS for port 8089 (default)!!!
    username=USERNAME,
    password=PASSWORD)

 
QUERY = "| inputlookup Honeypot_Data.csv"
#Creates a job to lookup the Honeypot_Data.csv file in Splunk and return it as a csv file
job = service.jobs.create(QUERY, **{"exec_mode": "blocking"})
options = {"count": 0, "output_mode": "csv"}
resultsList = job.results(**options)

#user chooses an output destination for the csv file and the data sheet is created there as "Honeypot_Data.csv"
dir = input("Choose output destination: ")
f = open(dir + "/Honeypot_Data.csv", 'w')
f.write(resultsList.read().decode())
f.close()





############################################################################
#                              OLD STUFF                                   #
############################################################################
#               Old versions of the code, here for reference               #
############################################################################

# Get the collection of search jobs
#jobs = service.jobs

# Create a search job
#job = jobs.create(query)

#print( "There are", len(jobs), "jobs available to the current user")
#print("\nSearch IDs:\n   " + "\n   ".join([job.sid for job in jobs]))

# Print installed apps to the console to verify login
#for app in service.indexes:
#    print(app.name)
#    if app.name == 'Index_name':
#        print(app.name)
#        print("Index Found")
#    else:
#        print("Index Not Found")

#baseurl = "https://10.11.17.220:8089"
#myhttp = httplib2.Http(disable_ssl_certificate_validation=True)


#STEP 1: get a session key
#serverContent = myhttp.request(baseurl + '/services/auth/login',
 #   'POST', headers={}, body=urllib.parse.urlencode({'username':USERNAME, 'password':PASSWORD}))[1]

#sessionKey = minidom.parseString(serverContent).getElementsByTagName('sessionKey')[0].childNodes[0].nodeValue


#STEP 2: create a search job
#sql for query
#searchQuery = '| inputlookup Honeypot_Data.csv'
#searchQuery = searchQuery.strip()

# If the query doesn't already start with the 'search' operator or another
# generating command (e.g. "| inputcsv"), then prepend "search " to it.
#if not (searchQuery.startswith('search') or searchQuery.startswith("|")):
#    searchQuery = 'search ' + searchQuery
    
#print(searchQuery)

#searchJob = myhttp.request(baseurl + '/services/search/jobs','POST',
#    headers={'Authorization': 'Splunk %s' % sessionKey},body=urllib.parse.urlencode({'search': searchQuery}))[1]
#sid = minidom.parseString(searchJob).getElementsByTagName('sid')[0].childNodes[0].nodeValue
#print ("====>sid:  %s  <====" % sid)


#STEP 3: Get the search status

#myhttp.add_credentials(USERNAME, PASSWORD)
#servicessearchstatusstr = '/services/search/jobs/%s/' % sid
#isnotdone = True
#while isnotdone:
#    searchstatus = myhttp.request(baseurl + servicessearchstatusstr, 'GET')[1]
#    decodedstatus = searchstatus.decode('utf-8')
#    isdonestatus = re.compile('isDone">(0|1)')
#    isdonestatus = isdonestatus.search(decodedstatus).groups()[0]
#    if (isdonestatus == '1'):
#        isnotdone = False
#print ("====>search status:  %s  <====" % isdonestatus)

#time.sleep(5)
#Step 4: Get the search results
#services_search_results_str = '/services/search/jobs/%s/results?output_mode=csv&count=0' % sid
#searchResults = myhttp.request(baseurl + services_search_results_str, 'GET')[1]
#print ("====>search result:  [%s]  <====" % searchResults)

#resultsList = searchJob.results(**{"output_mode": "csv"})

#Step 5: ??
#reader = splunklib.results.ResultsReader(searchresults)
#for item in reader:
#    print(item)
#print ("Results are a preview: %s" % reader.is_preview)

# Run the search.
# Again, disable SSL cert validation.
#print(httplib2.Http(disable_ssl_certificate_validation=True).request("https://" + HOST + ":" + PORT + '/services/search/jobs','POST',
  #  headers={'Authorization': 'Splunk %s' % sessionKey},body=urllib.parse.urlencode({'search': searchQuery}))[1])