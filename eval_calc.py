def eval_expression(val):
    code = compile(val, "<string>", "eval")
    if code.co_names:
        raise NameError(f"Do not use names.")
    return eval(code, {"__builtins__": {}}, {})
