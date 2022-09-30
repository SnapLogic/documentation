# Overview

Use this Pipeline Pattern to determine changes between two data files (inserts, updates, deletes, no-changes, older-records-for-updates).

This Pattern is best suited for small to medium files (< 50 million records). For larger files > 5GB or 100 Million records, consider using Spark mode Pipelines for optimal performance.
