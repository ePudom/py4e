# s = 'I don\'t know'
# t = "Hello there"

# print(s[-4])
# # for i in t:
# #     print(i)

# print(t[len(s)-4])

# u = 'Hippopotamus'
# v = u[0:5]
# w = u[3:7]
# x = u[:len(u):2]
# print(v)
# print(w)
# print(x)

# a = "*|*"
# print(a * 4)

# print(w.upper())

# a = "this is in lowercase"
# b = "THIS IS IN UPPERCASE"

# print(a.upper())
# print(a.capitalize())
# print(b.lower())

# c = "The boy will cut his hair and his hair will grow longer"
# d = c.replace('boy', 'man')
# e = c.replace('hair', 'beard')
# f = c.replace('hair', 'beard', 1)
# print(d)
# print(e) 
# print(f) 

# g = 'I know who God says I am, what He says I am, where He says I\'m at. I know who I am'
# h = g.title()
# print(g.count('I'))
# print(g.count('says'))
# print(h)

# i = 'We are going to be GREAT. We Believe It!!!'
# j = i.swapcase()
# print(j) 

# k = "*"
# l = ('b','i','s','o')

# print(k.join(l))

# m = '***This is a string***'
# n = m.lstrip('*')
# o = m.rstrip('*')
# p = m.lstrip('*').rstrip('*')
# q = m.strip('*') 
# print(m)
# print(n)
# print(o)
# print(p)  
# print(q) 

# r = 'This will be used as a test, be warned'
# print(r.find('be')) # returns the first char index of the first occurence
# print(r.find('is'))
# print(r.find('we')) # returns -1

# print(r.rfind('be')) # returns the first char index of the last occurence 
# print(r.rfind('is'))
# print(r.rfind('we')) # returns -1

# print(r.index('be')) # returns the first char index of the first occurence
# print(r.index('is'))
# print(r.index('we')) # returns error

# print(r.rindex('be')) # returns the first char index of the first occurence
# print(r.rindex('is'))
# print(r.rindex('we')) # returns error

# s = 'AS00U7'
# print(s.zfill(10))

# t = 'New txt'
# print(t.rjust(20, '*'))
# print(t.ljust(20, '*'))
# print(t.center(20, '*'))

# u = 'Tola'
# v = 'Tayo'
# w = 'Tolu'

# u_age = 32
# v_age = 21
# w_age = 23

# header_1 = 'Name'
# header_2 = 'Age'
# header_3 = 'Cash at hand'

# print('{0} is {3} years old, {1} is {4} years old and {2} is {5} years old'.format(u, v, w, u_age, v_age, w_age))

# LIST_LEN = 3

# names = list()
# names.append('Tola')
# names.append('Tayo')
# names.append('Tolu')

# ages = list()
# ages.append(32)
# ages.append(21)
# ages.append(23)

# cash = list()
# cash.append(100.23401)
# cash.append(2003.1117)
# cash.append(500.22092)

# print('\n')

# print('{0}{1:>10s}{2:>20s}'.format(header_1, header_2, header_3))

# for i in (0,1,2):
#     print('{0}{1:>10s}{2:>20s}\n'.format(names[i], ages[i], cash[i]))

# a = [1,2,3]
# b = [4,5]
# c = a + b
# print(c)

a = 'Banana'
a[0] = 'b'
print(a) 