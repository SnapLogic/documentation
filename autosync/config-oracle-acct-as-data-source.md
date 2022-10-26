# Configure an Oracle account as a data source

When creating or editing an AutoSync integration, step 1 requires you to provide connection parameters for the selected source. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes: Oracle account.

1.  Click **Configure new credentials** to create new credentials.

    Alternatively, you can click **Use existing credentials** and select the credentials from the **Select Existing Connection** dropdown.

2.  In **Create new connection tag**, enter a unique name that will help identify your account in AutoSync.

    We recommend that you use an easily recallable or relatable name.

3.  Configure **Account properties**.

    For more information about Oracle accounts, refer to the [Oracle documentation](https://docs.oracle.com/cd/E11882_01/server.112/e10897/users_secure.htm#ADMQS007).

    -   **Hostname**: Enter the hostname of the database to connect. For example, `oracleaccount.dfctruwzzvnq.us-west-2.rds.amzaws.com`.
    -   **Port Number**: Enter the port number of the database server. Default value: `1521`
    -   **Database name**: Enter the name of the source database. For example, `MyDB`.
    -   In the **Database specifier type** drop-down list, select either of the following options to determine the Java Database Connectivity \(JDBC\) URL format that must be used internally. Default value: `Service name`

-   **Service name**: Uses the `jdbc:oracle:thin@//HOST:PORT/DBNAME` format.
-   **SID**: Uses the `jdbc:oracle:thin@HOST:PORT:DBNAME` format.
    -   **Username**: Enter the username of your account. The username must be valid to connect to the data source.
    -   **Password**: Enter the password for the account.
4.  Click **Validate and Save**.

    If your account successfully validates, it is added to the **Select existing connection** drop-down list. The new source is displayed in the **Select Source** box of the integration workflow on the right side of the integration page.

    **Note:** If an asset with the same name exists, an `Asset conflict error message` is displayed. Multiple attempts with invalid credentials could lock your account.

5.  From the **Select schema** drop-down list, choose the schema name \(table\) you want to use as your data source.

    For example, `oracle_TI (21 tables)`. This schema list is populated directly from the account that you just configured.


