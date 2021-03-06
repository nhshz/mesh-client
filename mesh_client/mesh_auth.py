#!/usr/bin/env python
from __future__ import print_function
from mesh_client import _AuthTokenGenerator
from argparse import ArgumentParser


def main():
    parser = ArgumentParser(description="Create MESH auth token for user")
    parser.add_argument('user', help="The username")
    parser.add_argument('password', help="The password for the user")
    parser.add_argument('--shared-key', help="The shared key to use - ask Spine for this")
    args = parser.parse_args()
    generator = _AuthTokenGenerator(args.shared_key, args.user, args.password)
    print(generator())


if __name__ == '__main__':
    main()
