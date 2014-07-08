#!/usr/bin/env python

"""
@copyright: AlertAvert.com (c) 2012. All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Collection of code utilities developed while following the Crypt course on
Coursera.org:
    https://class.coursera.org/crypto-2012-002/class/index

@author: Marco Massenzio (m.massenzio@gmail.com)
         Created on Jul 14, 2012
"""





# Week 1 - Problem set

def resolve_q7():
    def encrypt(key, msg):
        secret = []
        for i, k in enumerate(key):
            secret.append(k ^ ord(msg[i]))
        return secret

    _cipher = r'6c73d5240a948c86981bc294814d'
    cipher = []
    for i in xrange(0, len(_cipher) / 2):
        cipher.append(chr2hex(_cipher[2 * i]) * 16 + chr2hex(_cipher[2 * i + 1]))

    plaintext = r'attack at dawn'
    key = encrypt(cipher, plaintext)

    # Encode the new secret message
    plaintext = r'attack at dusk'
    cipher = encrypt(key, plaintext)
    print [hex(c) for c in cipher]


# Week 2 - Problem Set


def resolve_q4():
    F2_OUT = {'1': ["4af532671351e2e1", "87a40cfa8dd39154"],
              '2': ["7c2822ebfdc48bfb", "325032a9c5e2364b"],
              '3': ["e86d2de2e1387ae9", "1792d21db645c008"],
              '4': ["7b50baab07640c3d", "ac343a22cea46d60"]
            }
    for k in F2_OUT:
        res = xor(F2_OUT[k][0], F2_OUT[k][1])
        print "%s] %s" % (k, res)


def resolve_q8():
    MSGS = ['The significance of this general conjecture, assuming its truth, is easy to see. It means that it may be feasible to design ciphers that are effectively unbreakable.',
            'If qualified opinions incline to believe in the exponential conjecture, then I think we cannot afford not to make use of it.',
            'We see immediately that one needs little information to begin to break down the process.',
            'In this letter I make some remarks on a general principle relevant to enciphering in general and my machine.'
           ]
    for m in MSGS:
        print '%d: %s' % (len(m), m)

if __name__ == '__main__':
    resolve_q7()