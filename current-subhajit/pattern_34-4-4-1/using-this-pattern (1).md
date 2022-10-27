# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**How to Configure the Pipeline**

In the REST Post (labeled as _Get Taleo authToken in the Pattern Pipeline_) Snap:&#x20;

* Specify the Taleo instance for the **Service URL** field. For example, [https://chk.tbe.taleo.net/chk06/ats/api/v1/login](https://chk.tbe.taleo.net/chk06/ats/api/v1/login)
* Set the value for the `orgCode` Query Parameter to the Taleo orgCode of your organization.
* Specify the valid username and password to connect to the Taleo account.&#x20;
