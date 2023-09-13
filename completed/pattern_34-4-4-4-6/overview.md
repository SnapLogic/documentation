# Overview

Use this Pipeline Pattern to synchronize updates from a source PostgreSQL table to a target PostgreSQL table.

Source changes are detected by running a query based on the time stamp. After changes are synchronized to the target, the time stamp is stored. Next time the Pipeline runs, any changes after that time stamp are retrieved and synchronized.

