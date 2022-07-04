# Configure your Google BigQuery OAuth2 account

For Google BigQuery OAuth2 account, configure your account with the following details:

* **Label:** Enter a unique label for the account.
* **Access token**: The access token for the application which is retrieved while setting up the account for the endpoint.
* **Refresh token**: The refresh token for the application which is retrieved while setting up the account for the endpoint.
* **Access token expiration**: The access token expiration value.
* **OAuth2 Endpoint**: Enter the URL of the endpoint that authorizes the application.&#x20;
* **OAuth2 Token**: Enter the URL of the endpoint that retrieves the token for an authenticated account.
* **Auth endpoint config**: Custom properties for the OAuth2 auth endpoint.
  * **Access Type**: The access type for the token, if offline, then it will be persisted in the account.
  * **Approval Prompt**: The approval type for the token.
  * **Default Standard SQL**: Select this check box if you want to default the dialect in the **Query** field using this account to Standard SQL.
  * **Application scope**: The scope for the applications execution.
* **Auto-refresh token**: Select this checkbox to refresh the token automatically using the refresh token, if the property is enabled. If this property is deselected, the token expires and is not refreshed automatically.
* **Authorize**: Click it to start the OAuth authorization flow. Account will be saved before authorize.
* Click any one of the following:
  * **Apply** to save your account information in Flows.
  * **Cancel** to return to the previous screen.
