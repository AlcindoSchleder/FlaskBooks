# -*- coding: utf-8 -*-
import os

COMMON_DIRECTORY = os.path.abspath(os.path.dirname(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIGURE_HASH = os.environ.get(
    "CONFIG_HASH",
    default="b17913cc95df7a21eb8faa3fb55571e70f963f26a613bc72677842033506f32c"
)
