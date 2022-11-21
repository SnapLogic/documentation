# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**Important Information about this Pattern Pipeline:**

* The Microsoft Dynamics 365 Finance and Operations application OData REST API is used for the insert operation.&#x20;
* The Salesforce Subscriber Snap is used to capture account creations using the platform event in Salesforce.
* A customer account identifier value is generated in SnapLogic and sent to Microsoft Dynamics 365 Finance and Operations. After it is successfully inserted into Dynamics 365 Finance and Operations, it is sent back to Salesforce. This will synchronize the record between Dynamics F\&O and Salesforce.
* To prevent duplicates, you can modify the Pipeline to either:&#x20;
  * Filter out Salesforce records that have the `ERP_Customer_Id__c` custom field populated because if that field is populated, it means that the record was already sent to Dynamics 365 Finance and Operations.&#x20;
  * Use a Router Snap to update the record in Microsoft Dynamics 365 Finance and Operations if the `ERP_Customer_Id__c` custom field is already populated in Salesforce. In that case, you can use the Microsoft Dynamics 365 Finance and Operations Update Custom Snap.
