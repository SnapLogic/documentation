# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

If the Pipeline runs successfully, you can view the output. For more information, read this article: [My First Pipeline](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/1438412).

If the Pipeline fails, verify the error in the Snap Statistics and resolve it using the suggested resolution. For more information, read this article: [Pipeline Execution Statistics](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/1438478/Pipeline+Execution+Statistics).

**How to Configure the Pipeline**

The Pipeline validates whether the input groups already exist in SnapLogic and if not, creates a new group and adds the list of users to the group.

The output is written to a JSON file on SLDB and gets responses using REST calls. The output values contains the following fields: statusGroup, statusUser, and name.
