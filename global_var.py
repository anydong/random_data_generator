_global_dict = {}


def _init():
    global _global_dict


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, default_value=None):
    try:
        return _global_dict[name]
    except KeyError:
        return default_value
