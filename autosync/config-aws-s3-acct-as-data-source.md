# Configure an AWS S3 connection

Create a new connection configuration for S3 by entering the following:

-   A unique, meaningful name such as `S3-Integration`.
-   **Account Properties**:
    -       -   -   **File Type**: The source file type, `CSV` or `JSON`.
-   **S3 Bucket URI**: The S3 directory path that contains the source files.

    **Note:** S3 directory paths must start with `s3:///` and end with a forward slash \( `/` \). For example:

    -   `s3:///mybucket/myfolder/mysubfolder/ […myanothersubfolder/]`
    -   `s3:///mybucket/myfolder/`
    -   `s3:///mybucket/`

