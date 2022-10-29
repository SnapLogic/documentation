# Configure an SAP Data Warehouse Cloud \(DWC\) connection

Before creating a connection configuration for SAP DWC you must add [SnapLogic IP addresses](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/1449033775/) to the DWC allowlist. The entries must be approved by SAP before AutoSync can connect to the SAP DWC. For more information about adding IP addresses to the allowlist, refer to the [SAP Documentation](https://help.sap.com/viewer/9f804b8efa8043539289f42f372c4862/cloud/en-US/a3c214514ef94e899459f68f4c1e2a23.html).

To create a new SAP DWC connection configuration, enter the following:

-   A unique, meaningful name such as `SAP-Accounting`.
-   **Account Properties**:
    -   For example, `ww23456-1db2-4dd0-8cbe-71521705c697.hana.prod-eu10.hanacloud.ondemand.com`.
    -       -   **Database name**: The name of the space schema.
    -       -   
