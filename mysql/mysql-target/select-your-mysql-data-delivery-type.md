# Select your MySQL data delivery type

Select any of the following data delivery types to configure this Flow:

* **Insert**: Executes a SQL INSERT statement on the selected table.&#x20;
  * **Table Name**: Enter the name of the table to execute an insert query.
  * **Use MySQL INSERT IGNORE option**: Select _Ignore_ to insert null values into MySQL when it receives invalid data. Select _Fail_ to ensure that all data validation errors are caught in the error view.
* **Update**: Executes a SQL update with the given properties.
  * **Table Name**: Enter the name of the table to execute the update.&#x20;
* **Delete**: Executes a SQL delete with the given properties.
  * **Table Name**: Enter the name of the table to execute the delete.&#x20;

Use the **Map Data** option to apply the mapping between the data of fields uploaded by the source endpoint to the same of the target endpoint.
