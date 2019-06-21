import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(name)4s: %(filename)s %(funcName)s %(levelname)8s: %(message)s',
                    handlers=[logging.FileHandler("test.log", "a"), logging.StreamHandler()])

# Now, we can log to the root logger, or any other logger. First the root...
logging.info('Jackdaws love my big sphinx of quartz.')

# Now, define a couple of other loggers which might represent areas in your
# application:
logger1 = logging.getLogger('log1')
logger2 = logging.getLogger('log2')

logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')