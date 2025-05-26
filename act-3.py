class ele:
    def fun1(self,nums,val):
        dict1={}
        for i,num in enumerate(nums):
            if val - num in dict1:
                return (dict1[val - num],i)
            dict1[num]=i



val=int(input("Enter the sum: "))
print("index1=%d,index2=%d" % ele().fun1((1,2,3,4,5,6,7,8,9,10,20,30,40,50,60,80,70,90,100),val))