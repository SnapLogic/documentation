# Configure an SAP Data Warehouse Cloud \(DWC\) connection

When creating or editing an AutoSync integration, step 2 requires you to provide connection parameters for the selected destination. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes:

-   Connection configurations that you created in AutoSync.
-   Accounts that you or an Org admin created in the IIP that are saved in:
    -   The global **shared** folder
    -   The **shared** folder, in the **\\~SL-AutoSyncProjectSpace**
    -   Your AutoSync project, **\\~User\\~<username\>\_<snaplogic\_org\>**, in the **\\~SL-AutoSync-ProjectSpace**

Before creating a connection configuration for SAP DWC you must add [SnapLogic IP addresses](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/1449033775/) to the DWC allowlist. The entries must be approved by SAP before AutoSync can connect to the SAP DWC. For more information about adding IP addresses to the allowlist, refer to the [SAP Documentation](https://help.sap.com/viewer/9f804b8efa8043539289f42f372c4862/cloud/en-US/a3c214514ef94e899459f68f4c1e2a23.html).

To create a new SAP DWC connection configuration, enter the following:

-   A unique, meaningful name such as `SAP-Accounting`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **Hostname**: The hostname of the database. For example, `ww23456-1db2-4dd0-8cbe-71521705c697.hana.prod-eu10.hanacloud.ondemand.com`.
    -   **Port Number**: The port number of the database server.
    -   **Database name**: The name of the space schema.
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data.
    -   **Password**: The password for the account.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

-   **Select schema**: AutoSync populates this list from the account. Choose the schema to use as the destination.


