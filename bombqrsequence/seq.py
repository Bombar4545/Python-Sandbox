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

def longest(s):
    l = 0

    for e in s:
        l = max(l, len(e))
    
    return l

def print_bs(bs, base):
    if base < 2: base = 10
    l = []
    for e in bs:
        s = ''
        for i in e:
            s += str(i)
        b = int(s, base)
        l.append(b)
        print(b, ':\t', s)
    return sorted(l)

if __name__ == '__main__':
    import sys

    if len(sys.argv) == 2:
        N = int(sys.argv[1])
        S = 'Running for N={}'.format(N)
        print(S)

        if N > 3: print('N is too large to compute, latency may occur!', file=sys.stderr)

        s = build_sett_req(sett=set(range(N)))

        print('Computed! B Set of {} with {} elements'.format(N, len(s)))
        l = print_bs(s, N)
        print(l)

        f1 = open('outN-{}.txt'.format(N), 'w')
        f1.write(str(l))
        f1.close()

    else:
        N = 3
        S = '''
                                B SET DEMO

        B Set: Set of possible non-emply sequences that can be arranged 
        with n different elements and each subsequence of any element in 
        set, minimum length of 2, contained in the sequence at max once.

        B Set Max: Maximum length of a sequence that can be in the B Set 
        of n.

        B Set Length: Number of elements in the B set of n.


                    Table 1. Values of BSM and BSL.
        -----------------------------------------------------------------
        | n     | BSM(n)        | BSL(n)                                |
        -----------------------------------------------------------------'''

        print(S)

        for i in range(N + 1):
            starts = set(range(i))

            allset = build_sett_req(sett=starts)

            print('\t| {} \t| {}   \t\t| {} \t\t\t\t\t|'.format(i, longest(allset), len(allset)))
        S = '''\t-----------------------------------------------------------------
        '''
        print(S)