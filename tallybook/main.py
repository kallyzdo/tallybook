#!/usr/bin/env python3
import argparse
from tallybook.parsers import add, unadd, check, uncheck, show_calendar, list_habits, todo
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

    todo_parser = subparsers.add_parser("todo")
    group = todo_parser.add_mutually_exclusive_group()
    group.add_argument("task", nargs='?', help='Todo task to add (wrap in quotes if multiple words)')
    group.add_argument("-r", "--remove", type=int, help="Remove todo by line number")
    todo_parser.set_defaults(func=todo)
    
    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()