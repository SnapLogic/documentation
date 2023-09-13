# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**Important Information about this Pattern**

This Pattern consists of the following Pipelines:&#x20;

* **Master\_SnapLogic\_Folder\_Access\_Check**:&#x20;

This Pipeline is created as a Triggered task. It consumes the email ID and triggers the child Pipeline with the output in JSON format.

**Parameters**: `email ID`\
**Output Values**: `email ID and Path`

**Example**:\
`{“`[`emailId":"`](mailto:emailId%22:%22mohammed.rafi@agilisium.com)`john.doe@imarti.com”,“path”:[“/DEV/projects/JohnDoe “,”/ DEV/projects/Doe”,“/ DEV/projects/46313-Connect”,“/ DEV/projects/Transform1.0_SPARK”,“/ DEV/projects/Snaplogic-logs”]}`

* **SnapLogic-User-Folder-Access-Check**

This Pipeline verifies the user has read access to all the project spaces.

**Parameters**: `email ID`\
**Output Values**: The output field path is passed to the `Master_Snaplogic_Folder_Access_Check` Pipeline.&#x20;

* **Child\_User\_Folder\_Access\_Check**

This Pipeline verifies the user has Read, Write, Execute (RWX) permissions for all the project folders.

\
**Parameters**:

* `Email ID`
* `api_url` set to [`https://elastic.snaplogic.com/api/1/rest/public/groups 3`](https://elastic.snaplogic.com/api/1/rest/public/groups)
* Path containing the org name and project space, such as `/orgname/projectSpace`
* `organization`

**Output Values**: The output fields path and email ID are passed to the `Snaplogic_User_Folder_Access_Check` Pipeline.

