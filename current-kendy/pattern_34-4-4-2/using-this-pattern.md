# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**Important Information about this Pattern**

This Pattern can be used as a child Pipeline through the Pipeline Execute Snap. If there are multiple records, make sure to configure the Reuse executions parameter in the Pipeline Execute Snap and pass $input\_date as a document, and make sure to remove the Map the input date and Mapper Snaps.
