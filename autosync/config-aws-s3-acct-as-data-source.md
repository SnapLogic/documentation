# Configure an AWS S3 connection

Create a new connection configuration for S3 by entering the following:

-   A unique, meaningful name such as `S3-Shared-Sales`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **Access-key ID**: The S3 Access key ID for authentication. For example, `NAVRGGRV7EDCFVLKJH`.
    -   **Secret Key**: The S3 Secret key for authentication. For example, `2RGiLmL6bCujkKLaRuUJHY9uSDEjNYr+ozHRtg`.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

-   **File Type**: The source file type, `CSV` or `JSON`.
-   **S3 Bucket URI**: The S3 directory path that contains the source files.

    **Note:** S3 directory paths must start with `s3:///` and end with a forward slash \( `/` \). For example:

    -   `s3:///mybucket/myfolder/mysubfolder/ […myanothersubfolder/]`
    -   `s3:///mybucket/myfolder/`
    -   `s3:///mybucket/`

