inp = open("Increasing Substrings_inp.in")
out = open("Increasing Substrings_out.ans")
inp_content = inp.readlines()
out_content = out.readlines()
result = []
for x in range(int(inp_content[0])):
    a = []
    N = int(inp_content[2*x+1])
    S = inp_content[2*x+2].upper()[:N]
    for i in range(len(S)):
        if i==0:
            a.append(1)
        else:
            count = 1
            for j in range(i):
                if ord(S[j])<ord(S[j+1]):
                    count += 1
                else:
                    count = 1
            a.append(count)
    result.append(a)
count = 0
for i in range(int(inp_content[0])):
    msg = f"Case #{i+1}:"
    for j in result[i]:
        msg = msg + ' '+ f"{j}"
    if out_content[i][:len(msg)]==msg:
        print(msg)
    else:
        print("Not Working!")
        count += 1
print(count)
