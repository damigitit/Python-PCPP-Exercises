"""
Author: Damian Archer
Date: 1/26/2023
File: logger.py
Purpose: PCPP Exercise
"""

import logging
import random

logger = logging.getLogger(__name__)
handler = logging.FileHandler('battery_temperature.log', mode='w')

FORMAT = '%(name)s:%(levelname)s:%(asctime)s:%(message)s'
formatter = logging.Formatter(FORMAT)
handler.setFormatter(formatter)

logger.setLevel(logging.DEBUG)
logger.addHandler(handler)

temps = [random.randrange(20,40) for i in range(60)]

for TEMPERATURE_IN_CELSIUS in temps:
    
    DEBUG = TEMPERATURE_IN_CELSIUS < 20
    WARNING = TEMPERATURE_IN_CELSIUS >= 30 and TEMPERATURE_IN_CELSIUS <= 35
    CRITICAL = TEMPERATURE_IN_CELSIUS > 35
    if DEBUG:
        logger.debug('This phone battery temperature is lower than expected.')
    elif WARNING:
        logger.warning('Warning, this phone battery is a little bit warm.')
    elif CRITICAL:
        logger.critical('This phone battery is way too hot!')
    else:
        logger.info('Temperature is in an appropriate range')

    
        
        
    
