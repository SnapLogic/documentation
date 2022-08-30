# Configure a Redshift account as a data destination {#config-redshift-acct-as-data-destination .task}

You can configure a new account destination in AutoSync by using the user credentials from your existing Redshift account.

1.  Click **Configure new credentials** to create new credentials.

    Alternatively, you can click **Use existing credentials** and select the credentials from the **Select Existing Connection** dropdown.

2.  In **Create new connection tag**, enter a unique name that will help identify your account in AutoSync.

    We recommend that you use an easily recallable or relatable name.

3.  Configure **Account properties**.

    For more information about Redshift accounts, refer to the [Redshift documentation](https://docs.aws.amazon.com/redshift/latest/dg/r_CREATE_USER.html).

    -   **Endpoint**: Enter the Endpoint server’s address to establish a connection. For example, `54.98.196.248`.
    -   **Port Number**: Enter the port number of the database server.
    -   **Database name**: Enter the name of the destination database.
    -   **Username**: Enter the username of your account. The username must be valid to connect to the data source.
    -   **Password**: Enter the password for the account.
    -   **S3 Bucket**: Enter the external S3 Bucket name residing in an external AWS account, to use for staging data on Redshift. For example, `sl-bucket-ca`.
    -   **S3 Folder**: Enter the relative path to a folder in S3 Bucket. This is used as a root folder for staging data on Redshift. For example, `san-francisco` for using `s3://sl-bucket-ca/san-francisco`. If you want to create files at the root level, append a forward slash \( `/` \) to the file path.
    -   **S3 Access-key ID**: Enter the S3 Access key ID part of the AWS authentication. For example, `NAVRGGRV7EDCFVLKJH`.
    -   **S3 Secret Key**: Enter the S3 Secret key part of the AWS Authentication. For example, `2RGiLmL/6bCujkKLaRuUJHY9uSDEjNYr+ozHRtg`.
4.  Click **Validate and Save**.

    If your account successfully validates, it is added to the **Select existing connection** drop-down list. The new source is displayed in the **Select Source** box of the integration workflow on the right side of the integration page.

    **Note:** If an asset with the same name exists, an `Asset conflict error message` is displayed. Multiple attempts with invalid credentials could lock your account.

5.  From the **Select schema** drop-down list, choose the schema name \(table\) you want to use as your data source.

    For example, `oracle_TI (21 tables)`. This schema list is populated directly from the account that you just configured.


