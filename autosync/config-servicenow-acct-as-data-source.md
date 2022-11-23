# Configure a ServiceNow connection

Create a new connection configuration for ServiceNow by entering the following:

-   A unique, meaningful name such as `ServiceNow-IT-Admin`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **Username**: A username for an account with the correct permissions for AutoSync to load and synchronize data.
    -   **Password**: The password for the account. Note that multiple retries with an invalid password can cause your account to be locked.
    -   **Instance**: Enter the name of your ServiceNow instance. This is the URL without the protocol. For example, if `https://snaplogic.service-now.com/` is the URL of your ServiceNow instance, `snaplogic.service-now.com` is the instance name.

After configuring a destination, you will choose which tables to synchronize.

