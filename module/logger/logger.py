import os
import logging
import logging.config
import yaml

# Set logger directory
if not os.path.exists('logs'):
    os.makedirs('logs')

with open('config/logging_config.yaml', 'r') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

logger = logging.getLogger('mainapi')