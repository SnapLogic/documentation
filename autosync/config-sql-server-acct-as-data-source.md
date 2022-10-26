# Configure a SQL Server account as a data source

When creating or editing an AutoSync integration, step 1 requires you to provide connection parameters for the selected source. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes: SQL Server account.

1.  Click **Configure new credentials** to create new credentials.

    Alternatively, you can click **Use existing credentials** and select the credentials from the **Select Existing Connection** dropdown.

2.  In **Create new connection tag**, enter a unique name that will help identify your account in AutoSync.

    We recommend that you use an easily recallable or relatable name.

3.  Configure **Account properties**.

    For more information about SQL Server accounts, refer to the [Microsoft - SQL Server documentation](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/create-a-database-user?view=sql-server-ver15).

    -   **Hostname**: The hostname of the database. You can use either an IP \(`14.8.276.318`\), or URL \(`sqlservertest.cwstru.us-west-1.rds.amzaws.com`\) for hostname.
    -   **Port Number**: The port number of the database server.
    -   **Database name**: The name of the source database.
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data. For example, `WIN-USER\slogic`.
    -   **Password**: The password for the account.
4.  Click **Validate and Save**.

    If your account successfully validates, it is added to the **Select existing connection** drop-down list. The new source is displayed in the **Select Source** box of the integration workflow on the right side of the integration page.

    **Note:** If an asset with the same name exists, an `Asset conflict error message` is displayed. Multiple attempts with invalid credentials could lock your account.

5.  From the **Select schema** drop-down list, choose the schema name \(table\) you want to use as your data source.

    For example, `oracle_TI (21 tables)`. This schema list is populated directly from the account that you just configured.


