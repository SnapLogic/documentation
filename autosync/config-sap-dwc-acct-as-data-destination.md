# Configure an SAP Data Warehouse Cloud \(DWC\) connection

Before creating a connection configuration for SAP DWC you must add SnapLogic IP addresses to the DWC allowlist. The entries must be approved by SAP before AutoSync can connect to the SAP DWC. For more information about adding IP addresses to the allowlist, refer to the SnapLogic and SAP documentation

To create a new SAP DWC connection configuration, enter the following:

-   A unique, meaningful name such as `SAP-Accounting-Admin`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **Hostname**: The hostname of the database. For example, `ww23456-1db2-4dd0-8cbe-71521705c697.hana.prod-eu10.hanacloud.ondemand.com`.
    -   **Port Number**: The port number of the database server.
    -   **Database name**: The name of the space schema.
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data.
    -   **Password**: The password for the account. Note that multiple retries with an invalid password can cause your account to be locked.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

-   **Select schema**: AutoSync populates this list from the account. Choose the schema to use as the destination.


