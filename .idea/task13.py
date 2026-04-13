L, target = [2, 7, 11, 15], 9
for i in range(len(L)):
    for j in range(i+1, len(L)):
        if L[i] + L[j] == target:
            print(f"Task 13: {L[i]}, {L[j]}")
            break
    else:
        continue
    break