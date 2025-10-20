from faker import Faker

faker = Faker()

def payload_grupo(name="__faker__", handle="__faker__"):
    payload = {}

    # name
    if name == "__faker__":
        payload["name"] = faker.company()
    elif name is not None:
        payload["name"] = name
    # Si es None => no se agrega al payload

    # handle
    if handle == "__faker__":
        payload["handle"] = faker.user_name()
    elif handle is not None:
        payload["handle"] = handle
    # Si es None => no se agrega al payload

    return payload
