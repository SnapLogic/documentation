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

![Alt text](https://global.discourse-cdn.com/business5/uploads/snaplogic2/optimized/1X/b8cbbd53ca30fa0b229fc8310457ea0f55e2d0b1_2_600x450.png)
2. Extract the Salesforce record Id and OwnerId from the Salesforce output.

![Alt text](https://global.discourse-cdn.com/business5/uploads/snaplogic2/optimized/1X/a246ad126be9e6f231eeeb232c0d3c3a3785fc86_2_600x350.png)
3. Use the Binary to Document Snap to convert the binary file stream to a  document file for mapping.

![Alt text](https://global.discourse-cdn.com/business5/uploads/snaplogic2/optimized/1X/aec40b49c88a935762f27ddb07323a52202c44c5_2_600x250.png)
4. Merge the ID with the File using the **Merge** option in the Join Snap.

![Alt text](https://global.discourse-cdn.com/business5/uploads/snaplogic2/optimized/1X/6dcff47816cff6e4d5323ec830c63f61c030b52d_2_600x450.png)
5. Map the Salesforce Attachment structure.

![Alt text](https://global.discourse-cdn.com/business5/uploads/snaplogic2/optimized/1X/522457539b04370232439685f689db82e74e3f14_2_650x350.png)

6. Create the Salesforce attachment record using the Salesforce Create Snap.

