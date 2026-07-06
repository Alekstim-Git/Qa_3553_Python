# №_1
print()


def print_string_reverse(s):
    if s is None or s == '' or s.isspace():
        print('Wrong string')
    else:
        print(s[::-1])


print_string_reverse('Shalom')
print_string_reverse('      ')

# № 2
print()


def is_isr_phone_number(phone):
    if phone is None or phone == '' or phone.isspace():
        return None
    if len(phone) == 10 and phone[0] == '0' and phone.isdigit():
        return True
    else:
        return False


print(is_isr_phone_number('0549856345'))
print(is_isr_phone_number('154985634r'))
print(is_isr_phone_number(''))

# № 3
print()


def print_substring_reverse(s, start, finish):
    if s is None or s == '' or s.isspace():
        print('Wrong args')
        return
    if start < 0 or finish >= len(s) or start > finish:
        print("Wrong args")
        return
    start_part = s[:start]
    middle_part = s[start:finish + 1]
    end_part = s[finish + 1:]
    result = start_part + middle_part[::-1] + end_part
    print(result)
print_substring_reverse("Shalom", 1, 3)
# № 4
print()
