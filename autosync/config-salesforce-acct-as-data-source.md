# Configure a Salesforce account as a data source {#config-salesforce-acct-as-data-source .task}

You can configure a new account source in AutoSync by using the user credentials from your existing Salesforce account.

1.  Click **Configure new credentials** to create new credentials.

    Alternatively, you can click **Use existing credentials** and select the credentials from the **Select Existing Connection** dropdown.

2.  In **Create new connection tag**, enter a unique name that will help identify your account in AutoSync.

    We recommend that you use an easily recallable or relatable name.

3.  Configure **Account properties**.

    **Note:** The username and password should be the same as configured in the endpoint.

    -   **Username**: Enter the username of your account. The username must be valid to connect to the data source. For example, `WIN-USER\slogic`.
    -   **Password**: Enter the password for the account.
    -   **Login URL**: Enter the URL that is used to log in to Salesforce. For example, https://login.salesforce.com/.
    -   **Security token**: Enter the valid security token configured during the account configuration. To create a security token, log into your Salesforce account and go to **Personal Setup** \> **My Personal Information** \> **Reset My Security Token**.
4.  Click **Validate and Save**.

    If your account successfully validates, it is added to the **Select existing connection** drop-down list. The new source is displayed in the **Select Source** box of the integration workflow on the right side of the integration page.

    **Note:** If an asset with the same name exists, an `Asset conflict error message` is displayed. Multiple attempts with invalid credentials could lock your account.


