import json

class config_reader:
    def read_config_values(filePath):
        with open(filePath) as json_file:
            if json_file:
                json_config = json.load(json_file)
                return (json_config["cc_tenant_id"],
                        json_config["cc_subscription_id"],
                        json_config["cc_resource_group"],
                        json_config["cc_workspace_id"],
                        json_config["cc_workspace_name"])
        return None