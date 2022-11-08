# Configure an Oracle connection

Create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes:

-   Connection configurations that you created in AutoSync.
-   Accounts that you or an Org admin created in the IIP, including nondynamic Accounts saved in:
    -   The global `shared` folder
    -   The `shared` folder, in the `SL-AutoSyncProjectSpace`
    -   Your AutoSync project, `~User~<username>_<snaplogic_org>`, in the `SL-AutoSync-ProjectSpace`

Create a new connection configuration for Oracle by entering the following:

-   A unique, meaningful name such as `Oracle-Sales-Admin`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **Hostname**: The hostname of the database. For example, `oracleaccount.dfctruwzzvnq.us-west-2.rds.amzaws.com`.
    -   **Port Number**: The port number of the database server. Default value: `1521`
    -   **Database name**: The name of the source database. For example, `MyDB`.
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data.
    -   **Password**: The password for the account. Note that multiple retries with an invalid password can cause your account to be locked.
    -   **Database specifier type**: the format of the JDBC URL. AutoSync formats the connection parameters into one of the following options. Default value: `Service name`

        -   **Service name**: Uses the `jdbc:oracle:thin@//HOST:PORT/DBNAME` format.
        -   **SID**: Uses the `jdbc:oracle:thin@HOST:PORT:DBNAME` format.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

-   **Select schema**: AutoSync populates this list from the account. Choose the schema that contains the tables to load as a source.


