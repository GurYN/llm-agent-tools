import inspect
from typing import get_type_hints


def get_function_info_list(funcs):
    func_info = ""
    for func in funcs:
        func_name = func.__name__
        args = inspect.signature(func).parameters
        arg_types = get_type_hints(func)
        arg_info = [(param.name, arg_types.get(param.name, 'any')) for param in args.values()]
        return_type = get_type_hints(func).get('return', 'any')
        return_type_name = return_type.__name__ if hasattr(return_type, '__name__') else str(return_type)
        description = inspect.getdoc(func)
        func_info += f"{func_name}("
        for idx, (arg_name, arg_type) in enumerate(arg_info):
                arg_type_name = arg_type.__name__ if hasattr(arg_type, '__name__') else str(arg_type)
                if idx > 0:
                    func_info += ", "
                func_info += f"{arg_name}: {arg_type_name}"
        func_info += f") -> {return_type_name} : {description}\n"

    return func_info

def call_function_dynamically(funcs, func_name, *args, **kwargs):
    for func in funcs:
        if func.__name__ == func_name:
            return func(*args, **kwargs)

    return f"Function {func_name} not found"
