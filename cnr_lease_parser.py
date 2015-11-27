#!/usr/bin/python

import re
import argparse

argparser = argparse.ArgumentParser(description="CNR scope listLeases parser")
argparser.add_argument("--file","-f", help="input file",required=True)
argparser.add_argument("--date","-d", help="renewal date MON,DAY",required=True)
args = argparser.parse_args()

fl = open(args.file,'r')

lower = 0
bigger = 0

re_month,re_day = args.date.split(",")

for line in fl:
	ip = re.search('^(([0-9]{1,3})\.?)*',line).group()
	time = re.search('lease-renewal-time="([A-Za-z0-9 :]*)"',line)
	if time and ip is not None:
		date = re.search('(Nov|Dec) +([0-9]{1,2})',time.group(1))
		if date is not None:
			month = date.group(1)
			day = int(date.group(2))
			if month == re_month and day > int(re_day):
				bigger += 1
				print('bigger {0}: {1} {2}'.format(ip,month,day))
			else:
				lower += 1
				print('lower {0}: {1} {2}'.format(ip,month,day))

fl.close()

total = """------------
bigger: {0}
lower: {1}
total {2}
""".format(bigger,lower,bigger+lower)

print(total)
