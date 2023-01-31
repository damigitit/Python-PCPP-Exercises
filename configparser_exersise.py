"""
Author: Damian Archer
Date: 1/27/2023
File: configparser_exercise.py
Purpose: PCPP Exercises
"""

import configparser

config = configparser.ConfigParser()

# creating messy config file, with both development and
# production environment configurations mixed
config['mariadb'] = {'host': 'localhost',
                     'name': 'hello',
                     'user': 'user',
                     'password': 'password',
                     'env': 'dev'}

config['sentry'] = {'key': 'key',
                    'secret': 'secret',
                    'env': 'prod'}

config['redis'] = {'host': 'localhost',
                   'port': '6379',
                   'db': '0',
                   'env': 'dev'}

config['github'] = {'user': 'user',
                    'password': 'password',
                    'env': 'prod'}

with open('mess.ini', 'w') as configfile:
    config.write(configfile)

# creating new config for development
config = configparser.ConfigParser()

config['mariadb'] = {
    'host': 'localhost',
    'name': 'hello',
    'user': 'user',
    'password': 'password'
}

config['redis'] = {
    'host': 'localhost',
    'port': '6379',
    'db': '0'
}

# write configurations to file
with open('dev_config.ini', 'w') as configfile:
    config.write(configfile)

# creating new config for production
config = configparser.ConfigParser()

config['sentry'] = {
    'key': 'key',
    'secret': 'secret'
    }
    
config['github'] = {
    'user': 'user',
    'password': 'password'
    }
    
with open('prod_config.ini', 'w') as configfile:
    config.write(configfile)
    
config = configparser.ConfigParser()


