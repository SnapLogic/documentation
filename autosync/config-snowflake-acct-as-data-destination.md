# Configure Snowflake as a destination

When creating or editing an AutoSync integration, step 2 requires you to provide connection parameters for the selected destination. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes:

-   The global **shared** folder
-   The **shared** folder, in the **\\~SL-AutoSyncProjectSpace**
-   Your AutoSync project, **\\~User~<username\>\_<snaplogic\_org\>**, in the **\\~SL-AutoSync-ProjectSpace**

Create a new connection configuration for Snowflake by entering the following:

-   A unique, meaningful name such as `Sales-Shared-Snowflake`
-   **Account Properties**
    -   **Hostname**: Enter the hostname of the database to connect.
    -   **Port Number**: Enter the port number of the database server.
    -   **Username**: Enter the username of your account. The username must be valid to connect to the data source. For example, `Autosync_Snowflake_User`.
    -   **Password**: Enter the password for the account.
    -   **Database name**: Enter the name of the destination database.
    -   **Warehouse name**: Enter the name of the destination warehouse into which you want to load your data. You can use any existing warehouse from your Snowflake database. For example, `DEMO_W`.

