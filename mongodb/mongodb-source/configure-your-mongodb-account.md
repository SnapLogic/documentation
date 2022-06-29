# Configure your MongoDB account

For the MongoDB account, configure your account with the following details:

* **Label:** Enter a unique label for the account.
* **Hostname**: Enter the MongoDB Hostname.&#x20;
* **Port**: Enter the MongoDB Port.
* MongoDB JARs:&#x20;
  * Database name: Enter the database that the MongoDB account is defined in. This is also the default database used for queries.
  * Username: Enter the MongoDB Username.
  * Password: Enter the password associated with the MongoDB Username.
  * Authentication type: Select the authentication type that you want to use with this account.
  * Encryption type: Select the encryption type for connecting Mongo instance.
* SSL certs properties: The required Keystore and Truststore properties only when the encryption type is selected as _SSL certs_.
  * **Truststore filepath**: Enter the location of the Truststore file in PKCS#12 format.
  * **Truststore password**: Enter the Truststore password to access the Truststore file of the server.
  * **Keystore filepath**: Enter the location of the Keystore file in PKCS#12 format.&#x20;
  * **Keystore file password**: Enter the Keystore password to access the Keystore file of the client.
* **Connection properties**: Connection properties to specify connection and server selection timeouts.
  * **Connection timeout (seconds)**: Set the number of seconds the Mongo driver waits before aborting a new connection attempt.
  * **Server Selection timeout (seconds)**: Set the number of seconds the Mongo driver waits to select a server for an operation before aborting the selection.
* **MongoDB cursor properties**:&#x20;
  * **Use Cursor Timeout**: Select this checkbox to set a timeout for idle cursors, which means, it enables the server to close a cursor automatically after a period of inactivity.
* Click any one of the following:
  * **Apply** to save your account information in Flows.
  * **Validate** to verify if your account information is valid by connecting Flows with your Redshift account.
  * **Cancel** to return to the previous screen.
