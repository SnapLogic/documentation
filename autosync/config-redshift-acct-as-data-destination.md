# Configure Redshift as a destination

When creating or editing an AutoSync integration, step 2 requires you to provide connection parameters for the selected destination. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes:

-   Connection configurations that you created in AutoSync.
-   Accounts that you or an Org admin created in the IIP that are saved in:
    -   The global **shared** folder
    -   The **shared** folder, in the **\\~SL-AutoSyncProjectSpace**
    -   Your AutoSync project, **\\~User~<username\>\_<snaplogic\_org\>**, in the **\\~SL-AutoSync-ProjectSpace**

Before configuring Redshift as a destination in AutoSync, you must configure Redshift to allow inbound access from SnapLogic addresses. Refer to [Allowing AutoSync to Access Redshift](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/2610168222/Configuring+a+Redshift+account+as+a+data+destination+in+AutoSync) for instructions.

To create a new Redshift connection configuration, enter the following:

-   A unique, meaningful name such as `Redshift-Sales`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **Endpoint**: Enter the Endpoint server’s address to establish a connection. For example, `54.98.196.248`.
    -   **Port Number**: The port number of the database server.
    -   **Database name**: The name of the destination database.
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data.
    -   **Password**: The password for the account.
    -   **S3 Bucket**: Enter the external S3 Bucket name residing in an external AWS account, to use for staging data on Redshift. For example, `sl-bucket-ca`.
    -   **S3 Folder**: Enter the relative path to a folder in S3 Bucket. This is used as a root folder for staging data on Redshift. For example, `san-francisco` for using `s3://sl-bucket-ca/san-francisco`. If you want to create files at the root level, append a forward slash \( `/` \) to the file path.
    -   **S3 Access-key ID**: Enter the S3 Access key ID part of the AWS authentication. For example, `NAVRGGRV7EDCFVLKJH`.
    -   **S3 Secret Key**: Enter the S3 Secret key part of the AWS Authentication. For example, `2RGiLmL/6bCujkKLaRuUJHY9uSDEjNYr+ozHRtg`.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

-   **Select schema**: AutoSync populates this list from the account. Choose the schema name \(table\) you want to use as your data source.


