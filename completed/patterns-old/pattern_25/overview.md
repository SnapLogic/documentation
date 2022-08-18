# Overview

Use this Pipeline Pattern to create Box folders for ServiceNow Service Requests. For a service request created in ServiceNow, SnapLogic checks if a Box folder named with the ServiceNow request’s number exists.&#x20;

If the folder doesn’t exist, SnapLogic creates a new Box folder and names it with the ServiceNow request’s number. SnapLogic also creates a shared link to the newly created Box folder.
