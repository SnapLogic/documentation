# Overview

Use this Pipeline Pattern to test if your Cloudplex or Groundplex can access a database on a remote server by pinging the remote host and port.&#x20;

This Pattern Pipeline sets `$post` to 1521 in the Mapper Snap and `$tgt_host` to the host Network Access Protection (NAP) or IP address to test if Oracle can be accessed on a specific server.&#x20;

