# Overview

Use this Pipeline Pattern to search for active users in Workday that are updated in the last two hours and fetch the employee files into their corresponding sub-folders using the file structure created in Box.

The parent directory for employee files is divided into two folders: Active and Terminated. Under each sub-folder is a series of other sub-folders from A to Z (representing the first letter of the surname of each employee).&#x20;

Therefore, the employee file folder is found in the appropriate alphabetical sub-folder with a naming convention such as `EmployeeID_LastName_FirstName`. Additional sub-folders are created in each employee folder, each representing a functional category of documents that the HR unit may want to capture, such as performance, expenses, and training.





