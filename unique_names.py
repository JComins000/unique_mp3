from ID3 import *
from os import listdir, rename

def shared_end_substring(str1, str2):
	for i in range(len(str1)):
		idx = -i-1
		if not str1.endswith(str2[idx:]):
			return str1[-i:], -i

def shared_start_substring(str1, str2):
	for i in range(len(str1)):
		idx = i+1
		if not str1.startswith(str2[:idx]):
			return str1[:i], i

extension = ".mp3"
mp3s = [f for f in listdir('.') if f[-4:] == '.mp3']
cut, cutoff = shared_end_substring(*mp3s[0:2])
start, startoff = shared_start_substring(*mp3s[0:2])

for mp3 in mp3s:
	if not mp3.endswith(cut):
		cut, cutoff = shared_end_substring(cut, mp3)
	if not mp3.startswith(start):
		start, startoff = shared_start_substring(start, mp3)

for mp3 in mp3s:
	name = mp3[startoff:cutoff]
	rename(mp3, name+extension)
	try:
		id3info = ID3(name+extension)
		id3info['TITLE'] = name
	except InvalidTagError, message:
		print "Invalid ID3 tag:", message
