# Configure a Snowflake account as a data destination

When creating or editing an AutoSync integration, step 2 requires you to provide connection parameters for the selected destination. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes:

-   The global **shared** folder
-   The **shared** folder, in the **\\~SL-AutoSyncProjectSpace**
-   Your AutoSync project, **\\~User~<username\>\_<snaplogic\_org\>**, in the **\\~SL-AutoSync-ProjectSpace**

1.  Click **Configure new credentials** to create new credentials.

    Alternatively, you can click **Use existing credentials** and select the credentials from the **Select Existing Connection** dropdown.

2.  In **Create new connection tag**, enter a unique name that will help identify your account in AutoSync.

    We recommend that you use an easily recallable or relatable name.

3.  Configure **Account properties**.

    For more information about Snowflake accounts, refer to the [Snowflake documentation](https://docs.snowflake.com/en/user-guide/admin-user-management.html).

    -   **Hostname**: Enter the hostname of the database to connect.
    -   **Port Number**: Enter the port number of the database server.
    -   **Username**: Enter the username of your account. The username must be valid to connect to the data source. For example, `Autosync_Snowflake_User`.
    -   **Password**: Enter the password for the account.
    -   **Database name**: Enter the name of the destination database.
    -   **Warehouse name**: Enter the name of the destination warehouse into which you want to load your data. You can use any existing warehouse from your Snowflake database. For example, `DEMO_W`.
4.  Click **Validate and Save**.

    If your account successfully validates, it is added to the **Select existing connection** drop-down list. The new source is displayed in the **Select Source** box of the integration workflow on the right side of the integration page.

    **Note:** If an asset with the same name exists, an `Asset conflict error message` is displayed. Multiple attempts with invalid credentials could lock your account.

5.  From the **Select schema** drop-down list, choose the schema name \(table\) you want to use as your data source.

    For example, `oracle_TI (21 tables)`. This schema list is populated directly from the account that you just configured.


