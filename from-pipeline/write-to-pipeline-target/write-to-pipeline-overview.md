# Write to Pipeline overview

You can use this target endpoint to execute a flow with the Pipeline created in SnapLogic Intelligent Integration Platform (IIP). Following rules should be adhered to while selecting the Pipeline from Flows.

To select the Pipelines from IIP:

1. Create the Pipeline in the SnapLogic IIP at the project space/shared level.
2. While configuring the account for the Pipeline, select the same shared folder that is selected in Flows to save the Pipeline. If the pipeline is created in any other folder, they are not displayed for the selection in Flows.
3. In Flows, select Write to Pipeline to execute the selected Pipeline. The list of Pipelines from the selected folder is displayed with the appropriate title and description. These details are read from the Pipeline **Purpose** and **Notes** fields respectively. If these fields are not populated, then use the **Label** of the Pipeline.

**Note**: When adding Write to Pipeline to any target endpoint, the respective IIP Pipeline should have an open input view. The Pipeline should not have an open output view, or else it cannot be selected in Flows.

Use the **Map Data** option to apply the mapping between the data of fields uploaded by the source endpoint to the same of the target endpoint.