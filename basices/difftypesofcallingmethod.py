class Demo:
    def disp(self,a=10,b=20,c=30):
        print(a)
        print(b)
        print(c)
d=Demo()
x=11
y=22
z=33
d.disp()
d.disp(x,y,z)
d.disp(x)
d.disp(z)
d.disp(y,z)
d.disp(c=z)
d.disp(a=y,b=z,c=x)
