# Configure a Salesforce connection

When creating or editing an AutoSync integration, step 1 requires you to provide connection parameters for the selected source. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes:

-   Connection configurations that you created in AutoSync.
-   Accounts that you or an Org admin created in the IIP that are saved in:
    -   The global **shared** folder
    -   The **shared** folder, in the **SL-AutoSyncProjectSpace**
    -   Your AutoSync project, **User<username\>\_<snaplogic\_org\>**, in the **SL-AutoSync-ProjectSpace**

Create a new connection configuration for Salesforce by entering the following:

-   A unique, meaningful name such as `Salesforce-Marketing-Shared`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data. For example, `WIN-USER\slogic`.
    -   **Password**: The password for the account. Note that multiple retries with an invalid password can cause your account to be locked.
    -   **Login URL**: Enter the URL that is used to log in to Salesforce. For example, `https://login.salesforce.com/`.
    -   **Security token**: Enter the valid security token configured during the account configuration. To create a security token, log into your Salesforce account and go to **Personal Setup** \> **My Personal Information** \> **Reset My Security Token**.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.


After configuring a destination, you will choose which tables to synchronize

