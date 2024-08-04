def eval_list_form(code):
    if type(code) != list:
        return code
    fn, args = code[0], code[1:]
    raise Exception("TODO: handle lists")
