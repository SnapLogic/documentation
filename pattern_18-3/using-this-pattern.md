# Using this Pattern

**Steps**

1. Click **Use Pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the pattern.
3. Click the pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

If the Pipeline runs successfully, you can view the output. For more information, read this article: [My First Pipeline](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/1438412).

**How to Configure the Pipeline**

* Define the following fields as Pipeline parameters
  * URL: the REST API URL for your Marketo instance, like: https://xxx-xxx-xxx.mktorest.com 7
  * clientID: The clientID for API access.
  * clientKey: The client secret for API access.
* to configure the REST Get Snap (labeled Marketo Login in this Pipeline):
  * For Service URL, toggle on the Expression button ( = ) and set the field to:\
    `_url + '/identity/oauth/token?grant_type=client_credentials&client_id=' + _clientID + '&client_secret=' +_clientKey`
  * Remove the input view.
  * Validate the Snap to return a response that contains an access\_token and scope.
* Use the access token in subsequent Snaps to pass as a header, rather than a query parameter because it simplifies paged operations such as Get Lead Changes.\
  Here's an example of a simple call:
  * For the Service URL, toggle on the Expression button ( = ) and set the field to the following:\
    `_url + '/rest/v1/activities/types.json'`
  * Under HTTP Header, set the Key to Authorization and Value with the Expression button ( = ) toggled on to `'Bearer ' + $accessToken`.

**Additional Considerations**

For more complex operations, such as getting lead changes, you need to make two API calls: the first creates a paging token, and the second uses the paging token typically with the paging mechanism enabled in the REST GET Snap.

**Get Paging Token**

Get Paging Token In this REST GET Snap (renamed _Get Paging Token_ for clarity), where you specify the query parameters.

For instance, if you want to get lead changes since a particular date, you'd pass that in via "sinceDateTime". The example provided uses a literal string but could be a pipeline parameter or ideally one of the Date objects formatted to match what Marketo expects.

`_url + '/rest/v1/activities/pagingtoken.json'`

**Configure Paging Mechanism**

When calling Get Leads (through a REST GET Snap), a few things to `consider`:

* You need to pass "nextPageToken" as a query parameter, along with the fields you want back. Ideally, the list of fields should be in a Pipeline Parameter because they appear twice in this configuration.
* The leads will be returned in `$entity.result`, which is an array. This field will not exist if there are no results, so you need to enable "Null safe" on a Splitter Snap after this REST Get.
* Paging expressions for the REST Get Snap are:
  * Has next:\
    `$entity.moreResult == true Next URL: '%s/rest/v1/activities/leadchanges.json?`
  * nextPage:\
    `Token=%s&fields=firstName,lastName'.sprintf( _url, $entity.nextPageToken )`

**API Throttling Marketo throttles API calls**

If the Marketo API throttling limits to 100 API calls in a 20-second window, then configure the REST Snap option to wait for _X_ seconds or milliseconds between requests for retrieving paginated results.
