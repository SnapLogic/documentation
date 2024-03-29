# Configure a Coupa connection

Create a new connection configuration for Coupa by entering the following:

-   A unique, meaningful name such as `Coupa-Sales-Shared`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **Host**: The domain name of your Coupa instance. For example, `https://snaplogic.coupacloud.com/`.
    -   **Client ID**: The ID generated by Coupa during OAuth 2.0 client creation. For example, `45b546f46b004d10d275c2b553bc7g44`.
    -   **Client Secret**: The secret generated by Coupa during OAuth 2.0 client creation. For example, `zcvfc098adfdb343s`.
    -   **Grant Type**: Keep the default value, **client\_credentials**.
    -   **OAuth2 Token**: The access token returned by Coupa as a response to a POST with the client parameters, as described in the Coupa documentation.
    -   Click **Authorize** to grant AutoSync access to your Coupa account.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.


