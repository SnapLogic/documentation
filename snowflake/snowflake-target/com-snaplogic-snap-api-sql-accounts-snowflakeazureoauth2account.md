# Configure your Snowflake Azure OAuth2 account



Configure your Snowflake Azure OAuth2 account with the following details:

* **Label:** Enter a unique label for the account.
* **Client ID**: Enter the OAuth Client ID (to be used for token request) that you obtain from the Snowflake Console.
* **Client secret**: Enter the OAuth Client secret that you obtain from the Snowflake Console.
* **Access token**: _Auto-generated after authorization._ The access token associated with the Azure portal application is used to make API requests on behalf of the user associated with the client ID.
* **Refresh token**: _Auto-generated upon account authorization_. The token used to refresh the access token.
* **Access token expiration**: _Auto-generated upon account authorization_. The number of seconds after which the access token expires.
* **Header authenticated**: Select this checkbox if the endpoint uses bearer header authentication.
* **OAuth2 Endpoint:** Enter the tenant ID in the designated position in the URL.
* **OAuth2 Token: E**nter the tenant ID in the designated position in the URL.
* **Token endpoint config**: Enable this if the endpoint uses bearer header authentication. Click ![https://docs-snaplogic.atlassian.net/wiki/download/attachments/896369522/Plus.png?version=1\&modificationDate=1579553898874\&cacheVersion=1\&api=v2](../../.gitbook/assets/0) on the right of the field to add a row. This field set comprises the following fields:
  * Token endpoint parameter
  * Token endpoint parameter value
* **Auth endpoint config**: Use this field set to assign scopes for the OAuth2 authentication endpoint for the account. It is recommended to define at least one scope entry in this fieldset. Click ![https://docs-snaplogic.atlassian.net/wiki/download/attachments/896369522/Plus.png?version=1\&modificationDate=1579553898874\&cacheVersion=1\&api=v2](<../../.gitbook/assets/0 (3)>) on the right of the field to add a row. This field set comprises the following fields:
  * Authentication parameter
  * Authentication parameter value
* **Auto-refresh token**: Select this to refresh the access token automatically.
* Click **Authorize.** You will be directed to the login page of your MS Teams account.
* **Account Properties**:
  * **JDBC JARs**: The list of JDBC jar files to be loaded. Click the **+** **Add** button to add JDBC Driver as a separate row.
    * **JDBC URL**: Enter the URL of the JDBC database.&#x20;
* **Hostname**: Enter the hostname of the Snowflake server to which you want to connect the new account.
* **Port Number**: Enter the port number associated with the Snowflake database server that you want to use for this account.
* **Database name**: Enter the name of the database to which you want to connect.
* **Warehouse name**: Enter the name of the warehouse to which you want to connect.
* **JDBC Driver Class**: Enter the JDBC driver class to use.
* **Azure storage account name**: Enter the name of the instance of the Azure storage account.
* **Azure storage account key**: Enter the key to connect to the instance of the Azure storage account.&#x20;
* **Container**: Enter the name of the Azure storage blob container that you want to use for hosting files.
* **Path**: Enter the location of the folder in the container where you want to host files.
* **Shared Access Signature (SAS) token method**: Select the method of supplying the SAS token to the endpoint from any of the two options:
  * User Supplied**:** Manually enter the shared access token signature
  * System Generated: Allow endpoint to generate and use the SAS tokens as and when required.
* **User token**: Enter the shared access token that you want to use to access the Azure storage blob folder specified in the Path. You can get a valid SAS token from the Azure portal.
* **Client side encryption**: Select one of the following options to encrypt the blob before uploading to Microsoft Azure:&#x20;
  * None: Indicates that you do not want to use client-side encryption.
  * Custom\_Key: Indicates that you want to use a custom key to access the storage blob.
* **Custom key**: If the _Custom\_Key_ is selected for the **Client side encryption** field, then enter the custom key that you want to use to access the Azure storage blob.
* **Advanced properties**
  * **Url properties**: Click the **+** **Add** icon to add the following URL properties associated with this account.
    * Url property name
    * Url property value
  * **Batch size**: Enter the number of statements to execute at a time.
  * **Fetch size**: Enter the number of rows to fetch at a time when executing a query.
  * **Min pool size**: Enter the minimum number of connections a pool will maintain at a time.
  * **Max pool size**: Enter the maximum number of connections a pool will maintain at a time.
  * **Max life time**: Enter the maximum lifetime of a connection in the pool.
  * **Idle Timeout**: Enter the maximum amount of time a connection is allowed to sit idle in the pool.
  * **Checkout timeout**: Enter the number of milliseconds to wait for a connection to be available when the pool is exhausted.

Click any one of the following:

* **Apply** to save your account information in Flows.
* **Validate** to verify if your account information is valid by connecting Flows with your Redshift account.
* **Cancel** to return to the previous screen.
