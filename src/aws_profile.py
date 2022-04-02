import argparse
import pkg_resources
import logging
import os
import configparser

# global logger
logger = logging.getLogger()
logger.setLevel("INFO")

HOME = os.getenv("HOME")
DEFAULT_CONFIG_FILE = os.path.join(HOME, ".aws", "config")


def list_profiles(config_file=None, **kwargs) -> [str]:
    config = configparser.ConfigParser()
    config.read(config_file or DEFAULT_CONFIG_FILE)
    results = list(
        map(
            lambda x: x.replace("profile ", ""),
            filter(lambda x: x.startswith("profile"), config.sections()),
        )
    )
    for result in results:
        print(result)
    return results


def _parse_args():
    parser = argparse.ArgumentParser(description="Manage Aws Profiles")
    # universal arguments
    parser.add_argument(
        "--version",
        action="version",
        version=pkg_resources.get_distribution("aws-profiles").version,
    )
    parser.add_argument(
        "-v", "--verbose", action="store_true", help="print DEBUG output"
    )
    subparsers = parser.add_subparsers(title="operation")

    # list arguments
    list_parser = subparsers.add_parser(name="list", help="list profiles")
    list_parser.add_argument("-c", "--file", help="the config file to parse")
    list_parser.set_defaults(func=list_profiles)

    args = parser.parse_args()
    return parser, args


def main() -> int:
    parser, args = _parse_args()
    if args.verbose:
        logger.setLevel("DEBUG")
    logging.debug(args)
    return 0 if args.func(**vars(args)) else 1


if __name__ == "__main__":
    main()
