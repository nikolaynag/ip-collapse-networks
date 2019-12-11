# Get optimized list of networks

Read list of CIDR networks from stdin, collapse multiple small networks into
bigger one and write optimized list of networks to stdout. Based on
`ipaddress.collapse_addresses` library function.

Example:

    $ echo "192.168.0.0/24" > /tmp/input
    $ echo "192.168.1.0/24" >> /tmp/input
    $ ./ip-collapse-nets.py < /tmp/input
    192.168.0.0/23
