# Configure Redshift SSL Account

Configure your Redshift SSL account with the following details:

* **Label:** Enter a unique user-provided label for the account.&#x20;
* **JDBC Driver Class**: Enter the name of the JBDC driver class to use, like _org.postgresql.Driver._&#x20;
* **JDBC JARs**: The list of JDBC jar files to be loaded. Click the **+** **Add** button to add JDBC Driver as a separate row.
  * **JDBC URL**: Enter the URL of the JDBC database, like _jdbc:redshift://hostname:port/database._
* **Account properties**: Enter the information to create a connection to the database.
  * **Endpoint**: Enter the server's address.
  * **Port Number**: Enter th_e_ database server's port.
  * **Database name**: Enter the database name.&#x20;
  * **Username**: Enter the username to connect to the database.
  * **Password**: Enter the password used to connect to the database.
  * **S3 Bucket**: Enter the external S3 Bucket name residing in an external AWS account, to use for staging data onto Redshift.
  * **S3 Folder**: Enter the relative path to a folder in S3 Bucket.
  * **S3 Access-key ID**: Enter the S3 Access key ID part of AWS authentication.
  * **S3 Secret key**: Enter the S3 Secret key part of AWS Authentication.
  * **TrustStore**: Enter the location of the TrustSstore file.
  * **TrustStore Password**: Enter the password for the TrustStore file.
* **IAM properties (Redshift Cluster)**: the IAM properties information for Redshift to communicate with IAM**.**
  * **AWS account ID**: Enter the ID of the Amazon Web Services account to be used for performing bulk load operation.
  * **IAM role name**: Enter the name of the IAM role that has been assigned to the Redshift cluster to access the S3 bucket.
  * **Region name**: Enter the name of the region the Redshift cluster.
* **Advanced properties**: The advanced properties to support this account.
  * **Auto commit**: Select this checkbox to enable the Flow to commit offsets automatically.
  * **Batch size**: Enter the number of statements to execute at a time.
  * **Fetch size**: Enter the number of rows to fetch at a time when executing a query.
  * **Max pool size**: Enter the maximum number of connections a pool will maintain at a time.
  * **Max life time**: Enter the maximum lifetime of a connection in the pool.
  * **Idle Timeout**: Enter the maximum amount of time a connection is allowed to sit idle in the pool.
  * **Checkout timeout**: Enter the number of milliseconds to wait for a connection to be available when the pool is exhausted.
* **Url properties**: Click the **+** **Add** icon to add the following URL properties associated with this account.
  * Url property name
  * Url property value
* Click any one of the following:
  * **Apply** to save your account information in Flows.
  * **Validate** to verify if your account information is valid by connecting Flows with your Redshift account.
  * **Cancel** to return to the previous screen
