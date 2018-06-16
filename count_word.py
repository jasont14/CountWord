fil = 'PATH TO FILE HERE; e.g. C:\\folder\\file.txt' 
with open(fil,'r') as f:   
    #Dict (K,V) to hold word, count
    cnt = {}
    lines = f.readlines()
    for line in lines:
        #skip blank lines
        if line =='\n':
            continue
        else:
            words = line.split()
            for word in words:
                if word in cnt:
                    cnt[word] += 1
                else:
                    cnt[word] = 1
    #print
    for key in cnt.keys():
        print(key, cnt[key])