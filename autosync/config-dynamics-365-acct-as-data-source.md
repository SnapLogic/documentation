# Configure a Microsoft Dynamics 365 connection

Create a new connection configuration for Dynamics 365 by entering the following:

-   A unique, meaningful name such as `Dynamics-365-Sales`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **Dynamics Organization URL**: The URL for the Dynamics 365 WebAPI endpoint. For example: `https://organization.api.crm.dynamics.com/api/data/v9.1/`.
    -   **Client ID**: The client ID associated with your account, in the following format: `9el09921-7c72-432d-b552-a21e8b1ab143`
    -   **Client Secret**: The client secret associated with your account, in the following format: `YQlf7Q11HdTTYJZdwpx5VfbvFhHMCpJflBAtJP8m9X4=.`
    -   **Header authenticated**: Select if the account requires bearer header authentication.
    -   **Oauth2 Endpoint**: The URL of the authorization endpoint. For example: `https://login.microsoftonline.com/yourcompany.com/oauth2/authorize`.
    -   **Oauth2 Token**: The authorization token. For example: `https://login.microsoftonline.com/yourcompany.com/oauth2/token`.
    -   **Auth endpoint resource**: The URL for OAuth in the form: `https://login.microsoftonline.com/common/oauth2/authorize?resource=[URL of the D365Environment]`. For example, `https://login.microsoftonline.com/common/oauth2/authorize?resource=https://organization.crm.dynamics.com`.
-   **Authorize**: Authorize with your Microsoft account.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.

-   **Select schema**: AutoSync populates this list from the account. Choose the schema that contains the tables to load as a source.


After you select a destination, you will choose the tables to load and synchronize.

