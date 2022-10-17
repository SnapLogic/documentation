# Overview

Use this Pipeline Pattern to load a large number of small files as a sequence file with the metadata of each of those files into any target locations like S3, WASB, ADL, HDFS, SFTP, and other protocols.

This Pattern is useful If you have a number of small files on SPTP, S3, HDFS, or Kafka relating to a certain event, such as small files generated in an hour, and want to store them and their metadata in a larger file for efficient storage.&#x20;
