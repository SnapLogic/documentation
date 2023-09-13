# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**Important Information about this Pattern**

This Pattern has the following Pipelines**:**&#x20;

* **Get Employee Files.slp**
  * This Pipeline determines the information to include about the active users updated in Workday within the last 2 hours.
  * Execute the Box\_Folder\_Management Pipeline.
  * Get the user’s Expensify information and write it to the user’s Expenses sub-folder.
  * Get the user’s DocuSign information.
  * Get the user’s Skilljar information and write it to the user’s Training sub-folder.
  * Get the user’s 7Geese information and write it to the user’s Performance sub-folder.
  * Get the user’s Jobvite candidate information.
  * Get the user’s active status, employee name, and ID from Workday.
* **Box\_Folder\_Management.slp**
  * This Pipeline is executed to create a folder structure within Box to store relevant data for a new hire, move it to a separate location when an employee leaves, or archive the Terminated folder if the employee is rehired.\
    **Note**: After leaving the company, the folders of an outgoing employee are moved to the Terminated folder. If the same employee is re-hired, their Terminated folder is archived.
* **Check\_and\_Create\_Folder.slp**
  * This Pipeline is executed to verify if the requested folder already exists, and if not, create this folder.&#x20;
* **Push\_File\_to\_Box.slp**
  * This Pipeline is executed to read a file from the SnapLogic platform and write it to a user's folder in Box.&#x20;



