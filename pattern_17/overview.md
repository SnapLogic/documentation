# Overview

Use this Pipeline Pattern to connect to an Azure SQL database, query data, and then upsert the results to an object in Salesforce. Both error and successful records are written to a log file within SLDB. The Pipeline Pattern could be used to migrate customer data stored in a transactional Azure SQL table into Salesforce for Sales prospecting. Both Azure SQL and Salesforce accounts are required, and you must specify the necessary mappings in the Mapper Snap.
