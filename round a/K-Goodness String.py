inp_file = open("K-Goodness String_inp.in")
out_file = open("K-Goodness String_out.ans")
inp_content = inp_file.readlines()
out_content = out_file.readlines()
result = []
for x in range(int(inp_content[0])):
    N, K = map(int, inp_content[2*x+1].split())
    S = inp_content[2*x+2][:N].upper()
    count = 0
    for i in range(len(S)//2):
        if S[i]!=S[len(S)-i-1]:
            count += 1
    if count==K:
        result.append(0)
    else:
        result.append(abs(count-K))
count = 0
for i in range(int(inp_content[0])):
    msg = f"Case #{i+1}: {result[i]}"
    if out_content[i][:len(msg)]==msg:
        print(msg)
    else:
        print("Not Working!")
        count += 1
print(count)
