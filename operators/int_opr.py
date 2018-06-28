
def less_than_equals(rule, json_obj):

    if float(json_obj['value']) <= float(rule[2]):
        return True

    return False


def less_than(rule, json_obj):

    if float(json_obj['value']) < float(rule[2]):
        return True

    return False


def greater_than_equals(rule, json_obj):

    if float(json_obj['value']) >= float(rule[2]):
        return True

    return False


def greater_than(rule, json_obj):

    if float(json_obj['value']) > float(rule[2]):
        return True

    return False


def equals(rule, json_obj):
    if float(json_obj['value']) == float(rule[2]):
        return True

    return False


def not_equals(rule, json_obj):
    if float(json_obj['value']) != float(rule[2]):
        return True

    return False
