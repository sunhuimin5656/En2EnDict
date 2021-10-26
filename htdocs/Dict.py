#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import cgi, cgitb 

# 创建 FieldStorage 的实例化
form = cgi.FieldStorage() 
# 获取数据
word  = form.getvalue('word')
explain = form.getvalue('explain')

print('<html>')
print('<head><title>Dict</title></head>')
print('<body>')
print('<form id="DictPage" action="Dict.html" method="post"></form>')
print('<form id="HistoryPage" method="post"></form>')
print('<div style="text-align:center;">')
print('<h2>在线词典</h2>')
print('<input type="text" name="word" placeholder="请输入单词" form="DictPage" style="height:25px;width:200px;" ')
print("value=\"%s\">" % (word))
print('<input type="submit" name="translate" value="翻译" form="DictPage"><br>')
print('<textarea readonly placeholder="显示区" style="height:100px;width:250px;resize:none">')
print("%s" % (explain))
print('</textarea><br>')
print('<input type="submit" name="history" value="历史记录" form="HistoryPage" formtarget="_blank">')
print('</div>')
print('</body>')
print('</html>')
