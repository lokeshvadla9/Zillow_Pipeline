# Zillow_Pipeline


This project revolves around simplifying the process of collecting property details from Zillow for a specific location using the Zillow API. The main tools used here are Python, Airflow, and Azure services.

Python is used to communicate with the Zillow API, fetching property data. Airflow, a scheduling tool, is used to automate this process on a monthly basis. The entire system is hosted on an Azure Virtual Machine, ensuring it runs reliably and efficiently.

The collected property data is cleaned using Pandas, a popular data manipulation library in Python. After cleaning, the data is organized and saved in a CSV format. Azure Blob storage is employed to store these CSV files securely in the cloud.

This project showcases how a simple combination of programming, automation, and cloud services can streamline the process of collecting, organizing, and storing property data from Zillow, making it easily accessible for future use.
