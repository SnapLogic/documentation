# Configure a SAP Data Warehouse Cloud account as a data destination

When creating or editing an AutoSync integration, step 2 requires you to provide connection parameters for the selected destination. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes: SAP-DWC account.

1.  Click **Configure new credentials** to create new credentials.

    Alternatively, you can click **Use existing credentials** and select the credentials from the **Select Existing Connection** dropdown.

2.  In **Create new connection tag**, enter a unique name that will help identify your account in AutoSync.

    We recommend that you use an easily recallable or relatable name.

3.  Configure **Account properties**.

    For more information about SAP DWC accounts, refer to the [SAP DWC documentation](https://help.sap.com/viewer/9f804b8efa8043539289f42f372c4862/cloud/en-US/1c7dc8c6acad44869ca9105d0b9d80c9.html?q=setting%20up%20your%20instance).

    For more information about SAP Data Warehouse, refer to the [SAP DWC Help Portal](https://help.sap.com/viewer/product/SAP_DATA_WAREHOUSE_CLOUD/cloud/en-US).

    -   **Hostname**: The hostname of the database. For example, `ww23456-1db2-4dd0-8cbe-71521705c697.hana.prod-eu10.hanacloud.ondemand.com`.
    -   **Port Number**: The port number of the database server.
    -   **Database name**: The name of the destination CDW.

        **Note:** When configuring a SAP account that is used to connect to SAP DWC, enter the Database name in this format: `Database name: Space Schema Name`. For the account to work as expected, you must [add SnapLogic IP addresses to the allow list](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/1449033775) in your SAP DWC. This entry must be approved by SAP before you can connect to the SAP DWC. For more information about adding IP addresses to the Allow list, refe to the [SAP Documentation](https://help.sap.com/viewer/9f804b8efa8043539289f42f372c4862/cloud/en-US/a3c214514ef94e899459f68f4c1e2a23.html).

    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data.
    -   **Password**: The password for the account.
4.  Click **Validate and Save**.

    If your account successfully validates, it is added to the **Select existing connection** drop-down list. The new source is displayed in the **Select Source** box of the integration workflow on the right side of the integration page.

    **Note:** If an asset with the same name exists, an `Asset conflict error message` is displayed. Multiple attempts with invalid credentials could lock your account.

5.  From the **Select schema** drop-down list, choose the schema name \(table\) you want to use as your data source.

    For example, `oracle_TI (21 tables)`. This schema list is populated directly from the account that you just configured.


