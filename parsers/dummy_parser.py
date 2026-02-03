from parsers.base import BaseParser

class DummyParser(BaseParser):
    #A reference implementation of the parser contract.
    def can_parse(self, line: str) -> bool:
        return line[:5] == "DUMMY"
    
    def parse_line(self, line: str) -> dict | None:
        return {
            "parser": "dummy",
            "raw": line
        }
