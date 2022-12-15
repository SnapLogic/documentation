# Configure an Azure Synapse Analytics connection

Create a new connection configuration for Azure Synapse Analytics by entering the following:

-   A unique, meaningful name such as `Sales-Shared-Synapse`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties:**
    -   **Hostname**: The URL for Synapse, such as `organization-synapse.sql.azuresynapse.net`
    -   **Port Number**: The Synapse port number. The default is `1433`.
    -   **Database name:** The Synapse database name. For example, `Sales-DB`
    -   **Username**: The username for an account with the correct permissions to write data. For example `Sales-admin`.
    -   **Password**: The password for the account. Note that multiple retries with an invalid password can cause your account to be locked.
    -   **External Location**: The Azure data storage location, either **Blob Storage** or **Azure Data Lake Gen2**.
    -   **External Storage Endpoint**: The storage URL, in one of the following formats:
        -   **Blob storage**: `[https://%3Caccount-name%3E.blob.core.windows.net](https://%3Caccount-name%3E.blob.core.windows.net).`
        -   **Data Lake Gen2**: `[https://%3Caccountname%3E.dfs.core.windows.net](https://%3Caccountname%3E.dfs.core.windows.net).`
    -   **Storage Account**: The Azure storage account name.
    -   **Azure Container**: The container name.
    -   **Azure Folder**: The folder name.
    -   **Azure Auth Type**: The type of authorization AutoSync should use for the account, **Access Key**, **Shared Access Signature**, or **Managed Identity**.
    -   **Azure Identity**: The managed identity for Azure authorization. Required for all three types of authorization.
    -   **Azure Access Key**: The key Azure generated for the account. Required for Access Key and Shared Access Signature authorization.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

-   **Select schema**: AutoSync populates this list from the account. Choose the schema to use as the destination.


