# Configure a Snowflake connection

Create a new connection configuration for Snowflake by entering the following:

-   A unique, meaningful name such as `Sales-Shared-Snowflake`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**
    -   **Hostname**: The hostname part of the connection URL. For example, if the Snowflake URL is https://snaplogic.snowflakecomputing.com/console\#/internal/worksheet, the hostname is snaplogic.snowflakecomputing.com.
    -   **Port number**: The port number for Snowflake.
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data. For example, `Autosync_Snowflake_User`.
    -   **Password**: The password for the account. Note that multiple retries with an invalid password can cause your account to be locked.
    -   **Database name**: The name of the destination database.
    -   **Warehouse name**: The destination warehouse in which to load the data. You can use any existing warehouse from your Snowflake database. For example, `DEMO_WH`.
    -   **Role**: Optional. The role for AutoSync to use when loading the data. For example, Sysadmin.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

-   **Select schema**: AutoSync populates this list from the account. Choose the schema to use as the destination.


