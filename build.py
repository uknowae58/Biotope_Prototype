#   -*- coding: utf-8 -*-
from pybuilder.core import use_plugin, init

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")


name = "simple-CI-CD-Python-project"
default_task = "publish","analyze"


@init
def set_properties(project):
    pass
