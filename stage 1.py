# print("* * * *")
#
# print("*     *")
#
# print("*     *")
#
# print("* * * *")
#
# dt="123456"
# print(len(dt))
# print(dt.upper())
# print(dt[2:-1])
#
# print('word = word.replace("\u0301", " ")')  #  delete stress symbols from the word
# print('Those in favor, say "aye"')
#
# print("Wow! It's amazing!")
#
# print('It\'s time for tea!' )
#
# print("He said: \"So what?\"")
#
# print('word = word.replace("\u0301", "")')  # delete stress symbols from the word
# print("\\")
# print()
# a="""word = word.replace("\u0301", "")"""
# print(a)

# s = """Gur Mra bs Clguba, ol Gvz Crgref
#
# Ornhgvshy vf orggre guna htyl.
# Rkcyvpvg vf orggre guna vzcyvpvg.
# Fvzcyr vf orggre guna pbzcyrk.
# Pbzcyrk vf orggre guna pbzcyvpngrq.
# Syng vf orggre guna arfgrq.
# Fcnefr vf orggre guna qrafr.
# Ernqnovyvgl pbhagf.
# Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
# Nygubhtu cenpgvpnyvgl orngf chevgl.
# Reebef fubhyq arire cnff fvyragyl.
# Hayrff rkcyvpvgyl fvyraprq.
# Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
# Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
# Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
# Abj vf orggre guna arire.
# Nygubhtu arire vf bsgra orggre guna *evtug* abj.
# Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
# Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
# Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""
#
# d = {}
# for c in (65, 97):
#     for i in range(26):
#         d[chr(i+c)] = chr((i+13) % 26 + c)
#
# print("".join([d.get(c, c) for c in s]))
#
# import this
# import antigravity

# from math import pi
# π = pi
# r = 6
# area = π * r**2
#
# résumé = 'knows Python'
# 'Python' in résumé
from antigravity import geohash
# Your location, a date and that date's (or most recent) DJIA opening.
geohash(37.421542, -122.085589, b'2005-05-26-10458.68')
37.857713 -122.544543