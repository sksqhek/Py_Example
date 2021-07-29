import re

str='hello/ world, sarah- good'

words = re.findall('(\w+)(\/|,|-|)',str)

print(words)