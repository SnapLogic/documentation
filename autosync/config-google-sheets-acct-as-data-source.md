# Configure a Google Sheets connection

When creating or editing an AutoSync integration, step 1 requires you to provide connection parameters for the selected source. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes:

-   Connection configurations that you created in AutoSync.
-   Accounts that you or an Org admin created in the IIP that are saved in:
    -   The global `shared` folder
    -   The `shared` folder, in the `SL-AutoSyncProjectSpace`
    -   Your AutoSync project, `~User~<username>_<snaplogic_org>`, in the `SL-AutoSync-ProjectSpace`

Create a new connection configuration for Google Sheets:

-   Enter a unique, meaningful name such as `Accounting-Google-Spreadsheet`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Authorize:** Authorizes **SnapLogic Sheets & Drive Integration** with your Google Account.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

-   **Select Spreadsheet**: The spreadsheet to use as a source for this integration. For example, `NEW LEADS DATA`. After selecting a destination, you will choose which sheets to load.

