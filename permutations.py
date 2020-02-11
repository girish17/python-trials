l = ['a', 'b']

def perm(l, start, end):
    ''' generate all the permutations of list[start] to list[end] '''
    if start==end:
        for j in l:
            print j
        print "    "
    else:
        ''' list[start] to list[end] has more than one permutation, generate these recursively'''
        for j in l[start:end]:
            l[start], j = j, l[start]
            perm(l, start+1, end)
            l[start], j = j, l[start] #restore original list

perm(l, 0, 2)
