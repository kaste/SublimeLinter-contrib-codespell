from SublimeLinter.lint import Linter


class Codespell(Linter):
    cmd = ('codespell', '${args}', '-')
    defaults = {
        'selector': '',
    }
    regex = r"^(?P<line>\d+).*\n\s+(?P<message>(?P<near>\w+) ==> .+)"
    multiline = True
