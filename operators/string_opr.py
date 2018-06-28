

def equals(rule, json_obj):
    if json_obj['value'].strip() == rule[2].strip():
        return True

    return False


def not_equals(rule, json_obj):
    if json_obj['value'].strip() != rule[2].strip():
        return True

    return False


def contains(rule, json_obj):
    if rule[2].strip() in json_obj['value'].strip():
        return True

    return False
