class employee:
    def __init__(self,age,name):
          self.age=age
          self.name=name
          print("super")
    def details(self):
        print(self.age)
        print(self.name)

class Manager(employee):
    def __init__(self,age,name):
        super(Manager,self).__init__(age,name)
        print("lavadi")
    def printer(self,x,y):
        print(x+y)






def main():
    t=Manager(20,"bharu")
    t.details()
    t.printer(20,30)
    #print("mama")
for i in range(1,5):
    print("8"*i)

if __name__=="__main__":
    main()