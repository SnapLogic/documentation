# Requirements

To use this pattern, you need:

* to be able to view the Snap Packs in the Snap Catalog. Otherwise, contact [support@snaplogic.com](mailto:support@snaplogic.com) to be subscribed to the Snap Packs.
* accounts in the following applications with the given minimum permissions (read/write):
  * Marketo API (read)
  * JSON (write)
*   to configure the following Marketo information:



    *   set Service URL to get the OAuth token using the following format:\
        _https://XXX-XXX-XXX.mktorest.com/identity/oauth/token_.


    *   define the following query parameters:&#x20;



        * client\_id
        * client\_secret
        * grant type: set to client\_credentials.
