__all__ = ['op_map']

import int_opr, string_opr, date_opr

op_map = {
    'Integer': int_opr,
    'Datetime': date_opr,
    'String': string_opr
}