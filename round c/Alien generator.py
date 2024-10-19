inp = open("Alien generator_inp.in")
out = open("Alien Generator_out.ans")
inp_content = inp.readlines()
out_content = out.readlines()
result = []
for x in range(int(inp_content[0])):
    G = int(inp_content[x+1])
    res = []
    for i in range(1,G+1):
        K = i
        sum = 0
        for j in range(1,G+1):
            K = i+j-1
            sum += K
            if sum==G:
                res.append(i)
                break
            elif sum>G:
                break
    result.append(len(res))
count = 0
for i in range(int(inp_content[0])):
    msg = f"Case #{i+1}: {result[i]}"
    if out_content[i].rstrip() == msg:
        print(msg)
    else:
        print("Not Working")
        count += 1
print(count)