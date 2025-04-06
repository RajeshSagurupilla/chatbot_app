import os

def load_config(filepath):
    config = {}
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue  # Skip empty lines and comments
            if "=" in line:
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    return config

# Path to extra.config
config_path = os.path.join(os.path.dirname(__file__), 'development', 'extra.config')
config = load_config(config_path)

# Optional: Set environment variables (if needed)
for key, value in config.items():
    os.environ[key] = value

# Direct access
OPENAI_API_KEY = config.get("OPENAI_API_KEY")
MIXTRAL_API_KEY = config.get("MIXTRAL_API_KEY")
