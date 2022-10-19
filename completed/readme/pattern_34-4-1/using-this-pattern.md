# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

If the Pipeline runs successfully, you can view the output. For more information, read this article: [My First Pipeline](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/1438412).

**How to Configure the Pipeline**

* The Pipeline takes a closed Salesforce opportunity ID as the pipeline parameter.
* The Pipeline assumes the Salesforce product and NetSuite item has been synchronized, and the NetSuite item internal ID is stored in each Salesforce product.
* The Pipeline creates a new NetSuite customer if the Salesforce Opportunity Account is not already created.
* The Pipeline creates the NetSuite Sales Order based on the approved Opportunity Quote.
* Each Salesforce Quote Line Item will create a NetSuite Sales Order Line Item.
