"""settings"""
from .. import envs

if envs.MODE.lower() == 'dev':
    from .dev import *
else:
    from .prod import *