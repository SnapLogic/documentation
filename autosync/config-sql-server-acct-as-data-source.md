# Configure a Microsoft SQL Server connection

Create a new connection configuration for SQL Server by entering the following:

-   A unique, meaningful name such as `SQL-Server-Sales`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **Hostname**: The hostname of the database. You can use either an IP \(`14.8.276.318`\), or URL \(`sqlservertest.cwstru.us-west-1.rds.amzaws.com`\) for hostname.
    -   **Port Number**: The port number of the database server.
    -   **Database name**: The name of the source database.
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data.
    -   **Password**: The password for the account. Note that multiple retries with an invalid password can cause your account to be locked.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

-   **Select schema**: AutoSync populates this list from the account. Choose the schema that contains the tables to load as a source.


After you select a destination, you will choose the tables to load and synchronize.

