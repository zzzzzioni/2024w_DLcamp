import argparse
import logging
from utils.command_handler import CommandHandler
from utils.command_parser import CommandParser

# TODO 1-1: Use argparse to parse the command line arguments (verbose and log_file).
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", type=bool, default=False)
parser.add_argument("--log_path", type=str, default='file_explorer.log')
args = parser.parse_args()

verbose = args.verbose
# TODO 1-2: Set up logging and initialize the logger object.
logging.basicConfig(level=logging.INFO, filename=args.log_path, filemode='w',
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    
command_parser = CommandParser(verbose=verbose)
handler = CommandHandler(command_parser)
logger = logging.getLogger(__name__)


while True:
    command = input(">> ")
    handler.execute(command)
    logger.info(f"Input command: {command}")
    
