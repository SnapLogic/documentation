# Configure an AWS S3 account as a data source

1.  -   -   2.  In the **File Type** dropdown list, choose the type of file you want to use for your data source.

    For example, `JSON`.

3.  In the **S3 Bucket URI** field, specify the S3 directory path that contains your source files.

    **Note:** S3 directory paths must start with `s3:///` and end with a forward slash \( `/` \).

    For example:

    -   `s3:///mybucket/myfolder/mysubfolder/ […myanothersubfolder/]`
    -   `s3:///mybucket/myfolder/`
    -   `s3:///mybucket/`

