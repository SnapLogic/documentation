# Overview

Use this Pipeline Pattern to migrate customer data stored in a transactional Azure SQL table into Salesforce for Sales prospecting. The Pipeline connects to an Azure SQL database, query data, and then upserts the results to an object in Salesforce. Both error and successful records are written to a log file within SnapLogic.
