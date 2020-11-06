from plover.formatting import _Context, _Action


def __retro_surround(ctx: _Context, cmdline: str) -> _Action:
    action: _Action = ctx.copy_last_action()
    args = cmdline.split(":")
    word_cnt = int(args[0])
    left_char = args[1]
    right_char = args[2]

    last_words = "".join(ctx.last_fragments(count=word_cnt))

    action.prev_replace = last_words
    action.text = left_char + last_words + right_char
    action.word = None
    action.prev_attach = True

    return action


def retro_surround(*args, **kwargs) -> _Action:
    return __retro_surround(*args, **kwargs)
