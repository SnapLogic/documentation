# Select your MongoDB data delivery type

Select any of the following data delivery types to configure this Flow:

* **Insert**: Inserts a document to the database.&#x20;
  * **Database name**: Enter The database where the collection is defined. If not specified, then the MongoDB account database will be used.
  * **Collection name**: Enter the MongoDB collection name to execute the insert command.&#x20;
  * **Batch Size**: Enter the number of documents to be inserted at a time.
* **Update**: Updates one or more documents in a MongoDB collection.&#x20;
  * **Database name**: Enter The database where the collection is defined. If not specified, then the MongoDB account database will be used.
  * **Collection name**: Enter the MongoDB collection name to execute the update command.&#x20;
  * **Update query**: Enter text or expression to evaluate to an object or JSON string. ****&#x20;
* **Delete**: Deletes some or all documents in a MongoDB collection.
  * **Database name**: Enter The database where the collection is defined. If not specified, then the MongoDB account database will be used.
  * **Collection name**: Enter the MongoDB collection name to execute the delete command.&#x20;

Use the **Map Data** option to apply the mapping between the data of fields uploaded by the source endpoint to the same of the target endpoint.
