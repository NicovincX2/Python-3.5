#-*- coding: utf-8 -*-

from pip import get_installed_distributions
from pip.commands import install
import os

install_cmd = install.InstallCommand()

options, args = install_cmd.parse_args([package.project_name
                                        for package in
                                        get_installed_distributions()])

options.upgrade = True
install_cmd.run(options, args)  # Chuck this in a try/except and print as wanted

os.system("pause")
