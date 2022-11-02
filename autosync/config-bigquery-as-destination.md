# Configure a Google BigQuery connectionn

Create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes:

-   Connection configurations that you created in AutoSync.
-   Accounts that you or an Org admin created in the IIP, including nondynamic Accounts saved in:
    -   The global `shared` folder
    -   The `shared` folder, in the `SL-AutoSyncProjectSpace`
    -   Your AutoSync project, `~User~<username>_<snaplogic_org>`, in the `SL-AutoSync-ProjectSpace`

To configure BigQuery as a new connection:

-   Provide a unique, meaningful name such as `Sales-Shared-BigQuery.` If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   Authorize AutoSync with your Google account.

After authorization:

-   Enter the ID of the BigQuery Project to load data into.
-   From the **Schema** list, select the destination schema.

