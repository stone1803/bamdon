# lay thoi gian am lich
# cong thuc (tinh ngay am + thang am + gio di ) - 2 % 6
# gio dinh khac 11h den 1h 1
# 1 h 3 h la 2
# 3 5 la 3
# 5 7 la 4
# 7 9 la 5
# 9 11 6
# # 22- 6 - 2019
# khac = {1: [11, 1], 2: [1, 3], 3: [3, 5], 4: [5, 7], 5: [7, 9], 6: [9, 11]}
# tim = 7
# for key, val in khac.items():
#     val == tim
#     print(val)

# # print(khac[1][0])
# # print(khac[1][1])
# # if  n == khac[1][0]:
# #     print('oke0')
# # elif n == khac[1][1]:
# #     print('oke1')
# # else:
# #     print('no')
#
# dictionary = {'george' : 16, 'amber' : 19}
# search_age = 16
# for name, age in dictionary.items():    # for name, age in dictionary.iteritems():  (for Python 2.x)
#     if age == search_age:
#         print(name)

def find(key, dictionary):
    for k, v in dictionary.items():
        if k == key:
            yield v
        elif isinstance(v, dict):
            for result in find(key, v):
                yield result
        elif isinstance(v, list):
            for d in v:
                for result in find(key, d):
                    yield result

example = {'app_url': '', 'models': [{'perms': {'add': True, 'change': True, 'delete': True}, 'add_url': '/admin/cms/news/add/', 'admin_url': '/admin/cms/news/', 'name': ''}], 'has_module_perms': True, 'name': u'CMS'}
khac = {1: [11,12,1], 2: [1,2, 3], 3: [3,4, 5], 4: [5,6, 7], 5: [7,8, 9], 6: [9,10, 11]}
for k, v in khac.items():
    print(k)
print(len(khac))


print(khac[1][1])
print(khac[1][0])
a = 4
b = khac[1][1]
c = khac[1][0]
if a == 11:
    print(1)
elif a == 1:
    print(1)
elif a == 12:
    print(1)
elif a== 1:
    print(1)
else:
    print("sai")
