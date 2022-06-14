# Using this Pattern

**Steps**

1. Click **Use Pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the pattern.
3. Click the pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

If the Pipeline runs successfully, you can view the output. For more information, read this article: [My First Pipeline](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/1438412).

How to Configure the Pipeline



Configure the following Marketo information:

* set Service URL to get the OAuth token using the following format:\
  _https://XXX-XXX-XXX.mktorest.com/identity/oauth/token_.
* define the following query parameters:&#x20;
  * client\_id
  * client\_secret
  * grant type: set to client\_credentials.
