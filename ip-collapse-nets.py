#!/usr/bin/env python3
import sys
import ipaddress

if sys.version_info < (3, 3):
    sys.stderr.write(
        "Sorry, this script could not run with Python {}.{}, "
        "Python 3.3 or higher is required\n".format(*sys.version_info))
    sys.exit(1)


def main():
    networks = (
        ipaddress.ip_network(line.strip(), False)
        for line in sys.stdin
    )
    for net in ipaddress.collapse_addresses(networks):
        sys.stdout.write(str(net) + "\n")


if __name__ == "__main__":
    main()
