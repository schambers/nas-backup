import os
import rclone
from os.path import expanduser
import logging

# Enabled verbose logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(name)s [%(levelname)s]: %(message)s")

#cfg = """[local]
#type = local
#nounc = true"""

with open(expanduser('./rclone.conf')) as config_file:
    config = config_file.read()


# List all top level folders with run_cmd
#result = rclone.with_config(config).run_cmd(command="lsd", extra_args=["remote:"])

# List top level folders using ls
#result = rclone.with_config(config).ls("remote:")

# Copy README.md to root to test
source = "./README.md"
result = rclone.with_config(config).copy(source, "remote:backup-test")
print(result.get('out'))

# Perform sync

