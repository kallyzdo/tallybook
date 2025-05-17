#!/usr/bin/env python3
import argparse
from tallybook.parsers import add, unadd, check, uncheck, show_calendar, list_habits
from datetime import date

def main():

    # creating the main parser
    parser = argparse.ArgumentParser(prog="tb")

    # adding subparsers
    subparsers = parser.add_subparsers(dest="command")

    # add
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("habit", type=str)
    add_parser.set_defaults(func=add)

    # unadd
    unadd_parser = subparsers.add_parser("unadd")
    unadd_parser.add_argument("habit", type=str)
    unadd_parser.set_defaults(func=unadd)

    # check
    check_parser = subparsers.add_parser("check")
    check_parser.add_argument("habit", type=str)
    check_parser.add_argument("day", nargs="?", default=date.today().day, type=int)
    check_parser.set_defaults(func=check)

    # showcal
    showcal_parser = subparsers.add_parser("showcal")
    showcal_parser.add_argument("habit", type=str)
    showcal_parser.set_defaults(func=show_calendar)

    # uncheck
    uncheck_parser = subparsers.add_parser("uncheck")
    uncheck_parser.add_argument("habit", type=str)
    uncheck_parser.add_argument("day", nargs="?", default=date.today().day, type=int)
    uncheck_parser.set_defaults(func=uncheck)

    # list
    list_parser = subparsers.add_parser("list")
    list_parser.set_defaults(func=list_habits)

    
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()