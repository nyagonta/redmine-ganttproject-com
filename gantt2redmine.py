# -*- coding: utf-8 -*-
import sys # モジュール属性 argv を取得するため
import datetime
from redmine import Redmine

argvs = sys.argv  # コマンドライン引数を格納したリストの取得
argc = len(argvs) # 引数の個数

# デバッグプリント
print argvs
print argc
print
if (argc != 3):   # 引数が足りない場合は、その旨を表示
    print 'Usage: # python %s issue_id status_id' % argvs[0]
    quit()         # プログラムの終了

redmine = Redmine('http://localhost/redmine', key='03928143a9d038873b00e1ffcb9e13f7abccd232')

issue = redmine.issue.get(argvs[1])
issue.status_id = argvs[2]
issue.save()
