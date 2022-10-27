# Configure a Redshift account as a data destination

When creating or editing an AutoSync integration, step 2 requires you to provide connection parameters for the selected destination. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes: Redshift account.

1.  Click **Configure new credentials** to create new credentials.

    Alternatively, you can click **Use existing credentials** and select the credentials from the **Select Existing Connection** dropdown.

2.  In **Create new connection tag**, enter a unique name that will help identify your account in AutoSync.

    We recommend that you use an easily recallable or relatable name.

3.  Configure **Account properties**.

    For more information about Redshift accounts, refer to the [Redshift documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html).

    -   **Endpoint**: Enter the Endpoint server’s address to establish a connection. For example, `54.98.196.248`.
    -   **Port Number**: The port number of the database server.
    -   **Database name**: The name of the destination CDW.
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data.
    -   **Password**: The password for the account.
    -   **S3 Bucket**: Enter the external S3 Bucket name residing in an external AWS account, to use for staging data on Redshift. For example, `sl-bucket-ca`.
    -   **S3 Folder**: Enter the relative path to a folder in S3 Bucket. This is used as a root folder for staging data on Redshift. For example, `san-francisco` for using `s3://sl-bucket-ca/san-francisco`. If you want to create files at the root level, append a forward slash \( `/` \) to the file path.
    -   **S3 Access-key ID**: Enter the S3 Access key ID part of the AWS authentication. For example, `NAVRGGRV7EDCFVLKJH`.
    -   **S3 Secret Key**: Enter the S3 Secret key part of the AWS Authentication. For example, `2RGiLmL/6bCujkKLaRuUJHY9uSDEjNYr+ozHRtg`.
4.  **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

5.  **Select schema**: AutoSync populates this list from the account. Choose the schema name \(table\) you want to use as your data source.


