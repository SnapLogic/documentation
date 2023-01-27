# Overview

Use this Pipeline Pattern to create an API that accepts the email ID of a user as input and returns the list of project folders in SnapLogic to which the user has Read, Write and Execute (RWX) permissions. If the user doesn’t have full access to any of the folders, the Pipeline returns an empty array list.

This Pattern helps to maintain governance by verifying the access level information for each user.

