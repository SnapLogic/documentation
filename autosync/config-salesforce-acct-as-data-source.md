# Configure a Salesforce connection

Create a new connection configuration for Salesforce by entering the following:

-   A unique, meaningful name such as `Salesforce-Marketing-Shared`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   Select **Include deleted records** to have AutoSync track deletions. On the first load, AutoSync adds all previously deleted records to the destination with a value of `True` in the `IsDeleted` column. On synchronization, AutoSync inserts `True` in the `IsDeleted` column for records deleted since the last load.
-   **Account Properties**:
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data. For example, `WIN-USER\slogic`.
    -   **Password**: The password for the account. Note that multiple retries with an invalid password can cause your account to be locked.
    -   **Login URL**: Enter the URL that is used to log in to Salesforce. For example, `https://login.salesforce.com/`.
    -   **Security token**: Enter the valid security token configured during the account configuration. To create a security token, log into your Salesforce account and go to **Personal Setup** \> **My Personal Information** \> **Reset My Security Token**.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.


After configuring a destination, you will choose which tables to synchronize.

