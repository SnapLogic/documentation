# Using this Pattern

**Steps**

1. Click **Use Pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the pattern.
3. Click the pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

If the Pipeline runs successfully, you can view the output. For more information, read this article: [My First Pipeline](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/1438412).

**How to Configure the Pipeline**

Example HDFS writer configuration:

![](https://aws1.discourse-cdn.com/business5/uploads/snaplogic2/optimized/2X/8/85d5e6abd9f9ee0d65edc1bc37ebcddb0bf3ef80\_2\_690x324.png)

The URI to access the file on WASB has the following format (where “field-storage-account-container” is the name of the container): wasb:///field-storage-account-container/data/demo/raw/
