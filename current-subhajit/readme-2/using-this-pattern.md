# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**Important Information about this Pattern**

This Pattern has the following Pipelines:&#x20;

* **Master\_UserProvisioning.slp:** This Pipeline is called from a Triggered task. It consumes the input JSON message containing two fields: `Email ID` and A`dministrator`.&#x20;
  * Email ID: Contains the list of users to be added to SnapLogic.
  * Administrator: Contains the value as `true` or `false,`specifying whether the user is an administrator.
* The output is written to SLDB in a JSON file, and the unconnected output gets the response using the REST calls.
* The Output Values contain the `statusUser`, `user`, and `email` fields.&#x20;

**slProvisioning-createUser.slp:** This Pipeline validates whether the user already exists in SnapLogic and, if not, creates a new user and assigns a default folder in SnapLogic using the REST Post Snap. It also captures the error and sends the response to the master user provisioning Pipeline.

\


\


\
