#
# Generated __init__.py for compiled model
#

import os
import sys
_this_dir = os.path.dirname(os.path.abspath(__file__))
sys.path += [ os.path.join(_this_dir, "build") ]
sys.path += [ os.path.join(_this_dir, "build", "Release") ]

print("Importing mfcc")
from . import mfcc

__all__ = [mfcc]
