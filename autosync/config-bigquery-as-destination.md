# Configuring Google BigQuery as a destination

When creating or editing an AutoSync integration, step 2 requires you to provide connection parameters for the selected destination. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes:

-   Connection configurations that you created in AutoSync.
-   Accounts that you or an Org admin created in the IIP that are saved in:
    -   The global **shared** folder
    -   The **shared** folder, in the **\\~SL-AutoSyncProjectSpace**
    -   Your AutoSync project, **\\~User~<username\>\_<snaplogic\_org\>**, in the **\\~SL-AutoSync-ProjectSpace**

To configure BigQuery as a new connection:

-   Provide a unique, meaningful name such as `Sales-Shared-BigQuery.`
-   Authorize AutoSync with your Google account.

After authorization:

-   Enter the ID of the BigQuery Project to load data into.
-   From the **Schema** list, select the target schema.

