#!/usr/bin/env python3
# coding: utf-8

import argparse

from loguru import logger
from rich import print
from rich.traceback import install

# save runtime logs to file
logger.add("runtime.log", level="DEBUG")

# rich.traceback
install(show_locals=True)


############################################################
async def main():
    '''The main function'''
    pass



############################################################
def cli_params() -> None:
    '''Get parameters that are passed through from the command line upon execution.'''

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", "-v", required=False, action='store_true',
                        help="""Make verbose outputs on stdout (same function as verbose).""", )

    parser.add_argument("--dry", "--dry-run", required=False, action='store_true',
                        help="""Dry run only, do not write/execute anything.""", )

    parser.add_argument("-i", "--input", type=str, required=False,
                        help="""Some input string.""", )

    # args = parser.parse_args(args=["--debug"])  ## within the jupyter notebook
    args = parser.parse_args()  # this is for production runs

    if args.debug:
        logger.debug(f"ARGS: {args}")

    return (args)


############################################################
if __name__ == "__main__":
    asyncio.run(main())
