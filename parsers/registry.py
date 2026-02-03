from parsers.dummy_parser import DummyParser
# later:
# from parsers.json_parser import JsonParser
# from parsers.regex_parser import RegexParser

def get_parsers():
    return [
        DummyParser(),
        # JsonParser(),
        # RegexParser(),
    ]
