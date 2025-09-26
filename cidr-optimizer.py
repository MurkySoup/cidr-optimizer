#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
CIDR List Optimizer, Version 0.4 (Do Not Distribute)
By Rick Pelletier (galigante@gmail.com), 10 June 2025
Last Update: 26 September 2025

Accepts an input file of CIDR's, one per line
Outputs an optimally collapsed list
"""


import sys
import ipaddress
import argparse


def optimize_cidrs(cidrs) -> list:
    try:
        networks = [ipaddress.ip_network(cidr) for cidr in cidrs]
        optimized_networks = ipaddress.collapse_addresses(networks)

        return [str(network) for network in optimized_networks]
    except (TypeError, ValueError) as e:
        raise RuntimeError(e) from e


def process_file(file_path) -> list:
    try:
        with open(file_path, 'r') as file:
            cidrs = file.readlines()

        cidr_list = [cidr.strip() for cidr in cidrs if cidr.strip()]

        return optimize_cidrs(cidr_list)
    except (OSError, ValueError) as e:
        raise RuntimeError(e) from e


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, required=True)
    args = parser.parse_args()

    try:
        optimized_cidrs = process_file(args.file)
        print(*optimized_cidrs, sep='\n')
    except RuntimeError as e:
        print(e)

        return 1

    return 0


if __name__ == '__main__':
    sys.exit(main())
else:
    sys.exit(1)

# end of script
