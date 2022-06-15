# Select your SharePoint Online data source type

Select any one of the following **Data Source Types** to start your Flow and provide the following information:

* **Create Folder**: Select this data delivery type to create a folder both in a SharePoint Online document library and within another item of type folder.
  * **Site**: The name of a site that contains the list of document libraries to be used in the subsequent Snap settings.
  * **Document library**: Select the drive representing the top-level container for the system such as Onedrive or Sharepoint document libraries.
  * **Folder Name**: The folder name to be used to create the folder.
* **Create Item Permission**: Select this data delivery type to create ad share invitations for an item to the configured set of recipients.
  * **Site**: The name of a site that contains the list of document libraries to be used in the subsequent Snap settings.
  * **Document library**: Select the drive representing the top-level container for the system such as Onedrive or Sharepoint document libraries.
  * **Source item relative path**: Enter the item resource path that represents a file, folder, or other item stored in a document library to get the available permissions on the item.
  * **Roles**: Specify the roles that are to be granted to the recipients of the invitation.
  * **Recipients**: Enter the comma-separated recipients who will receive access and the sharing invitation to the selected item.
* **Create List:** Select this data delivery type to create a list or list item in SharePoint Online.
  * **Site**: The name of a site that contains the list of document libraries to be used in the subsequent Snap settings.
  * **List name**: Select the name of the list.
* **Copy Item**: Select the data delivery type to copy the item resource path that represents a folder or file stored in a document library and update a name or move an item.
  * **Site**: The name of a site that contains the list of document libraries to be used in the subsequent Snap settings.
  * **Document library**: Select the drive representing the top-level container for the system such as Onedrive or Sharepoint document libraries.
  * **Source item relative path:** Enter the item resource path that represents a file, folder, or other item stored in a document library to get the available permissions on the item.
* **Update Item**: Select the data delivery type to update the item resource path that represents a folder or file stored in a document library and update a name or move an item.
  * **Site**: The name of a site that contains the list of document libraries to be used in the subsequent Snap settings.
  * **Document library**: Select the drive representing the top-level container for the system such as Onedrive or Sharepoint document libraries.
  * **Source item relative path:** Enter the item resource path that represents a file, folder, or other item stored in a document library to get the available permissions on the item.
* **Update Item Permission:** Select this data delivery type to update item permission associated with an item/folder of the SharePoint Online document library.
* **Update List Item**: Select this data delivery type to update the values of an existing list item in a SharePoint Online site.
* **Delete Item**: Select this data delivery type to delete items from the SharePoint Online document library.
  * **Site**: The name of a site that contains the list of document libraries to be used in the subsequent Snap settings.
  * **Document library**: Select the drive representing the top-level container for the system such as Onedrive or Sharepoint document libraries.
  * **Source item relative path**: Enter the item resource path that represents a file, folder, or other item stored in a document library to get the available permissions on the item.
* **Delete Item Permission**: Select this data delivery type to delete the permission of an item from the SharePoint Online document library.
  * **Site**: The name of a site that contains the list of document libraries to be used in the subsequent Snap settings.
  * **Document library**: Select the drive representing the top-level container for the system such as Onedrive or Sharepoint document libraries.
  * **Source item relative path:** Enter the item resource path that represents a file, folder, or other item stored in a document library to get the available permissions on the item.
  * **PermissionId**: Select the permission id from the drop-down list associated with an item selected in the Source file path property.
* **Delete List Item**: Select this data delivery type to delete a list item from the the SharePoint Online document library.
  * **Site**: The name of a site that contains the list of document libraries to be used in the subsequent Snap settings.
  * **List name**: Select the name of the list.
  * **Item Id**: Select or enter the item id to delete the list item.

Use the **Map Data** option to apply the mapping between fields uploaded by the source endpoint to the same of the target endpoint.

Click **Save and continue**