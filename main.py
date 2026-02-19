#!/usr/bin/env python3
# coding: utf-8

import asyncio

from argparse import ArgumentParser, Namespace
from loguru import logger
from rich import print
from rich.traceback import install
from dotenv import dotenv_values

# save runtime logs to file
logger.add("runtime.log", level="DEBUG", rotation="9MB")

# rich.traceback
install(show_locals=True)
cfg = {**dotenv_values()}


############################################################
async def main(params):
    '''The main function'''
    pass



############################################################
def cli_params() -> Namespace:
    '''Get parameters that are passed through from the command line upon execution.'''

    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--debug", "-v", required=False, action='store_true',
                        help="""Make verbose outputs on stdout (same function as verbose).""", )

    parser.add_argument("--dry", "--dry-run", required=False, action='store_true',
                        help="""Dry run only, do not write/execute anything.""", )

    parser.add_argument("-i", "--input", type=str, required=False,
                        help="""Some input string.""", )

    # params = parser.parse_args(params=["--debug"])  ## within the jupyter notebook
    params = parser.parse_args()  # this is for production runs

    if params.debug:
        logger.debug(f"ARGS: {params}")

    return (params)


############################################################
if __name__ == "__main__":
    params = cli_params()
    asyncio.run(main(params))
