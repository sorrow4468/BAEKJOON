def solution(new_id):
    answer = ''
    # print(new_id)
    new_id = new_id.lower()
    tmp = ''
    
    for n in new_id: # step 2
        if n in 'abcdefghijklmnopqrstuvwxyz0123456789-_.':
            tmp = tmp + n
    switch = False
    tmp2 = ''
    
    for t in tmp: # step 3
        if t == '.':
            if not switch:
                switch = True
                tmp2 = tmp2 + t
        else:
            tmp2 = tmp2 + t
            if switch:
                switch = False
    # print('step3', tmp2)
                
    if len(tmp2) >= 2:
        if tmp2[0] == '.': # step 4
            tmp2 = tmp2[1:]
        if tmp2[-1] == '.':
            tmp2 = tmp2[:len(tmp2)-1]
    else:
        tmp2 = ''
    # print('step4', tmp2)
        
    if tmp2 == '': # step 5
        tmp2 = 'a'
        
    if len(tmp2) >= 16: # step 6
        tmp2 = tmp2[:15]
        if tmp2[-1] == '.':
            tmp2 = tmp2[:len(tmp2)-1]
    
    while len(tmp2) <= 2: # step 7
        tmp2 = tmp2 + tmp2[-1]
        
    answer = tmp2
    return answer

print(solution(input()))