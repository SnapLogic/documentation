# Using this Pattern

**Steps**

1. Click **Use Pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the pattern.
3. Click the pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

If the Pipeline runs successfully, you can view the output. For more information, read this article: [My First Pipeline](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/1438412).

**How to Configure the Pipeline**

In this pipeline, the user details are sent to the JSON Generator via pipeline parameters.\


![](https://aws1.discourse-cdn.com/business5/uploads/snaplogic2/original/2X/9/9b905c0f27da6231209c5f8d2455718e5f3de5c6.png)

The REST Post uses the SnapLogic User API to create the record.\
If a user already exists in SnapLogic, but not within the specified org, this pipeline then updates the existing user.
