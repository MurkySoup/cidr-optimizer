# CIDR Ooptimizer
Accepts an input file of CIDR's, one per line and outputs an optimally collapsed list

# Prerequisites

This script uses the following modules:
* sys
* ipaddress
* argparse

# Example Usage:

```
usage: cidr-optimizer.py [-h] --file FILE

options:
  -h, --help            show this help message and exit
  --file FILE, -f FILE
```

Sample input:
```
192.168.1.0/26
192.168.1.64/27
192.168.1.96/27
10.1.0.0/26
10.1.0.64/26
```

Sample output:
```
10.1.0.0/25
192.168.1.0/25
```

# Signalling

Standard *nix-style messaging and exit codes apply:
* Exits with code '0' for success.
* Exits with code '1' for failure.

# License

This tool is released under the Apache 3.0 license. See the LICENSE file in this repo for details.

# Built With

* [Python](https://www.python.org) designed by Guido van Rossum

## Author

**Rick Pelletier**
