class MathDojo:
    def __init__(self):
        self.result = 0
    
    def add(self,num, *nums):
        if (nums) :
            for item in nums:
                self.result += item
        self.result += num
        return self  
    

    def subtract(self,num, *nums):
        if (nums) :
            for item in nums:
                self.result -= item
        self.result -= num
        return self

md = MathDojo()
print(md.add(2).add(2,5,1).subtract(3,2).result)