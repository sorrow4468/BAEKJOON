def dec_to_bin(number):
    # number : str
    dividor = 1
    number = int(number)
    while dividor*2 <= number:
        dividor *= 2
    answer = ''
    while dividor >= 1:
        if number >= dividor:
            answer += '1'
            number -= dividor
        else:
            answer += '0'
        dividor //= 2
    return answer

def bin_to_dec(number):
    # number : str
    multiplier = 1
    answer = 0
    for num in number:
        answer += int(num) * multiplier
        multiplier *= 2
    return answer

N = input()
N = dec_to_bin(N).rstrip('0')
N = bin_to_dec(N)
print(N)