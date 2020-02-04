class pi:
    def pi(n=10000000000):
        
        r=1
        A=4*(2**(1/2))*r
        B=8*r
        m=4;
        while m*2<=n :
         B=2*A*B/(A+B)
         A=(A*B)**(1/2)
        
         m=m*2
        pi= round((A/2/r + B/2/r  )/2,15)
        pi=round(pi,15)
        err = round((  A/2/r - B/2/r  )/2,15)
        err=round(err,15)

        return pi

