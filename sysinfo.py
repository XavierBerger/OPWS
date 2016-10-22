# -*- coding: utf-8 -*-

"""
Provides several system information.

System Information
------------------
       Operating System : Windows-10-10.0.10586-SP0
              Processor : Intel64 Family 6 Model 44 Stepping 2, GenuineIntel
 Installed Memory (RAM) : 7.97 GB
       Available Memory : 5.1 GB
            System Type : AMD64
               Hostname : Ganesha
         Python Version : 3.5.1 |Continuum Analytics, Inc. (AMD64)
              User Name : rtogo
"""

import os
import platform
import sys
import psutil
from humansize import format_size

__version__ = '1.0.0'

SYSINFO = [
    '',
    'System Information',
    '------------------',
    '       Operating System : {platform}',
    '              Processor : {processor}',
    ' Installed Memory (RAM) : {installed_memory}',
    '       Available Memory : {available_memory}',
    '            System Type : {machine}',
    '               Hostname : {hostname}',
    '         Python Version : {python}',
    '              User Name : {username}'
]


def getsysinfo():
    """
    Provides several system information.

    Returns
    -------
    str
        The string containing system information.
    """
    sysinfo = os.linesep.join(SYSINFO)
    sysinfo = sysinfo.format(
        platform=platform.platform(),
        processor=platform.processor(),
        installed_memory=format_size(psutil.virtual_memory()[0], binary=True),
        available_memory=format_size(psutil.virtual_memory()[1], binary=True),
        machine=platform.machine(),
        hostname=platform.node(),
        python="".join(sys.version.split('\n')),
        username=os.getlogin())

    return sysinfo
