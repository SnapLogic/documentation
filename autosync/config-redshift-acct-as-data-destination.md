# Configure a Redshift connection

Before configuring Redshift as a destination in AutoSync, you must allow inbound access from SnapLogic IIP addresses. Refer to the SnapLogic and Redshift documentation for instructions.

To create a new Redshift connection configuration, enter the following:

-   A unique, meaningful name such as `Redshift-Sales`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **Endpoint**: The endpoint portion of the JDBC URL to access Redshift. For example, `cluster.abc123xyz789.us-west-2.redshift.amazonaws.com`.
    -   **Port Number**: The port number of the database server.
    -   **Database name**: The name of the destination database.
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data.
    -   **Password**: The password for the account. Note that multiple retries with an invalid password can cause your account to be locked.
    -   **S3 Bucket**: The external S3 Bucket name residing in an external AWS account, to use for staging data on Redshift. For example, `sl-bucket-ca`.
    -   **S3 Folder**: The relative path to a folder in S3 Bucket. This is used as a root folder for staging data on Redshift. For example, `san-francisco` for using `s3://sl-bucket-ca/san-francisco`. To create files at the root level, append a forward slash \( `/` \) to the file path.
    -   **S3 Access-key ID**: The S3 Access key ID part of the AWS authentication. For example, `NAVRGGRV7EDCFVLKJH`.
    -   **S3 Secret Key**: The S3 Secret key part of the AWS Authentication. For example, `2RGiLmL/6bCujkKLaRuUJHY9uSDEjNYr+ozHRtg`.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

-   **Select schema**: AutoSync populates this list from the account. Choose the schema to use as the destination.


