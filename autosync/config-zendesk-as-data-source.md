# Configure a connection to Zendesk

## Limitations

After creating an account, in Step 2 you will select the objects to synchronize and in Step 3 you will choose a synchronization method. Be aware of the following limitations:

-   You can only synchronize the `audit_log` object if you have a Zendesk Enterprise Suite account.
-   If the voice feature is not enabled, you cannot synchronize the following objects:
    -   `line`
    -   `greeting`
    -   `greeting_category`
    -   `ivr`
    -   `call`
    -   `call_leg`
-   The upsert and SCD2 synchronization types cannot track changes for the `line`, `greeting`, `greeting_category`, `address`, and `ivr` objects because Zendesk does not provide timestamps for them.

Create a new connection configuration for Zendesk by entering the following:

-   A unique, meaningful name such as `Zendesk-Shared`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Token**: Zendesk administrators generate and provide the API Token from the Zendesk Admin center. A token must be in the following format: \(email\)/token:\(api\_token\). Refer to the Zendesk documentation for more information.
-   **Save**: After saving, AutoSync adds the connection configuration to the dropdown list of existing connections.
-   **Domain**: The domain is the URL used to connect to Zendesk. For example, *https://subdomain.zendesk.com*.

