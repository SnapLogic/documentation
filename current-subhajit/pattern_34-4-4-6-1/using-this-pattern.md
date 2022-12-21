# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**Important Information about these Patterns**

* As the Opportunity Line Item Schedule (OLIS) is updated in Salesforce, the SnapLogic Pipeline consumes the platform event and sends that information to Atlas.&#x20;
* The Pipeline can be in an active state to constantly listen to the platform event.
* Atlas is updated in two ways:&#x20;
  * Via SQL Server to check if an opinion line record exists. If it does, then update the record, otherwise insert it.&#x20;
  * Via Atlas API.
