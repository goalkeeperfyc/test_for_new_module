import argparse
import logging

# logging.basicConfig(filename="test.log", format=" %(asctime)s %(message)s", level=logging.DEBUG)

function_name = "test_function_name"

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    filename='test.log',
                    filemode='a')

console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger().addHandler(console)


logging.info("This is info level log")
logging.warning("This is warning level log")