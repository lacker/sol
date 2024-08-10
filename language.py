def eval_list_form(code):
    if type(code) != list:
        return code
    fn, args = code[0], code[1:]
    if fn == "quote":
        return args
    raise Exception("TODO: handle lists")
