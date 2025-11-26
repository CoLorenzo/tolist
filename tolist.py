
import argparse, re

def main():
    parser = argparse.ArgumentParser(description="Convert arguments into a comma-separated list.")
    parser.add_argument("-nb","--no-brackets",action="store_true",help="Do not wrap the output in [ ]")
    parser.add_argument("items", nargs="*", help="Items to convert")
    args = parser.parse_args()
    raw = " ".join(args.items)
    collapsed = re.sub(r"\s+"," ",raw).strip()
    items = collapsed.split(" ") if collapsed else []
    output = ", ".join(items)
    if not args.no_brackets:
        output = f"[{output}]"
    print(output)
