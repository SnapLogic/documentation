# Configure a Coupa connection

Create a new connection configuration or select from saved configurations. When available, the list of saved configurations includes:

-   Connection configurations that you created in AutoSync.
-   Accounts that you or an Org admin created in the IIP, including nondynamic Accounts saved in:
    -   The global `shared` folder
    -   The `shared` folder, in the `SL-AutoSyncProjectSpace`
    -   Your AutoSync project, `~User~<username>_<snaplogic_org>`, in the `SL-AutoSync-ProjectSpace`

Create a new connection configuration for Salesforce by entering the following:

-   A unique, meaningful name such as `Coupa-Sales-Shared`. If a configuration with the same name exists, AutoSync displays an `Asset conflict error message`.
-   **Account Properties**:
    -   **API Key**: The API key value. For example, `878f3a94287253678rdcj0cdeb2c71126804fi2`. A Coupa administrator can find this value in Coupa by navigating to **Setup** \> **Integrations** and clicking **API Keys**. Refer to the [Coupa documentation](https://success.coupa.com/Integrate/Technical_Documentation/API/Get_Started/API_Key_Security) for more information.
    -   **Base URL**: The URL for the Coupa homepage. For example, `https://snaplogic-demo.coupacloud.com/`.
-   **Validate and Save**: After saving and validating, AutoSync adds the configuration to the list of saved connections.


