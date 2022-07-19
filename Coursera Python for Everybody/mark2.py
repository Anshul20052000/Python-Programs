def computepay(h,r):
    if h>40:
        tot1=h*r
        tot2=(h-40)*((r*1.5)-r)
        tot=tot1+tot2
    else :
        tot=h*r
    return tot
hrs = input("Enter Hours:")
rate = ("Enter the Rate")
H = float(hrs)
R = float(rate)
p = computepay(H,R)
print("Pay",p)

