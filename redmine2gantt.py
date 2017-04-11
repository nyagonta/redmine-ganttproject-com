# -*- coding: utf-8 -*-
import datetime
from redmine import Redmine
from redmine.exceptions import ResourceNotFoundError

redmine = Redmine('http://localhost/redmine', key='03928143a9d038873b00e1ffcb9e13f7abccd232')

projects = redmine.project.all()
print (dir(projects))
for x in projects:
    print x

project = redmine.project.get('test')

print(u'ID,名前,開始日,終了日,期間,進捗,先行タスク,アウトライン番号,メモ').encode('utf-8')

# チケット番号の昇順にループ処理される

try:
    issues = redmine.issue.filter(assigned_to_id='me', sort='project:desc')
    for issue in issues:

        print issue.project

        relations = redmine.issue_relation.filter(issue_id=issue.id)
        follows = "0"
        for x in relations:
#            print "type:%s, to_id:%s, id:%s" % (x.relation_type, x.issue_to_id, x.issue_id)
            if x.relation_type == 'precedes' and x.issue_to_id == issue.id:
                if follows == "0":
                    follows = str(x.issue_id)
                else:
                    follows = str(follows) + ';' + str(x.issue_id)
                if x.delay > 0:
                    follows = str(follows) + '-FS=P' + str(x.delay) + 'D'

#""        print ('%d,%s,%s,%s,%s,%s,%s,0,%s' % (issue.id, issue.subject, (issue.start_date).strftime('%y/%m/%d'), (issue.due_date).strftime('%y/%m/%d'), (issue.due_date - issue.start_date).days, issue.done_ratio, follows, issue.id)).encode('utf-8')
        print ('%d,%s,%s'
                % (
                    issue.id,
                    issue.subject,
                    (issue.start_date).strftime('%y/%m/%d')
                )).encode('utf-8')

except (ResourceNotFoundError):
    print ('Not found')


# ID,名前,開始日,終了日,期間,進捗,Cost,責任者,先行タスク,アウトライン番号,リソース,ウェブリンク,メモ
# 0,タスク_1,17/01/30,17/01/30,1,100,0,,,1,,,
# 1,タスク_2,17/01/31,17/01/31,1,90,0,,0,2,,,
# 2,タスク_3,17/02/01,17/02/01,1,80,0,,,3,,,
