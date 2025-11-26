#!/usr/bin/env python3
import argparse
import re
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Convert arguments into a delimiter-separated list."
    )

    parser.add_argument(
        "-nb", "--no-brackets",
        action="store_true",
        help="Do not wrap the output in [ ]"
    )

    parser.add_argument(
        "-o", "--objects",
        nargs=argparse.REMAINDER,
        help="Treat everything after -o as list items"
    )

    parser.add_argument(
        "-d", "--delimiter",
        default=", ",
        help="Delimiter to use between items (default: ', ')"
    )

    args = parser.parse_args()

    # Se è stato usato -o, prendiamo SOLO gli oggetti dopo -o
    if args.objects is not None:
        items_raw = " ".join(args.objects)

    # altrimenti usiamo gli argomenti normali
    else:
        items_raw = " ".join(sys.argv[1:])
        # Rimuoviamo i flag noti
        for flag in ("-nb", "--no-brackets", "-d", "--delimiter"):
            items_raw = items_raw.replace(flag, "")
        items_raw = items_raw.strip()

    # Collassa whitespace multiplo
    collapsed = re.sub(r"\s+", " ", items_raw).strip()
    items = collapsed.split(" ") if collapsed else []

    # Usa il delimitatore scelto
    output = args.delimiter.join(items)

    if not args.no_brackets:
        output = f"[{output}]"

    print(output)


if __name__ == "__main__":
    main()
