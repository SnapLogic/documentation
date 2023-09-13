# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**Important Information about this Pattern**

This Pattern consists of the following Pipelines:

* **Migrate Accounts**

1. The SnapLogic List Snap gathers the list of accounts in the specified `source_path` parameter.&#x20;
2. The SnapLogic Read Snap reads the incoming `$path` for the accounts.&#x20;
3. The Mapper Snap maps the target path.
4. The SnapLogic Create Snap writes the accounts to the target location.

* **Migrate Files**

1. The SnapLogic List Snap gathers the list of files in the specified `source_path` parameter.
2. The Mapper Snap maps the source path to a `$source_path` field for use in the SnapLogic Read Snap.&#x20;
3. The SnapLogic Read Snap reads the incoming `$path` for the files.&#x20;
4. The SnapLogic Create Snap writes the files to the target location.

* **Migrate Pipelines**

1. The SnapLogic List Snap gathers the list of Pipelines in the specified `source_path` parameter.&#x20;
2. The SnapLogic Read Snap reads the incoming `$path` for the Pipelines.&#x20;
3. The Mapper Snap maps the target path.&#x20;
4. The SnapLogic Create Snap writes the Pipelines to the target location.
