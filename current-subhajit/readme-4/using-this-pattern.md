# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**Important Information about this Pattern**

* When retrieving the data from John Galt Atlas, the Pipeline uses the export custom view in JSON API.
* After retrieving the data from John Galt Atlas, the integration upserts the forecast data to the Opportunity Line Items in Salesforce using the child Pipeline.&#x20;
* If the data is not present, the integration creates new Opportunity Line Items in Salesforce using another child Pipeline.&#x20;
