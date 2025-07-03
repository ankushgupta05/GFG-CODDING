class Pattern:
    def __init__(self,n):
        self.n = n

    def Squar(self):
        for i in range(self.n):
            for j in range(self.n):
                print("*",end=" ")
            print()
        return 0

        # Pattern gives as a resulted of this code.
        # * * * * * 
        # * * * * *
        # * * * * *
        # * * * * *
        # * * * * *








    def LeftIncreasingOrder(self):
        for i in range(self.n):
            for j in range(i+1):
                print("*",end=" ")
            print()
        return 0

        # Pattern gives as a resulted of this code.
        # * 
        # * *
        # * * * 
        # * * * *
        # * * * * *



    def LeftDecreasingOrder(self):
        for i in range(self.n):
            for j in range(i,self.n):
                print("*",end=" ")
            print()
        return 0

        # Pattern gives as a resulted of this code.
        # * * * * *
        # * * * *
        # * * * 
        # * *
        # * 

    def PrimeNumber(self):
        count = 0
        if self.n == 0 or self.n == 1:
            print(f"The Number {self.n}  is Not Prime.") 
        
        else:
            for i in range(1,self.n+1):
                if self.n % i == 0:
                    count += 1

            if count == 2:
                print(f"The Number {self.n} is Prime.")
            else:
                print(f"The Number {self.n} is Not Prime.")

        
    def RightIncreasingOrder(self):
        for i in range(self.n):
            for j in range(i,self.n):
                print(' ',end=' ')
            
            for i in range(i+1):
                print('*',end=' ')
            print()
        

        #           * 
        #         * *
        #       * * *
        #     * * * *
        #   * * * * *

        

    def RightDecreasingOrder(self):
        for i in range(self.n):
            for j in range(i+1):
                print(' ',end=' ')
            
            for i in range(i,self.n):
                print('*',end=' ')

            print()

        #   * * * * *
        #     * * * *
        #       * * *
        #         * *
        #           * 

        


        
    def HillOrder(self):
        for i in range(self.n):
            for j in range(i,self.n):
                print(' ',end=' ')
            
            for j in range(i):     # 1 ko add nahi kiya 
                print('*',end=' ')

                
            for j in range(i):
                print('*',end=' ')
            
            print()


        #           * 
        #         * * *
        #       * * * * *
        #     * * * * * * *
        #   * * * * * * * * *






    def ReverseHillOrder(self):
        for i in range(self.n):
            for j in range(i+1):
                print(' ',end=' ')

            for j in range(i,self.n-1):
                print('*',end=' ')

            for j in range(i,self.n):
                print('*',end=' ')
            


            print()
            
        #   * * * * * * * * * 
        #     * * * * * * *
        #       * * * * *
        #         * * *
        #           *






    def DiamondOrder(self):
        for i in range(self.n-1):
            for j in range(i,self.n):
                print(' ',end=' ')
            for j in range(i):
                print('*',end=' ')
            for j in range(i+1):
                print('*',end=' ')

            print()


        for i in range(self.n):
            for j in range(i+1):
                print(' ',end=' ')
            for j in range(i,self.n-1):
                print('*',end=' ')
            for j in range(i,self.n):
                print('*',end=' ')


            print()


        #           * 
        #         * * *
        #       * * * * *
        #     * * * * * * *
        #   * * * * * * * * *
        #     * * * * * * *
        #       * * * * *
        #         * * *
        #           *









# 1)
# test=Pattern(5)
# test.Squar()



# 2)
# test=Pattern(5)
# test.LeftIncreasingOrder()



# 3)
# test=Pattern(5)
# test.LeftDecreasingOrder()



# 4)
# test=Pattern(5)
# test.RightIncreasingOrder()



# 5)
# test=Pattern(5)
# test.RightDecreasingOrder()



# 6)
# test=Pattern(5)
# test.HillOrder()





# 7)
# test=Pattern(5)
# test.ReverseHillOrder()




# 8)
test=Pattern(5)
test.DiamondOrder()





# 8)
# test=Pattern(11)
# test.PrimeNumber()


