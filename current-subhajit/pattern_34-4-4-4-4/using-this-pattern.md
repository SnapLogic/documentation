# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**Important Information about this Pattern**

This **** Pattern has the following Pipelines**:**&#x20;

* **Create\_or\_Update\_Skilljar\_User.slp**
  * Use this Pipeline to create or update a user in Skilljar via the REST API.&#x20;
  * Update the parameters for the action you want to perform. For example, set `empStatus` to `Active` if the user is to be added and made part of the `internal` group.
  * Add the users to the specific group by updating the value of `groupName` in the Snap labeled as Filter Group.
* **Workday Event Based Integration.slp**
  * Use this Pipeline to determine which child Pipeline is triggered when a hire or termination event is created in Workday.&#x20;
* **Employee Journey-Onboarding-AD-SNOW-SF.slp**
  * This Pipeline is triggered when a user is onboarded and added to Workday. &#x20;
* **Employee Journey-Offboarding-AD-SNOW-SF.slp**
  * This Pipeline is triggered when a user is offboarded and removed from Workday.

****

