# Overview

Use this Pipeline Pattern to read a CSV file and write the data into a Workday tenant.&#x20;

This pipeline reads a CSV file, parses the content, and then the Workday Write Snap is used to call the web service operation Put\_Applicant to write the data into a Workday tenant.
