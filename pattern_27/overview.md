# Overview

Use this Pipeline Pattern to send an email containing a link to an empty ServiceNow request. For an empty request created in ServiceNow, SnapLogic sends an email containing a link to the ticket to a manager. The manager then fills in the ticket details and submits it.

A separate triggered task needs to be created if Active Directory or a designated database is the central place to host all employees. With the additional triggered task, when a new employee is added to Active Directory or the designated database, SnapLogic will create a request in ServiceNow using this pipeline.
