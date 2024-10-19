inp = open("L Shaped Plots_inp.in")
out = open("L Shaped Plots_out.ans")
inp_content = inp.readlines()
out_content = out.readlines()
inp_cnt = 0
result = []
for x in range(int(inp_content[0])):
    inp_cnt+=1
    R, C = map(int, inp_content[inp_cnt].split())
    grid = []
    for i in range(R):
        inp_cnt+=1
        grid.append(list(map(int, inp_content[inp_cnt].split()[:C])))
    ones_row_wise = {}
    ones_col_wise = {}
    for i in range(len(grid)):
        count = 0
        for j in range(C):
            if grid[i][j]==1:
                count+=1
                if count==2:
                    ones_row_wise[(i,j-count+1,j)] = count*[1]
                elif count>2:
                    for k in range(count):
                        for l in range(k+1,count):
                            ones_row_wise[(i,j-count+1+k,j-count+1+l)] = (l-k+1)*[1]
            else:
                count = 0
    for i in range(C):
        count = 0
        for j in range(R):
            if grid[j][i]==1:
                count+=1
                if count==2:
                    ones_col_wise[(i,j+1-count,j)] = count*[1]
                elif count>2:
                    for k in range(count):
                        for l in range(k+1,count):
                            ones_col_wise[(i,j-count+1+k,j-count+1+l)] = (l-k+1)*[1]
            else:
                count=0
    count = 0
    for k1, v1 in ones_row_wise.items():
        for k2, v2 in ones_col_wise.items():
            if (k1[0]==k2[1] or k1[0]==k2[2]) and (len(v1)==2*len(v2) or len(v2)==2*len(v1)) and (k2[0]==k1[1] or k2[0]==k1[2]):
                count+=1
    result.append(count)
    print(x,count)
count = 0
for i in range(int(inp_content[0])):
    msg = f"Case #{i+1}: {result[i]}"
    if out_content[i][:len(msg)]==msg:
        print(msg)
    else:
        print("Not Working!")
        count += 1
print(count)