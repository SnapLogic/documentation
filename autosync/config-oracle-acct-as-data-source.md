# Configure an Oracle account as a data source

When creating or editing an AutoSync integration, step 1 requires you to provide connection parameters for the selected source. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes: Oracle account.

1.  Click **Configure new credentials** to create new credentials.

    Alternatively, you can click **Use existing credentials** and select the credentials from the **Select Existing Connection** dropdown.

2.  In **Create new connection tag**, enter a unique name that will help identify your account in AutoSync.

    We recommend that you use an easily recallable or relatable name.

3.  Configure **Account properties**.

    For more information about Oracle accounts, refer to the [Oracle documentation](https://docs.oracle.com/cd/E11882_01/server.112/e10897/users_secure.htm#ADMQS007).

    -   **Hostname**: The hostname of the database. For example, `oracleaccount.dfctruwzzvnq.us-west-2.rds.amzaws.com`.
    -   **Port Number**: The port number of the database server. Default value: `1521`
    -   **Database name**: The name of the source database. For example, `MyDB`.
    -   In the **Database specifier type** drop-down list, select either of the following options to determine the Java Database Connectivity \(JDBC\) URL format that must be used internally. Default value: `Service name`

-   **Service name**: Uses the `jdbc:oracle:thin@//HOST:PORT/DBNAME` format.
-   **SID**: Uses the `jdbc:oracle:thin@HOST:PORT:DBNAME` format.
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data.
    -   **Password**: The password for the account. Note that multiple retries with an invalid password can cause your account to be locked.
4.  **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

5.  **Select schema**: AutoSync populates this list from the account. Choose the schema that contains the tables to load as a source.


