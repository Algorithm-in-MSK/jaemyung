MAX_INPUT_LEN = 5000
DIVISOR = 1000000

def is_valid_input(input):
    assert input.isdigit() and len(input) <= MAX_INPUT_LEN

def is_valid_unicode(code):
    if len(code) == 2 and code[0] != '0' and int(code) < 27:
        return 1
    elif len(code) == 1 and int(code) > 0:
        return 1
    else:
        return 0

def decode(enc_input):
    is_valid_input(enc_input)

    dec_list = [1]
    for i in range(len(enc_input)):
        if i == 0:
            dec_list.append(is_valid_unicode(enc_input[i]))
        else:
            n = is_valid_unicode(enc_input[i]) * dec_list[i] + is_valid_unicode(enc_input[i-1:i+1])* dec_list[i-1]
            dec_list.append(n)

    return dec_list[-1]

if __name__ == "__main__":
    enc_input = input()
    n = decode(enc_input)
    print(n % DIVISOR)