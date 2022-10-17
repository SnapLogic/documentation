# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**How to Configure the Pipeline**

This Pattern retrieves the files, extracts the metadata, and loads them as a single sequence file that contains zipped source files and file metadata. The files can then be written to any target location using the File Writer Snap including S3, WASB, ADL, HDFS, SFTP, and other protocols.

You can adjust which endpoint to upload the files and their metadata into by replacing the HDFS Writer Snap with the preferred application and configuring it using the File Writer Snap.&#x20;

