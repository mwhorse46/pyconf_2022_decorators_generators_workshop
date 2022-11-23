plugins = {}


def register(func):
    pass


def get_plugin(name: str):
    return plugins[name]

# registering a plugin


@register("code")
def abc():
    print("code")
