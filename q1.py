# find how many slices of the string is there (cake slices)
# EQUATE consecutive slices

# without leaving any leftovers [IMPORTANT]
# in s = 'ababababab'
# even though consecutive string slices ['abab'], at the end, there are leftovers
# so, condition to check if s[-(len(sub_str):-1]==sub_str

def solution(s):
      dupl=s+' '                                        # because in range (string[-1] won't be included) (-1 now becomes -2)
      l=len(s)
      for i in range(1,(l//2+1)):                       # for 2  cake parts, till l//2, string slice ('abccbaabccba')
            if s[0:i]==s[i:2*i]:                        # CONSECTIVE SLICE CHECK (MAIN)
                  sub_str=s[0:i]
                  len_sub=len(sub_str)
                  if dupl[-(len_sub+1):-1]==sub_str:      # for no leftovers condition (+1 because of dupl=s+' ')
                        no_of_slices = s.count(sub_str)
                        return no_of_slices
                  else:
                        pass
                  
            elif i==(l//2):
                return 1

            else:
                  pass

print(solution('abcabcabcabc'))
print(solution('abccbaabccba'))
print(solution('abbbbbbbbbba'))   # no repeating patterns, return 1     


# below after considering no leftovers condition

# no need to make list of all repeating, as function call is returned after first sub_str found.
# therefore already max counts
# eg: 'abababababab')
# 'abab' parts - 3
# 'ab' parts - 6
# therefore, already returns at 'ab'


