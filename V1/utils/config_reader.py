import json

class config_reader:
    def read_config_values(filePath):
        with open(filePath) as json_file:
            if json_file:
                json_config = json.load(json_file)
                return (json_config["tenant_id"],
                        json_config["subscription_id"],
                        json_config["resource_group"],
                        json_config["workspace_id"],
                        json_config["workspace_name"])
        return None