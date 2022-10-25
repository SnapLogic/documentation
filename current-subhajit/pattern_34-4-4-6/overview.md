# Overview

Use this Pipeline Pattern to read the summary of Pipeline executions, load the line detail into a file, and write the summary of execution into another file.&#x20;

This pipeline uses the following methods:

* Use the iteration feature of the REST Get Snap so that the multiple iterative requests required to retrieve the detail from the SnapLogic Public APIs are consumed.
* Dynamically configure the URLs used with the ternary operator(expression language).
* Use an expression to get the org name used in the URLs.
* Place multiple different format data into a single output stream with an implication of order.&#x20;
