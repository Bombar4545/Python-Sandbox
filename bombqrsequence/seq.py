import copy


def build_sett_req(seq=[], sett=set(), k=1, allseq=set(), ha=tuple):
    for e in sett:
        bl = build(seq, e)

        if sequtive(bl, sett, k):
            allseq.add(ha(bl))
            allbs = build_sett_req(bl, sett, k, allseq, ha)
            allseq = allseq | allbs
    
    return allseq


def build(l, e):
    l = copy.deepcopy(l) + [e]
    return l

def sequtive(l, s=set(), k=1):
    st = set()

    for i in range(len(l)):
        for j in range(i + k, len(l)):
            sl = tuple(l[i:j + 1])
            if sl not in st and st not in s:
                st.add(sl)
            else:
                return False
    s = s | st
    return True

N = 3
print('bs(n, k)=l')
print('-----------------------')

for k in range(1, N + 1):
    for i in range(N + 1):
        starts = set(range(i))

        allset = build_sett_req(sett=starts)
        print('bs(', len(starts), ', ', k, ')=', len(allset), sep='')
    print()