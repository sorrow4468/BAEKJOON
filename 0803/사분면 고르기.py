x = int(input()) # x와
y = int(input()) # y값을 int로 받아서 
quadrant = 0 # 사분면 값을 초기화해주고
if x >= 0:
    if y >= 0:
        quadrant = 1 # + +
    else:
        quadrant = 4 # + -
else:
    if y >= 0:
        quadrant = 2 # - +
    else:
        quadrant = 3 # - -
print(quadrant) # 사분면 값을 출력