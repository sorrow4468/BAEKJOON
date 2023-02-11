orders = input()
balls = [1, 0, 0]
for order in orders:
    if order == 'A':
        balls[0], balls[1] = balls[1], balls[0]
    if order == 'B':
        balls[2], balls[1] = balls[1], balls[2]
    if order == 'C':
        balls[0], balls[2] = balls[2], balls[0]
print(balls.index(1)+1)    