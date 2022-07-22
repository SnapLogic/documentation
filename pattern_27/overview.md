# Overview

SnapLogic creates an empty request in ServiceNow, then SnapLogic sends an email containing a link to the ticket to manager. The manager then fills in the details for the ticket and submits it.

A separate triggered task needs to be created if Active Directory or a designated database is the central place to host all employees. With the additional triggered task, when a new employee is added to Active Directory or a designated database, then SnapLogic will create a request in ServiceNow using this pipeline.

Use this Pipeline Pattern to create Box folders for ServiceNow Service Requests. For a service request created in ServiceNow, SnapLogic checks if a Box folder named with the ServiceNow request’s number exists.&#x20;

If the folder doesn’t exist, SnapLogic creates a new Box folder and names it with the ServiceNow request’s number. SnapLogic also creates a shared link to the newly created Box folder.
