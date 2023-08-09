# Zillow_ ETL_ Pipeline


This project is all about simplifying how we get property details from Zillow of a specific location. We've built a pipeline using Python that talks to Zillow's API to fetch the data. To keep things organized and automated, we're using Airflow, a tool that helps us schedule tasks. We've set it up to pull data every month.

To make sure everything runs smoothly, we've put Airflow on an Azure Virtual Machine. This helps us manage the workload efficiently, especially as we get more data. And we're not stopping there - we're using Azure Blob storage to neatly store the property details in CSV files.

We're using a library called Pandas to clean up the data and put it in a nice format for the CSV files. If you're curious about the nitty-gritty details, take a look at the code. It's an exciting project that takes the hassle out of gathering property info and shows how these tools can work together for a smoother ETL (Extract, Transform, Load) process.
