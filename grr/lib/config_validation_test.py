#!/usr/bin/env python
"""Tests for validating the configs we have."""

import glob
import os

import logging

from grr.lib import config_lib
from grr.lib import config_testing_lib
from grr.lib import flags
from grr.lib import test_lib


class BuildConfigTests(config_testing_lib.BuildConfigTestsBase):

  def testAllConfigs(self):
    """Go through all our config files looking for errors."""
    # Test the current loaded configuration.
    configs = [config_lib.CONFIG]

    # Test all the other configs in the server config dir (/etc/grr by default)
    glob_path = os.path.join(config_lib.CONFIG["Config.directory"], "*.yaml")
    for cfg_file in glob.glob(glob_path):
      if os.access(cfg_file, os.R_OK):
        configs.append(cfg_file)
      else:
        logging.info("Skipping checking %s, you probably need to be root",
                     cfg_file)

    self.ValidateConfigs(configs)


def main(argv):
  test_lib.GrrTestProgram(argv=argv)


if __name__ == "__main__":
  flags.StartMain(main)
