# Using this Pattern

**Steps**

1. Click **Use Pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

If the Pipeline runs successfully, you can view the output. For more information, read this article: [My First Pipeline](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/1438412).

**How to Configure the Pipeline**

The following Pipeline failure details are included in the email:

1. CustomerName – Name of the Customer for whom we are generating the report.
2. CustomerOrg – Name of the Org where we are getting the Pipeline execution information.
3. PipelineMonitoringAPI – API to fetch Pipeline execution information.
4. To – The receiver list in the email.
5. Authorization – Account to access the Pipeline execution information.
