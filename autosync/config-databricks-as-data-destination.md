# Configure a Databricks connection

For a Databricks connection, you can optionally supply credentials for a storage resource account. To configure a new connection:

-   Provide a unique, meaningful name such as `Sales-Shared-Databricks.` If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties:**
    -   **JDBC URL:** The connection URL for the Databricks JDBC driver, in the form: `jdbc:databricks://<Server Hostname>:443;HttpPath=<Http Path>[;property=value[;property=value]]`.
    -   **Use Token Based Authentication**: Select to have AutoSync use a token to authenticate with Databricks.
    -   **Token**: The token value to authenticate with Databricks.
    -   **Database name**: The Databricks database name.
    -   **Source/Target Location**: Defaults to **None**. For staging storage, you can select and configure one of the following:
        -   **Amazon S3**:
            -   **S3 Bucket**: The S3 bucket for staging data.
            -   **S3 Folder**: The folder to use for staging data.
            -   **AWS Authorization type:** Select regular or session credentials.
            -   **S3 Access-key ID:** The access key ID.
            -   **S3 Secret key:** The secret key associated with the access key ID.
        -   **Azure Blob Storage or Azure Data Lake Storage Gen2**
            -   **Azure storage account name**: The storage account name for the endpoint. AutoSync appends `.blob.core.windows.net` to this value when formulating the URL.
            -   **Azure Container**: The name of an existing Azure container.
            -   **Azure folder**: The name of an existing Azure folder.
            -   **Azure Auth Type**: select **Storage Account Key** or **Shared Access Signature**
        -   **DBFS \(Databricks File System\)**:
            -   **DBFS Folder path**: The path to the folder for staging data.
        -   **Google Cloud Storage**:
            -   **GCS Bucket**: The bucket for staging data.
            -   **GCS Folder**: The folder for staging data.
            -   **GCS Authorization type**: The type of authentication AutoSync should use. The default value is **Service Account**.
            -   **Service Account Email**: The email for the account.
            -   **Service Account Key File Path**: The path to the key file for authentication.
        -   **JDBC**:
            -   **Source JDBC URL**: The JDBC URL of the table for staging.
            -   **Source username**: The username for the account.
            -   **Source password**: The password.

