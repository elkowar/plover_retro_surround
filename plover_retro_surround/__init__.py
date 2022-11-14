import re
from plover.formatting import _Context, _Action


SEPARATOR_RE = re.compile(r"(?<!(?<!\\)\\):")  # matches only unescaped colons
ESCAPED_COLON_RE = re.compile(r"\\:")

def _unescape_colon(arg):
    return ESCAPED_COLON_RE.sub(":", arg)

def __retro_surround(ctx: _Context, cmdline: str) -> _Action:
    action: _Action = ctx.copy_last_action()
    args = SEPARATOR_RE.split(cmdline)
    word_cnt = int(args[0])
    left_char = _unescape_colon(args[1])
    right_char = _unescape_colon(args[2])
    last_words = "".join(ctx.last_fragments(count=word_cnt))

    action.prev_replace = last_words
    action.text = left_char + last_words + right_char
    action.word = None
    action.prev_attach = True

    return action


def retro_surround(*args, **kwargs) -> _Action:
    return __retro_surround(*args, **kwargs)
