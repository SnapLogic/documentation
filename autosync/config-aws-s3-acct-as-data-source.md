# Configure an AWS S3 account as a data source

When creating or editing an AutoSync integration, step 1 requires you to provide connection parameters for the selected source. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes: AWS S3 account.

1.  Click **Configure new credentials** to create new credentials.

    Alternatively, you can click **Use existing credentials** and select the credentials from the **Select Existing Connection** dropdown.

2.  In **Create new connection tag**, enter a unique name that will help identify your account in AutoSync.

    We recommend that you use an easily recallable or relatable name.

3.  Configure **Account properties**.

    For more information about AWS S3 accounts, refer to the [AWS S3 documentation](https://docs.aws.amazon.com/s3/index.html).

    -   **Access-key ID**: Enter the S3 Access key ID part of the AWS authentication. For example, `NAVRGGRV7EDCFVLKJH`.
    -   **Secret Key**: Enter the S3 Secret key part of the AWS Authentication. For example, `2RGiLmL6bCujkKLaRuUJHY9uSDEjNYr+ozHRtg`.
4.  **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

5.  In the **File Type** dropdown list, choose the type of file you want to use for your data source.

    For example, `JSON`.

6.  In the **S3 Bucket URI** field, specify the S3 directory path that contains your source files.

    **Note:** S3 directory paths must start with `s3:///` and end with a forward slash \( `/` \).

    For example:

    -   `s3:///mybucket/myfolder/mysubfolder/ […myanothersubfolder/]`
    -   `s3:///mybucket/myfolder/`
    -   `s3:///mybucket/`

