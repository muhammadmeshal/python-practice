dict_1 = {'one': 1,'two': 2,'three': 3,'four':4,'five':5}
dict_new = dict_1.copy()
print("Dict:", dict_new)

pop_one = dict_new.pop('one',0)
if(pop_one):
    print("Removed")
else:
    print("No found")

pop_seven = dict_new.pop("seven",0)
if(pop_seven):
    print("Removed")
else:
    print('Not Found')
print("Dict after pop:",dict_new)  