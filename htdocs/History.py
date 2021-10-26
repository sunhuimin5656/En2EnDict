#!/usr/bin/python3
# -*- coding: UTF-8 -*-

print('<html>')
print('<head>')
print('<title>History</title>')
print('</head>')
print('<body>')
print('<form id="HistoryPage" method="post"></form>')
print('<h2>历史记录</h2>')
print('<ul>')

with open('test.txt', 'r') as fp:
    llist = fp.readlines()
    for i in range(0, len(llist)):
        llist[i] = llist[i].rstrip('\n')
        print("<li>%s" % (llist[i]))

print('</ul>')
print('<input type="submit" name="clear" value="清除" form="HistoryPage" formtarget="_blank" >')
print('</body>')
print('</html>')
