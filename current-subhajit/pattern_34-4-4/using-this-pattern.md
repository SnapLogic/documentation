# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**How to Configure the Pipeline**

1. Once configured with a Salesforce account, use the Salesforce Read Snap to query the record to which the file will be attached.
2. Extract the Salesforce record Id and OwnerId from the Salesforce output.
3. Use the Binary to Document Snap to convert the binary file stream to a  document file for mapping.
4. Merge the ID with the File using the **Merge** option in the Join Snap.
5. Map the Salesforce Attachment structure.
6. Create the Salesforce attachment record using the Salesforce Create Snap.

