#!/usr/bin/env python3
import argparse
import re
import sys

def main():
    parser = argparse.ArgumentParser(
        description="Convert arguments into a comma-separated list."
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

    args = parser.parse_args()

    # Se è stato usato -o, prendiamo SOLO gli oggetti dopo -o
    if args.objects is not None:
        items_raw = " ".join(args.objects)

    # altrimenti usiamo la vecchia logica items normali
    else:
        items_raw = " ".join(sys.argv[1:])  # prende TUTTI gli argomenti dopo script
        # rimuove i flag -nb
        items_raw = items_raw.replace("-nb", "").replace("--no-brackets", "").strip()

    # Collassa whitespace multiplo
    collapsed = re.sub(r"\s+", " ", items_raw).strip()
    items = collapsed.split(" ") if collapsed else []

    output = ", ".join(items)

    if not args.no_brackets:
        output = f"[{output}]"

    print(output)


if __name__ == "__main__":
    main()
