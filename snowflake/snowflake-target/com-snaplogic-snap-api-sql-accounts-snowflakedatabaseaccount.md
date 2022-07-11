# Configure your Snowflake S3 Database account



Configure your Snowflake S3 Database account with the following details:

* **Label:** Enter a unique label for the account.&#x20;
* **Account Properties**:
  * **JDBC JARs**: The list of JDBC jar files to be loaded. Click the **+** **Add** button to add JDBC Driver as a separate row.
    * **JDBC URL**: Enter the URL of the JDBC database.&#x20;
* **Hostname**: Enter the hostname of the Snowflake server to which you want to connect the new account.
* **Port Number**: Enter the port number associated with the Snowflake database server that you want to use for this account.
* **Authentication Type**: Select the authentication type that you want to use with this account.
* **Username**: Enter the username that you want to use to connect to the database server.
* **Password**: Enter the password associated with the username.
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
