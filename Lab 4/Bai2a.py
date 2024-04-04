so = 2
while so < 100:
    nguyen_to = True
    uoc_so = 2
    while uoc_so * uoc_so <= so:
        if so % uoc_so == 0:
            nguyen_to = False
            break
        uoc_so += 1
    if nguyen_to:
        print(so, end=" ")
    so += 1