#Sum The Strings

def sum_str(a, b):
    if(a=="" and b!=""): 
        return b;
    elif(a!="" and b==""): 
        return a;
    elif(a=="" and b==""):
        return "0";
    
    sum=int(a)+int(b);
    return str(sum);
