from pprint import pprint

formA = "ADAADADDDACBCABBCBBCBABBBBDBBBAADDADABBBCCAABDADDBCABCCBBACADDABCBDABBDCDACBCCACDBAADDACBDBCBDCBDCDAABADADCABBABBACBCCBDBDCDDABAAACCDDADAABABBBCACCBBDDBACCDCCBBCDCABAAACDBBACADDADABAADDACAACABACCDDDBB"

formB = "CCCDCCAABBBDBBADACCBABDADCCDAACBCBBBDCDADACDACBCCDDDCAAACCABCACCDCCCDDCBBDBABDCAAACDCADDAAADCABCCBBCBACCDAADDDDDDBBCDACBCBAACDCBCCBDBBCBBBADDAADBBACAABCDADABAACDCDBDCCDACAACDBBABBDACCCADDDBDDADABACBAD"

l = []
with open("modified.dat") as f:
    l = [x.strip() for x in f.readlines()]

nl = []
for e in l:
    nl.append(e.split("\t"))

def closest_to(ans):
    ratingA = 0
    ratingB = 0
    for i in range(len(ans)):
        if ans[i] == formA[i]:
            ratingA += 1
        if ans[i] == formB[i]:
            ratingB += 1
    print ratingA, ratingB
    return "A" if ratingA > ratingB else "B"

cheaters = ""
for e in nl:
    # print '"' + closest_to(e[3]) + '"' + '\t"' +  e[0] + '"'
    if closest_to(e[3]) != e[0]:
        cheaters += e[1].split()[1] + ","

print(cheaters)
