'''manipulating text or data is big thing.'''
import re,sys

version = "0.0.1"
ruleMap = {}
def ruleOfRe():
	ruleList = []
	with open("./ruleList","r") as fp:
		for line in fp.readlines():
			dicItem = {}
			line = line.strim()
			l = line.split(';')
			dicItem['rule'] = l[0]
			dicItem['des'] = l[1]
			dicItem['example'] = l[2]
			ruleList.append(dicItem)
	return ruleList
def findRule(rules,Onerule):
	print rules
	print Onerule
	for rule in rules:
		if rule['rule'] == Onerule:
			print "rule:"+r["rule"]
			print "describle:"+r["des"]
			print "example:"+r["example"]
			return
	print "can not found!"
	return
def pipeSymbol():
	'''(|) is pipe symbol '''
	print "this a pipe symbol example"
	srcString = raw_input("input srcString(any string is ok!):")
	pattern = raw_input("input pattern(like abc|def):")
	if -1 == pattern.find('|'):
		print "input worng"
	try:
		m = re.match(pattern, srcString)
		print "match is %r" % (m.group(),)
	except:
		print "match fail!"
def pointSymbol():
	'''(.) is point symbol'''
	print "this a point symbol example"
	srcString = raw_input("input srcString(any string is ok!):")
	pattern = raw_input("input pattern(like abc.def):")
	if -1 == pattern.find('.'):
		print "input worng"
	try:
		m = re.match(pattern, srcString)
		print "match is %r" % (m.group(),)
	except:
		print "match fail!"
def initMap():
	global ruleMap
	ruleMap['|'] = pipeSymbol
	ruleMap['.'] = pointSymbol
def main():
	global ruleMap
	initMap()
	allrules = ruleOfRe()
	for arg in sys.argv:
		if arg == "-v":
			print version
			return
		elif arg == "-h":
			for r in allrules:
				print "rule:"+r["rule"]
				print "describle:"+r["des"]
				print "example:"+r["example"]
			return
	try:
		ruleString = raw_input("which rule do you wanna try:")
		print "1.you wanna learn about it?"
		print "2.try to do matching!"
		choice = raw_input("which do you like(1 or 2)?")
		try:
			i = int(choice)
			if i < 1 or i > 2:
				print "there is no such option!"
				return
		except:
			print "input worng"
			return
		if i == 1:
			findRule(allrules,ruleString)
		else:
			ruleFunc = ruleMap[ruleString]
			ruleFunc()
	except Exception:
		print "threre is no "+ruleString+" rule!"
if __name__ == '__main__':
	main()
