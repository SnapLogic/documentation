# Configure an SFTP connection

Upload CSV or JSON files using SFTP \(Secure File Transfer Protocol\). Create a new connection configuration for SFTP by entering the following:

-   A unique, meaningful name such as `SFTP-Marketing-Storage`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data.
    -   **Password**: The password for the account. Note that multiple retries with an invalid password can cause your account to be locked.

After you save and AutoSync validates the account, you will select the type of file to load and provide the hostname, port number, and optionally, directory path. Please note that data loaded from SFTP is converted to strings in the destination.

