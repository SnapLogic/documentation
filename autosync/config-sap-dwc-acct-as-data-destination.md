# Configure a SAP Data Warehouse Cloud account as a data destination

When creating or editing an AutoSync integration, step 2 requires you to provide connection parameters for the selected destination. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes:

-   Connection configurations that you created in AutoSync.
-   Accounts that you or an Org admin created in the IIP that are saved in:
    -   The global **shared** folder
    -   The **shared** folder, in the **\\~SL-AutoSyncProjectSpace**
    -   Your AutoSync project, **\\~User~<username\>\_<snaplogic\_org\>**, in the **\\~SL-AutoSync-ProjectSpace**

To create a new SAP DWC connection configuration, enter the following:

-   A unique, meaningful name such as `SAP-Accounting`.
-   **Account Properties**:
    -   **Hostname**: The hostname of the database. For example, `ww23456-1db2-4dd0-8cbe-71521705c697.hana.prod-eu10.hanacloud.ondemand.com`.
    -   **Port Number**: The port number of the database server.
    -   **Database name**: The name of the destination CDW.

        **Note:** Enter the Database name in this format: `Database name: Space Schema Name`.

    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data.
    -   **Password**: The password for the account.
-   -   
