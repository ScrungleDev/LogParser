

class BaseParser:

    def can_parse(self, line: str) -> bool:
        # Returns true if this parser recognizes the line format
        pass

    def parse_line(self, line: str) -> dict | None:
        # Attempts to parse the line
        # Returns dictionary OR None
        pass

