import yaml


def change_origin_to_yaml(file_path):
    # Step 1: Read the existing YAML data
    with open(file_path, "r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    # Step 2: Add the new attribute to the data
    data["mixed-port"] = 10890
    data["external-controller"] = "127.0.0.1:10090"
    data["secret"] = ""
    data["external-ui"] = "ui"
    if 'enhanced-mode' in data['dns']:
        del data['dns']['enhanced-mode']
    # Step 3: Write the updated data back to the same file
    with open(file_path, "w", encoding="utf-8") as file:
        yaml.dump(
            data,
            file,
            allow_unicode=True,
            default_flow_style=False,
            sort_keys=False,
        )


# Example usage:
file_path = "config.yaml"
if __name__ == "__main__":
    change_origin_to_yaml(file_path)
