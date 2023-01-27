# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

**Important Information about this Pattern**

**Control Table - Tracking**

* The control table contains the source load type such as RDBMS, FTP, API, and others, and the corresponding object name.&#x20;
* Each object load has the load start or end time and the records or documents processed.&#x20;
* For every run, the target table load count is calculated after the source record fetches the count of records.&#x20;
* Based on the status (`S`-success, `F`-failure) of the load, automated notifications are triggered to the concerned team.

**Control Table Attributes:**

* `UID` – Primary key
* `SOURCE_TYPE` – Type of Source RDBMS, API, Social Media, FTP and others.
* `TABLE_NAME` – Table name or object name.
* `START_DATE` – Load start time
* `ENDDATE` – Load end time
* `SRC_REC_COUNT` – Source record count
* `RGT_REC_COUNT` – Target record count
* `STATUS` – `S` for Success and `F` for Failed based on the source or target load

**Partitioned Load**

For every load, the data gets partitioned automatically based on the transaction timestamp in the AWS S3 storage layer.
