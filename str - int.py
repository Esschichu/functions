Initial_Goods = 5000
#tell store owner to input number of goods dispatched
Goods_dispatched = input('Enter number of goods released in warehouse:')
#get the difference having in mind that the value obtained is a string,convert to int and store in a var
Goods_dispatched_int = int(Goods_dispatched)
Rem_goods = Initial_Goods - Goods_dispatched_int
print('Number of goods Remaining in warehouse is:' + '' ,Rem_goods)



