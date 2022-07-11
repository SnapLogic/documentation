# Configure your Snowflake S3 OAuth2 account

Configure your Snowflake S3 OAuth2 account with the following details:

* **Label:** Enter a unique label for the account.
* **Client ID**: Enter the OAuth Client ID (to be used for token request) that you obtain from the Snowflake Console.
* **Client secret**: Enter the OAuth Client secret that you obtain from the Snowflake Console.
* **Access token**: _Auto-generated after authorization._ The access token is used to make API requests on behalf of the user associated with the client ID.
* **Refresh token**: _Auto-generated upon account authorization_. The token used to refresh the access token.
* **Access token expiration**: _Auto-generated upon account authorization_. The number of seconds after which the access token expires.
* **Header authenticated**: Select this checkbox if the endpoint uses bearer header authentication.
* **OAuth2 Endpoint:** Enter the the endpoint in this format _`https://<account_identifier>.snowflakecomputing.com/oauth/authorize`_ to authorize the application.
* **OAuth2 Token:** Enter the the OAuth2 token in this format `https://<account_identifier>.snowflakecomputing.com/oauth/token-request` to get the access token.
* **Token endpoint config**: Enable this if the endpoint uses bearer header authentication. Click the **+ Add** icon on the right of the field to add a row. This field set comprises the following fields:
  * Token endpoint parameter
  * Token endpoint parameter value
* **Auth endpoint config**: Use this field set to assign scopes for the OAuth2 authentication endpoint for the account. It is recommended to define at least one scope entry in this fieldset. Click **+ Add** icon on the right of the field to add a row. This field set comprises the following fields:
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
* **S3 Bucket**: Enter the name of the S3 bucket that you want to use for staging data to Snowflake.
* **S3 Folder**: Enter the relative path to a folder in the S3 bucket listed in the S3 Bucket field.
* **S3 Access-key ID**: Enter the S3 access key ID that you want to use for AWS authentication.
* **S3 Secret key**: Enter the S3 secret key associated with the S3 Access-ID key listed in the S3 Access-key ID field.
* **S3 AWS Token**: Enter the the S3 AWS Token to connect to private and protected Amazon S3 buckets.
* **S3 Storage Integration**: Enter the predefined storage integration that is used to authenticate the Amazon S3 bucket hosting as an external stage.
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
