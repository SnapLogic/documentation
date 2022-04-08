# Requirements

To use this pattern, you need:

* to be able to view the Snap Packs in the Snap Catalog. Otherwise, contact [support@snaplogic.com](mailto:support@snaplogic.com) to be subscribed to the Snap Packs.
* accounts in the following applications with the given minimum permissions (read/write):
  * Salesforce (read)
  * Marketo (write)
* an access token and endpoint URL in the [Pipeline Parameters](https://docs-snaplogic.atlassian.net/l/c/kS2Y1y01).\
  \
  The initial Mapper Snap contains an expression to search for a specific user. You can either replace the ID value every time or define a Pipeline parameter to pass the value in and change the expression to the following:\
  \
  `"Id='" +_SFDC_ID + "'"`\
  \
  where _SFDC\_ID_ is the name of the Pipeline parameter.





