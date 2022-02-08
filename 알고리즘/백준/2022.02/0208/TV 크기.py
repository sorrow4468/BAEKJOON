D, H, W = map(int, input().split())

C = ((H*H)+(W*W))**0.5

print(int(D * H / C), int(D * W / C))
