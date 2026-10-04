class InputError(ValueError):
    pass


def check(body):
    if not isinstance(body, dict):
        raise InputError("body must be an object")
    failed = []

    if body.get("region") not in {"us-central1", "europe-west1"}: failed.append("region")
    if body.get("sku") not in {"starter", "standard"}: failed.append("sku")
    return {"passed": not failed, "failed": failed, "applied": False}
