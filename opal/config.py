import os
import configparser as cfg # In python 3, this module is changed to configparser
import platform as _platform
from .Platforms import LINUX as platform

def create_default_configuration():
    configuration = cfg.ConfigParser()
    configuration.add_section('SYSTEM')
    configuration.set('SYSTEM','Python','#!/usr/bin/env python')
    return configuration

def read_config():
    if "Linux" in _platform.platform():
        configFile = os.environ['HOME'] + '/.opal/opal.cfg'
    else:
        configFile = os.environ['APPDATA'] + '/.opal/opal.cfg'
    if not os.path.exists(configFile):
        return create_default_configuration()
    configuration = cfg.ConfigParser()
    configuration.read(configFile)
    return configuration

configuration = read_config()
python = configuration.get('SYSTEM','Python')
#paroptRootPackage = 'dev.paropt'
