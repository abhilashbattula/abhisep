class Math:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
    def mul(self):
        self.add()    
        print(self.a*self.b)
if __name__=="__main__":
    Math(20,30).add()
    Math(100,200).mul()