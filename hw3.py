a=int(input('할인율은?'))


def get_fixed_price(price):
    percent=100/(100-a)
    k=price*percent
    return k

c=int(input('A상품의 할인된 가격은?'))
e=get_fixed_price(c)
d=int(input('B상품의 할인된 가격은?'))
f=get_fixed_price(d)       
print('A상품의 정가는?',e,'원')
print('B상품의 정가는?',f,'원')
