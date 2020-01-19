'''
在类命名空间的变量就是类变量
'''

class Address:
    detail='广州'
    post_coed='510660'
    def info(self):
        print(Address.detail)
        print(Address.post_coed)
print(Address.detail)
addr=Address()
addr.info()
Address.detail='深圳'
Address.post_coed='5106601'
addr.info()

print("+++++++++++++++")
'''
如果程序通过对象对类变量赋值，其实不赋值，而是定义新变量
如果通过类修改类变量的值,也不影响实例变量的值
'''
class Inventory:
    item='鼠标'
    quantity=2000
    def change(self,item,quantity):
        self.item=item
        self.quantity=quantity
iv=Inventory()
iv.change('显示器',500)
print(iv.item)
print(iv.quantity)
print("访问Inventory的item和quantity类变量")
print(Inventory.item)
print(Inventory.quantity)

#通过类修改类变量的值,但不影响实例变量的值
Inventory.item='类变量item的值'
Inventory.quantity='类变量quantity的值'
print("访问实例变量:",iv.item)
print("访问实例变量",iv.quantity)
print("访问类变量",Inventory.item)
print("访问类变量:",Inventory.quantity)