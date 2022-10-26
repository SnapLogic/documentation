# Configure a ServiceNow account as a data source

When creating or editing an AutoSync integration, step 1 requires you to provide connection parameters for the selected source. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes: ServiceNow account.

1.  Click **Configure new credentials** to create new credentials.

    Alternatively, you can click **Use existing credentials** and select the credentials from the **Select Existing Connection** dropdown.

2.  In **Create new connection tag**, enter a unique name that will help identify your account in AutoSync.

    We recommend that you use an easily recallable or relatable name.

3.  Configure **Account properties**.

    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data. For example, `WIN-USER\slogic`.
    -   **Password**: The password for the account.
    -   **Instance**: Enter the name of your ServiceNow instance. For example, if `https://snaplogic.service-now.com/` is the URL of your ServiceNow instance, then `snaplogic` is the instance name.
4.  Click **Validate and Save**.

    If your account successfully validates, it is added to the **Select existing connection** drop-down list. The new source is displayed in the **Select Source** box of the integration workflow on the right side of the integration page.

    **Note:** If an asset with the same name exists, an `Asset conflict error message` is displayed. Multiple attempts with invalid credentials could lock your account.


