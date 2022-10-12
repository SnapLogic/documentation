# Overview

Use this Pipeline Pattern to enable or disable an existing task by using the SnapLogic Read and Update Snaps.This pipeline looks for NetSuite Cases in past 24 hours and brings them to ServiceNow. The pipeline attempts to bring the email of the NetSuite user but if none is found, it is defaulted for ServiceNow. Customers may want to use the [NetSuite Contact to ServiceNow User](https://community.snaplogic.com/t/netsuite-contact-to-servicenow-user/4553) pattern in conjunction with this to ensure ServiceNow Users exist for a corresponding NetSuite Contact.
