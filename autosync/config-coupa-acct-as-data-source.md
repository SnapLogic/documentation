# Configure a Coupa account as a data source

You can configure a new account source in AutoSync by using the user credentials from your existing Coupa account.

1.  Click **Configure new credentials** to create new credentials.

    Alternatively, you can click **Use existing credentials** and select the credentials from the **Select Existing Connection** dropdown.

2.  In **Create new connection tag**, enter a unique name that will help identify your account in AutoSync.

    We recommend that you use an easily recallable or relatable name.

3.  In **API Key**, enter the API key value of your Coupa account.

    For example, `878f3a94287253678rdcj0cdeb2c71126804fi2`. Your IT admin can find this value in Coupa by navigating to [**Setup** \> **Integrations** and clicking **API Keys**](https://success.coupa.com/Integrate/Technical_Documentation/API/Get_Started/API_Key_Security).

4.  In **Base URL**, enter the main URL of your Coupa account.

    For example, `https://snaplogic-demo.coupacloud.com/`. To find this value, log in to your Coupa account and use the URL of your homepage.

5.  Click **Validate and Save**.

    If your account successfully validates, it is added to the **Select existing connection** drop-down list. The new source is displayed in the **Select Source** box of the integration workflow on the right side of the integration page.

    **Note:** If an asset with the same name exists, an `Asset conflict error message` is displayed. Multiple attempts with invalid credentials could lock your account.


