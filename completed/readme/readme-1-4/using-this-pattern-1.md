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

You will need to define the following pipeline parameters:

* _authorization_, in the form of Bearer xxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx:xx
* _endpoint_, in the form of [https://xxx-xxx-xxx.mktorest.com](https://xxx-xxx-xxx.mktorest.com/)
* _GoogleSheetsName_, the name of the Google Sheet to write to
* _sheetName_, the name of the individual worksheet to write to within that Google Sheet
* Then you need to pass the user details with the parameters _first_, _last_, _email_, _title_, _company_, and _country_.

The initial Mapper contains data to create a user. You can either replace these values every time or define Pipeline parameters to pass the values in.
