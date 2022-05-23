# Requirements

To use this pattern, you need:

* to be able to view the Snap Packs in the Snap Catalog. Otherwise, contact [support@snaplogic.com](mailto:support@snaplogic.com) to be subscribed to the Snap Packs.
* accounts in the following applications with the given minimum permissions (read/write):
  * Pipeline runtime details from the Pipeline Monitoring API (read). Getting all Pipeline details for an Org requires Org admin access.
  * Email (write)
* to configure the Pipeline details to include in the email:
  * CustomerOrg: The name of the Org where we are getting Pipeline executed information.
  * [Pipeline Monitoring API](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/1438155/Pipeline+Monitoring+API): The public API to get Pipeline details.
  * To: A list of receivers in the email.
  * Authorization: An account to access the Pipeline execution information.

