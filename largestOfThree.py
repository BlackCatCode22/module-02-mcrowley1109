def maximum(fa, fb, fc): 
    if (fa >= fb) and (fa >= fc): 
        largest = fa 
    elif (fb >= fa) and (fb >= fc): 
        largest = fb 
    else: 
        largest = fc  
sa = input("Enter value for a: ")
sb = input("Enter value for b: ") 
sc = input)"Enter value for c: ")
fa = float(sa)
fb = float(sb)
fc = float(sc)
return largest
print(maximum(fa, fb, fc))
