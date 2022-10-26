# Configure Snowflake as a destination

When creating or editing an AutoSync integration, step 2 requires you to provide connection parameters for the selected destination. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes:

-   The global **shared** folder
-   The **shared** folder, in the **\\~SL-AutoSyncProjectSpace**
-   Your AutoSync project, **\\~User~<username\>\_<snaplogic\_org\>**, in the **\\~SL-AutoSync-ProjectSpace**

Create a new connection configuration for Snowflake by entering the following:

-   A unique, meaningful name such as `Sales-Shared-Snowflake`
-   **Account Properties**
    -   **Hostname**:The hostname part of the connection URL. For example, if the Snowflake URL is https://snaplogic.snowflakecomputing.com/console\#/internal/worksheet, the hostname is snaplogic.snowflakecomputing.com.
    -   **Port Number**: The port number of the database server.
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data. For example, `Autosync_Snowflake_User`.
    -   **Password**: The password for the account.
    -   **Database name**: The name of the destination CDW.
    -   **Warehouse name**: The destination warehouse in which to load the data. You can use any existing warehouse from your Snowflake database. For example, `DEMO_WH`.

