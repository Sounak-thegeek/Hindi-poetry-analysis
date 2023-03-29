import codecs
def matrabharcalculator(s):
    l = list(s)
    numeral = []
    length = len(l)
    ind_hrsa_svara = ['अ','इ','उ','ऋ']
    dep_hrsa_svara = ['ि','ु','ृ']
    ind_dirgh_svara = ['आ','ई','ऊ','ए','ऐ','ओ','औ']
    dep_dirgh_svara = ['ा','ी','ू','े','ै','ो','ौ']
    halant = '्'
    anusvar = 'ं'
    anunasik = 'ँ'
    vyanjan = ['क', 'ख', 'ग', 'घ', 'ङ', 'च', 'छ', 'ज', 'झ', 'ञ', 'ट', 'ठ', 'ड', 'ढ', 'ण', 'त', 'थ', 'द', 'ध', 'न', 'प',
               'फ', 'ब', 'भ', 'म', 'य', 'र', 'ल', 'व', 'श', 'ष', 'स', 'ह','ड़','ढ़']
    nuqta_vyanjan = ['क़','ख़','ग़','फ़','ज़']
    i = 0
    while i < length:
        if l[i] == ',':
            break
        elif l[i] == '़' or l[i] == '-' or l[i] == '!':
            i += 1
            continue
        elif l[i] == anusvar or l[i] == anunasik:
            numeral.pop(-1)
            numeral.append(2)
            i += 1
        elif l[i] in ind_hrsa_svara:
            numeral.append(1)
            i += 1
        elif l[i] in ind_dirgh_svara:
            numeral.append(2)
            i += 1
        elif l[i] in dep_hrsa_svara:
            i += 1
        elif l[i] in vyanjan or l[i] in nuqta_vyanjan:
            numeral.append(1)
            i += 1
        elif l[i] in dep_dirgh_svara:
            numeral.pop(-1)
            numeral.append(2)
            i += 1
        elif l[i] == halant:
            if l[i+1] == 'ह':
                i += 2
                continue
            if len(numeral) == 1:
                numeral.pop(-1)
                i += 1
            else:
                numeral[-2] = 2
                i += 2
    return numeral
 
with codecs.open("testing.txt", encoding='utf-8') as f:
    lines = f.readlines()
while '\n' in lines:
  lines.remove('\n')
for i in lines:
    i = i.rstrip('\n')  # removing '\n' that is appended at the end of each string read by readlines
lsen = []  # this is a list of lists
# each such member is a list containing words of a sentence without special character
for i in lines:
    if i == []:
        continue
    lsen.append(i.split())
lsen = []  # this is a list of lists
# each such member is a list containing words of a sentence without special character
for i in lines:
    lsen.append(i.split())
ans = []
for sen in lsen:  # iterating over the lists of words
    if sen == []:
        continue
    subans = []  # this would store the list of scansion for each word of a sentence
    for word in sen:
        if word == ',' or word == '।' or word == '॥' or (word>='1' and word<='9') or word == '-':
            continue
        else:
            subans.append(matrabharcalculator(word))
    ans.append(subans)
print(ans)

