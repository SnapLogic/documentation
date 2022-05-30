# Configure your Microsoft Dynamics 365 for Sales account

Select the project **Location** to save your account information. The default shared option will share the account with all the other Flows' users.

Configure your account with the following details:

* **Label:** Specify a unique user-provided label for the account.
* **Dynamics Organization URL**: Enter the URL for the MS Dynamics 365 For Sales WebAPI endpoint.
* **Client ID**: Enter the client ID associated with your Microsoft Dynamics application.
* **Client Secret:** Enter the client secret associated with your account.
* **Access token**: _Auto-generated after authorization._ The token that SnapLogic uses to make API requests on behalf of the user associated with the client ID.
* **Refresh token**: _Auto-generated after authorization_. The refresh token associated with your account. If the refresh token is stored, then the access token can be refreshed automatically before it expires.
* **Access token expiration**: The access token expiration value.
* **Header authenticated**: Select to indicate that the endpoint uses bearer header authentication.
* In **OAuth2 Endpoint,** enter the authorization endpoint to authorize the application.
* **OAuth2 Token**, enter the token endpoint to get the access token.
* **Token endpoint config**: Enable this if the endpoint uses bearer header authentication. Click **+** on the right of the field to add a row. This field set comprises the following fields:
  * Token endpoint parameter
  * Token endpoint parameter value
* **Auth endpoint config**: Use this field set to assign scopes for the OAuth2 authentication endpoint for the account. It is recommended to define at least one scope entry in this fieldset. Click **+** on the right of the field to add a row. This field set comprises the following fields:
  * Authentication parameter
  * Authentication parameter value
* Select the **Auto-refresh token** checkbox to refresh the token automatically using your Microsoft Dynamics account's refresh token
* Click **Authorize.** You will be directed to the login page of your Microsoft Dynamics account.
* Click any one of the following:
  * **Apply** to save your account information in Flows.
  * **Validate** to verify if your account information is valid by connecting Flows with your Microsoft Dynamics 365 for Sales account.
  * **Cancel** to return to the previous screen.
