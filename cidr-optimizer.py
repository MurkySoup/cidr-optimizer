#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
CIDR List Optimizer, Version 0.3 (Do Not Distribute)
By Rick Pelletier (galigante@gmail.com), 10 June 2025
Last Update: 10 June 2025

Accepts an input file of CIDR's, one per line
Outputs an optimally collapsed list
"""


import sys
import ipaddress
import argparse


def optimize_cidrs(cidrs):
    networks = [ipaddress.ip_network(cidr) for cidr in cidrs]
    optimized_networks = ipaddress.collapse_addresses(networks)

    return [str(network) for network in optimized_networks]


def validate_cidr(cidr):
    try:
        ipaddress.ip_network(cidr)

        return True
    except ValueError:
        return False


def process_file(file_path):
    try:
        with open(file_path, 'r') as file:
            cidrs = file.readlines()

        cidrs = [cidr.strip() for cidr in cidrs if cidr.strip()]
        invalid_cidrs = [cidr for cidr in cidrs if not validate_cidr(cidr)]

        if invalid_cidrs:
            print('Invalid CIDR(s) found')
            print(invalid_cidrs)

            return False

        return optimize_cidrs(cidrs)
    except Exception as e:
        print(f'An error occurred: {e}')

        return False

    return True


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', '-f', type=str, required=True)
    args = parser.parse_args()

    if (optimized_cidrs := process_file(args.file)) is False:
        sys.exit(1)
    else:
        for cidr in optimized_cidrs:
            print(cidr)

    sys.exit(0)
else:
    sys.exit(1)

# end of script
