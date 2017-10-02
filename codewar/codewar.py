def find_nb(m):
	if m - 1 == 0:
		return 1
	if (m - 1) % 3 == 0:
		pre_val = find_nb((m-1)/3)
		if pre_val > 0:
			return 1 + pre_val
		else:
			return pre_val
	return -1

# print(find_nb(1071225))
# print('ok')

def is_isogram(str):
	if len(str) <= 1:
		return True
	ss = sorted(str.lower())
	print(ss)
	i = len(ss)
	while i-2>=0:
		if(ss[i-1] == ss[i-2]):
			return False
		i = i - 1
	return True

def high_and_low(numbers):
    rs = sorted([int(x) for x in numbers.split(' ')])

    print(rs)
    return '{} {}'.format(rs[-1], rs[0])

# print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))
def openOrSenior(data):
	rsList = []
	for age, handicap  in data:
		if age >=55 and handicap > 7:
			rsList.append('Senior')
		else:
			rsList.append('Open')
	return rsList

def another(data):
	return ['Senior' if age >=55 and handicap > 7 else 'Open' for age, handicap in data]

def digital_root(n):
	s = sum([int(x) for x in str(n)])
	if len(str(s)) > 1:
		return digital_root(s)
	return s

def sum_two_smallest_numbers(numbers):
    return sum(sorted(numbers)[:2])

def longest(s1, s2):
    return ''.join(sorted(set(s1+s2)))

# print(longest("aretheyhere", "yestheyarehere"))

def countBits(n):
	return sum([int(x) for x in str('{:b}'.format(n))])
	# return bin(n).count("1") -- the best

def song_decoder(song):
    # return [x for x in song.replace("WUB",' ').split(' ') if len(x)>0]
    return ' '.join(song.replace("WUB",' ').split())

# print(song_decoder('AWUBWUBWUBBWUBWUBWUBC'))
def dig_pow(n, p):
    n_list = [int(x) for x in str(n)]
    sum = 0
    for d in n_list:
    	sum += d**p
    	p += 1
    if sum%n == 0:
    	return int(sum/n) 
    return -1

# k, fail = divmod(sum(int(d)**(p + i) for i, d in enumerate(str(n))), n) -- the best
def find_next_square(sq):
    from math import sqrt
    return int((sqrt(sq)+1)**2) if int(sqrt(sq)) ** 2 == sq else -1
    # if sqrt(sq) ** 2 == sq:
    # 	return int((sqrt(sq)+1)**2)
    # return -1

def find_missing_letter(chars):
	return [chr(ord(c)-1) for i, c in enumerate(chars) if ord(c) - i != ord(chars[0])][0]

# print(find_missing_letter(['a','b','d','e']))

def comp(array1, array2):
	if (array1 is None or array2 is None or len(array1) != len(array2)):
		return False

	t = sorted(array2)
	return True if len([x for i, x in enumerate(sorted(array1)) if t[i] != x**2]) == 0 else False

# return None not in (a1,a2) and [i*i for i in sorted(a1)]==sorted(a2) //best solution

# a = ["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]
# test.assert_equals(dirReduc(a), ['WEST'])
def dirReduc(arr):
	
