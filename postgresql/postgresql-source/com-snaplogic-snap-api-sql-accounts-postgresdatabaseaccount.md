# Configure your Postgres account

For the Postgres account, configure your account with the following details:

* **Label:** Enter a unique label for the account.
* **Account properties**: Enter the information to create a connection to the database.
  * **Hostname**: Enter the server's address.
  * **Port Number**: Enter th_e_ database server's port.
  * **Database name**: Enter the database name.&#x20;
  * **Username**: Enter the username to connect to the database.
  * **Password**: Enter the password used to connect to the database.
  * **JDBC JARs**: List of JDBC JAR files to be loaded. Click **+** **Add** icon on the right of the field to add a row.
    * **JDBC Driver**: The software component enabling an application to interact with a database.
  * **JDBC Driver Class**: The class name of the JBDC driver.
* **Advanced propertie**s: The advanced properties to support this account.
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
  * **Validate** to verify if your account information is valid by connecting Flows with your SQL Server account.
  * **Cancel** to return to the previous screen.
