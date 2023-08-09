import requests
import pandas as pd
import time
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

def run_zillow_etl():
    #Base URL of API
    url = "https://zillow56.p.rapidapi.com/search"
    # Parameters to pass 
    querystring = {"location":"Arlington, TX"}
    #Header Data Of API
    headers = {
	    "X-RapidAPI-Key": "YOUR KEY HERE",
	    "X-RapidAPI-Host": "YOUR HOST HERE"
    }       

    
    result_json=[]
    #Calling API to get Number of Pages of data the response has
    response = requests.get(url, headers=headers, params=querystring)
    #Getting Number of Pages
    pages=response.json()['totalPages']

    #Sleep Interval declaration: Set it to 2 Seconds
    SLEEP_INTERVAL=2

    #Calling Data to get page wise
    for page in range(1,pages):
        querystring["page"]=str(page)
        response_page = requests.get(url, headers=headers, params=querystring)
        #catching Data to resultant list
        result_json.extend(response_page.json()['results'])
        #Since I'm using API with Basic subscription only one hit is allowed per second
        # So, I'm making sleep for 2 seconds so that API gets hit every 2 seconds for next page
        time.sleep(SLEEP_INTERVAL)

    #Creating Data Frame of Properties from JSON response
    df=pd.DataFrame(result_json)
    #saving Data Frame to CSV
    zillow_csv=df.to_csv(index=False)

    #Creating client of Azure Blob Service
    blob_service_client = BlobServiceClient.from_connection_string('YOUR CONNECTION STRING HERE')
    #Accessing Blob container
    container_client = blob_service_client.get_container_client('YOUR CONTAINER NAME HERE')
    #getting csv file from blob, creates new if not exists
    blob_client = container_client.get_blob_client('zillow.csv')
    #uploading data 
    blob_client.upload_blob(zillow_csv,overwrite=True) 

#function call
run_zillow_etl()