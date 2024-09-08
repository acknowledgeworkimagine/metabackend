menu = ["espresso","mocha","latte","capuccino","cortado","americano","de hoya","caramel"]

def find_coffe(coffe):
    if coffe[0] == 'c':
        return coffe

#Map

# map_coffe=map(find_coffe, menu)
# print(map_coffe)
# for x in map_coffe:
#     print(x)

#Filter

filter_coffe=filter(find_coffe,menu)
print(filter_coffe)
for x in filter_coffe:
    print(x)