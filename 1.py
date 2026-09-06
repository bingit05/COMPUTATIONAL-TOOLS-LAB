class factorial:
    def __init__(self,n):

        self.n=n

    def factorial(self):

        if self.n==1 or self.n==0:

            print("the factorial of ", self.n ,"is 1")

        elif self.n<0 :

            print("please enter a positive number")

            return

        else:

            fact=1

            for i in range(1,self.n+1):

                fact*=i

            print("the factorial", self.n , "is" ,fact)


    def isprime(self):

        
        for i in range(2,int(self.n**0.5 + 1)):

            if self.n%i==0:

                print("  the no. is not prime")

                return


        print("the no. is prime")
        


n = int(input("enter the nummber to find factorial"))

fact = factorial(n)
fact.factorial()


prime= factorial(n)
prime.isprime()


            

