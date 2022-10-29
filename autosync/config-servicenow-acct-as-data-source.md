# Configure a ServiceNow connection

When creating or editing an AutoSync integration, step 1 requires you to provide connection parameters for the selected source. You can create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes:

-   Connection configurations that you created in AutoSync.
-   Accounts that you or an Org admin created in the IIP that are saved in:
    -   The global **shared** folder
    -   The **shared** folder, in the `SL-AutoSyncProjectSpace`
    -   Your AutoSync project, `~User<username>_<snaplogic_org>`, in the **SL-AutoSync-ProjectSpace**

Create a new connection configuration for ServiceNow by entering the following:

-   A unique, meaningful name such as `S3-Integration`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data.
    -   **Password**: The password for the account. Note that multiple retries with an invalid password can cause your account to be locked.
    -   **Instance**: Enter the name of your ServiceNow instance. This is the URL without the protocol. For example, if `https://snaplogic.service-now.com/` is the URL of your ServiceNow instance, `snaplogic.service-now.com` is the instance name.

After configuring a destination, you will choose which tables to synchronize

