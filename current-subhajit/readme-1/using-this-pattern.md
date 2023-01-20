# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**Important Information about this Pattern**

* The Parent Pipeline reads the source and target schema and tables with a clause to filter the source data from the`oracle_to_redshift__c.expr` expression file.&#x20;

Note: Modify this expression file to correspond with the table and schemas as per your target database.

* The Pipeline obtains the primary key constraints for each target table in Redshift. It constructs an array of documents for up to 10 key columns to determine the unicity of the data while upserting them into Redshift.&#x20;
* Each document is then passed into the child Pipeline that reads the data from the source Oracle table and then upserts them into Redshift.
* A Router Snap is used between the Oracle read and Redshift upsert to achieve concurrency for large data volumes.
* The Pattern Pipeline can also be reused to operate with different source and target databases, such as SQL Server to Google BigQuery.
