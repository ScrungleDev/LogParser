import argparse
from parsers.registry import get_parsers


def main():
    parser =argparse.ArgumentParser(
        description="LogParser - A modular log parsing and analysis tool"
    )
    parser.parse_args()


    parsers = get_parsers()

    sample_lines = [
        "DUMMY example line",
        "unknown garbage line"
    ]

    for line in sample_lines:
        for parser in parsers:
            if parser.can_parse(line):
                result = parser.parse_line(line)
                if result != None:
                    print(result)
                break

if __name__ == "__main__":
    main()