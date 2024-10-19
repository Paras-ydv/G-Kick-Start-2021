inp = open("Consecutive primes_inp.in")
out = open("Consecutive primes_out.ans")
inp_content = inp.readlines()
out_content = out.readlines()
result = []
for x in range(int(inp_content[0])):
    Z = int(inp_content[x+1])
    if Z<15:
        result.append(6)
    else:
        for i in range(Z):
            if i**2<=Z:
                num = i
            else:
                break
        primes = (Z+1)*[True]
        primes[0] = False
        primes[1] = False
        for p in range(2, int(pow(Z,0.5))+1):
            if primes[p]==True:
                for i in range(p*p,Z+1,p):
                    primes[i] = False
        ind = []
        for i in range(len(primes)):
            if primes[i]==True:
                if i<num:
                    ind.append(i)
                elif i==num:
                    ind.append(i)
                elif i>num:
                    ind.append(i)
                    break
        if ind[-2]*ind[-1]<=Z:
            result.append(ind[-2]*ind[-1])
        else:
            result.append(ind[-3]*ind[-2])
count = 0
for i in range(int(inp_content[0])):
    msg = f"Case #{i+1}: {result[i]}"
    if out_content[i][:len(msg)]==msg:
        print(msg)
    else:
        print("Not Working!", result[i])
        count += 1
print(count)