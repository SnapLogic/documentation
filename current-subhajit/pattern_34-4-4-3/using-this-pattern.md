# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**How to Configure the Pipeline**

when a new file is uploaded to Amazon S3, it creates an SQS event. SnapLogic consumes this event and retrieves the S3 file, inserts the records to Redshift, and confirms the SQS event.