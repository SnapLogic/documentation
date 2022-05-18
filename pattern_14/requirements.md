# Requirements

To use this pattern, you need:

* to be able to view the Snap Packs in the Snap Catalog. Otherwise, contact [support@snaplogic.com](mailto:support@snaplogic.com) to be subscribed to the Snap Packs.
* accounts in the following applications with the given minimum permissions (read/write):
  * Active Directory User Object Class (read)
  * REST call return (write)
* For configuring the Pipeline:
  * enter the base DN to look for users with the “baseDn" parameter.&#x20;
  * enter the AD username in the “filterUser” parameter.&#x20;
  * assign to a Triggered Task and call with the REST API. Alternatively, run as a child Pipeline called with a Pipeline Execute Snap that is part of an orchestrator Pipeline.
