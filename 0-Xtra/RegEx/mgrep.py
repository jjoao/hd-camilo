import re, sys
# python3 mgrep in.txt "\n<p>\n(^.*$)\n</p>" "\n<h2>\1</h2>'" out.txt
# needs scapping: | \
f_i = sys.argv[1]

r_i = r'{}'.format(sys.argv[2])
r_o = r'{}'.format(sys.argv[3])

f_o = sys.argv[4]; f_o = open(f_o, 'w'); f_o.write(re.sub(r_i, r_o, open(f_i, "r").read(), flags=re.M)); f_o.close()