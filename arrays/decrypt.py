'''
An infamous gang of cyber criminals named “The Gray Cyber Mob”, which is behind many hacking attacks and drug trafficking, has recently become a target for the FBI. After intercepting some of their messages, which looked like complete nonsense, the agency learned that they indeed encrypt their messages, and studied their method of encryption.

Their messages consist of lowercase latin letters only, and every word is encrypted separately as follows:

Convert every letter to its ASCII value. Add 1 to the first letter, and for every letter from the second to the last, add to it the value of the previous letter. Subtract 26 from every letter until it is in the range of lowercase letters a-z in ASCII. Convert the values back to letters.

For instance, to encrypt the word “crime”

Decrypted message:	c	r	i	m	e
Step 1:	99	114	105	109	101
Step 2:	100	214	319	428	529
Step 3:	100	110	111	116	113
Encrypted message:	d	n	o	t	q

'''

def get_in_range(ascii_val):
  while(True):
     if ascii_val >= ord('a') and ascii_val <= ord('z'):
        return ascii_val
     ascii_val -= 26


def decrypt(word):
   rolling_sum = 0
   res = []
   for idx, val in enumerate(word):
       if not idx:
          rolling_sum += 1 + ord(val)
       else:
          rolling_sum += ord(val)
       res.append(chr(get_in_range(rolling_sum)))
   return "".join(res)

print decrypt("crime")
