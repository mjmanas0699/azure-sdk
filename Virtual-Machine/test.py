from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute import ComputeManagementClient
import os
creds=AzureCliCredential()
subscription_id="8c11b217-12d8-4862-a0e5-4f4065f840b9"
r_client=ResourceManagementClient(creds,subscription_id)
LOCATION="centralindia"
RESOURCE_GRP_NAME="from-python"
VNET_NAME="from-python-vnet"
r_group=r_client.resource_groups.create_or_update(RESOURCE_GRP_NAME,{
                                                    "location": LOCATION 
                                                  })
network_client=NetworkManagementClient(subscription_id,creds)
vnet_resource=network_client.virtual_networks.begin_create_or_update(RESOURCE_GRP_NAME,VNET_NAME,{
  "location": LOCATION,
    "address_space": {
      "address_prefixes": ["10.0.0.0/16"]
    }
})
