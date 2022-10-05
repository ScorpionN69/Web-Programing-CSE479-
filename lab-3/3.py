def Merge(d1, d2,d3):
    res = {**d1, **d2 , **d3}
    return res
d1= {1:10 , 2:20}
d2= {3:30 , 4:40}
d3= {5:50 , 3:60}
a= Merge(d1, d2,d3)
print(a)
