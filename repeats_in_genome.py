D = {}
for line in open("Culex-tarsalis_knwr_BASEFEATURES_CtarK1.gff3"):
    i=line.strip().split()
    if len(i)<2:
        continue
    if i[1]=="repeatmasker":
        #print(line.strip())
        tig = i[0]
        if tig not in D:
            D[tig]=[]
        D[tig].extend(list(range(int(i[3]),int(i[4])+1)))

L = 0
for contig in D:
    L+=len(set(D[contig]))
print("repeat_len", L)
~                         
