beer = {
    '하이트': 2000, 
    '카스': 2100, 
    '칭따오': 2500, 
    '하이네켄': 4000, 
    '버드와이저': 500,
}

# print(beer, '           # 인상 전')

# for b in beer:
#     beer.update({b:beer[b]*1.05})

# print(beer, ' # 인상 후')


print(beer)

for b in beer:
    beer.update({b:beer[b]*1.05})

print(beer)