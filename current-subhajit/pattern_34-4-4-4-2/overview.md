# Overview

Use this Pipeline Pattern to synchronize updates from a source Postgres table to a target Postgres table.

Source changes are detected by running a query based on the timestamp. Once changes have been synchronized to the target, the timestamp is stored. Next time the pipeline runs, any changes after that timestamp are retrieved and synchronized.

