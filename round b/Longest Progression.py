inp = open("Longest Progression_inp.in")
out = open("Longest Progression_out.ans")
inp_content = inp.readlines()
out_content = out.readlines()
result = []
for x in range(int(inp_content[0])):
    N = int(inp_content[2*x+1])
    nums = list(map(int, inp_content[2*x+2].split()[:N]))
    res = []
    for i in range(1,len(nums)):
        count = 0
        a = nums.copy()
        diff_list = [a[i-1]-a[i]]
        cnt = 2
        for j in range(i,len(nums)-1):
            diff = a[j]-a[j+1]
            if diff == diff_list[-1]:
                diff_list.append(diff)
                cnt += 1
            elif diff!=diff_list[-1] and count==0:
                a[j+1] = a[j]-diff_list[-1]
                diff_list.append(diff_list[-1])
                count += 1
                cnt += 1
            elif diff!=diff_list[-1] and count==1:
                break
        res.append(cnt)

    for i in range(1,len(nums)):
        count = 0
        a = nums[::-1].copy()
        diff_list = [a[i-1]-a[i]]
        cnt = 2
        for j in range(i,len(nums)-1):
            diff = a[j]-a[j+1]
            if diff == diff_list[-1]:
                diff_list.append(diff)
                cnt += 1
            elif diff!=diff_list[-1] and count==0:
                a[j+1] = a[j]-diff_list[-1]
                diff_list.append(diff_list[-1])
                count += 1
                cnt += 1
            elif diff!=diff_list[-1] and count==1:
                break
        res.append(cnt)
    result.append(max(res))
count = 0
for i in range(int(inp_content[0])):
    msg = f"Case #{i+1}: {result[i]}"
    if out_content[i][:len(msg)]==msg:
        print(msg)
    else:
        print("Not Working!", result[i], out_content[i])
        count += 1
print(count)