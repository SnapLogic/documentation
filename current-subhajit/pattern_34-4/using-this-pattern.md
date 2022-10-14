# Using this Pattern

**Steps**

1. Click **Use pattern** and select the Project space you want to save the Pipeline in.
2. In **Designer**, click the Pipelines icon on the left panel and browse to the location where you saved the Pattern.
3. Click the Pattern to launch it as a Pipeline.
4. Configure your account in SnapLogic using the account information in the original application.
5. Open each Snap and configure the **Settings** per your requirements.
6. Save the Snap/Pipeline, validate, and run it.

If the Pipeline runs successfully, you can view the output. For more information, read this article: [My First Pipeline](https://docs-snaplogic.atlassian.net/wiki/spaces/SD/pages/1438412).

**How to Configure the Pipeline**

Set the following parameters **** for the Pipeline:

* **emailTo:** Receiver of the email
* **emailFrom:** Sender of the email
* **JIRAurl:** the URL for your instance of JIRA. Example: [https://company.atlassian.net](https://company.atlassian.net/)
* **projects:** the JIRA projects you want to query as part of the JQL query in the JIRA Search Snap. The query is set up to search multiple projects, for example, projects in (ABC,DEF,GHI). Refer to JIRA’s [Advanced Searching](https://confluence.atlassian.com/jirasoftwarecloud/advanced-searching-764478330.html) documentation to know about how to change this query.

The information sent in the email includes: Key (sent to be a link to the issue in JIRA), Issue Type, Title, Priority, Submitter, Status, and Assignee.
