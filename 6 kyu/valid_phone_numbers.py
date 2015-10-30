# from re import compile, search
#
# VALID = compile('\([0-9]{3}\) [0-9]{3}-[0-9]{4}')
#
#
# def validPhoneNumber(number):
#     """ valid_phone_number == PEP8, forced camelCase by CodeWars """
#     check = search(VALID, number)
#     return number == check.group(0) if check else False

from re import compile, match

VALID = compile('^\(\d{3}\) \d{3}-\d{4}$')


def validPhoneNumber(number):
    """ valid_phone_number == PEP8 (forced by CodeWars)
    Thanks to 'g964 & werneckpaiva' from CodeWars """
    return bool(match(VALID, number))


assert validPhoneNumber("(123) 456-7890") is True
assert validPhoneNumber("(1111)555 2345") is False
assert validPhoneNumber("(098) 123 4567") is False
assert validPhoneNumber('(123) 456-7890abc') is False
