# Uploading CSV files as a source

You can use comma-delimited CSV files as a source for an integration. AutoSync loads each source file to its own destination table with columns of type `Varchar`.

AutoSync trims leading and trailing spaces from the source. Source files must use quotes to bracket meaningful spaces and commas that are part of a field value. For example, in a source that lists vehicles where the header specifies `year`, `make`, `model`, and `description` columns, the quotes preserve the comma in the description column: `1997, Ford, E350, "Extended cab, luxury truck"`.

Each .csv file must:

-   Have a header
-   Be uncompressed
-   Be less than 100 MB in size
-   Use a single comma delimiter
-   Use quotes to bracket fields that include commas in the value

After you select the files to upload, AutoSync loads them into SnapLogic file storage. After you save the integration, AutoSync loads the data to the destination and deletes the files from SnapLogic storage. You can reuse the integration later by selecting different files.

