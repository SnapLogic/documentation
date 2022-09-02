# Configure an AWS S3 account as a data source {#config-aws-s3-acct-as-data-source .task}

You can configure a new account source in AutoSync by using the user credentials from your existing AWS S3 account.

1.  Click **Configure new credentials** to create new credentials.

    Alternatively, you can click **Use existing credentials** and select the credentials from the **Select Existing Connection** dropdown.

2.  In **Create new connection tag**, enter a unique name that will help identify your account in AutoSync.

    We recommend that you use an easily recallable or relatable name.

3.  Configure **Account properties**.

    For more information about AWS S3 accounts, refer to the [AWS S3 documentation](https://docs.aws.amazon.com/s3/index.html).

    -   **Access-key ID**: Enter the S3 Access key ID part of the AWS authentication. For example, `NAVRGGRV7EDCFVLKJH`.
    -   **Secret Key**: Enter the S3 Secret key part of the AWS Authentication. For example, `2RGiLmL6bCujkKLaRuUJHY9uSDEjNYr+ozHRtg`.
4.  Click **Validate and Save**.

    If your account successfully validates, it is added to the **Select existing connection** drop-down list. The new source is displayed in the **Select Source** box of the integration workflow on the right side of the integration page.

    **Note:** If an asset with the same name exists, an `Asset conflict error message` is displayed. Multiple attempts with invalid credentials could lock your account.

5.  In the **File Type** dropdown list, choose the type of file you want to use for your data source.

    For example, `JSON`.

6.  In the **S3 Bucket URI** field, specify the S3 directory path that contains your source files.

    **Note:** S3 directory paths must start with `s3:///` and end with a forward slash \( `/` \).

    For example:

    -   `s3:///mybucket/myfolder/mysubfolder/ […myanothersubfolder/]`
    -   `s3:///mybucket/myfolder/`
    -   `s3:///mybucket/`

