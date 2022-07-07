# Configure your Snowflake Azure Database account

Configure your Snowflake Azure Database account with the following details:

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
