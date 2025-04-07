import os
import logging
import logging.config
import yaml

# Set logger directory
logDir = os.path.join(os.path.dirname(__file__), '../../logs')
if not os.path.exists(logDir):
    os.makedirs(logDir)

configDir = os.path.join(os.path.dirname(__file__), '../../config/logging_config.yaml')
with open(configDir, 'r') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)

logger = logging.getLogger('app')