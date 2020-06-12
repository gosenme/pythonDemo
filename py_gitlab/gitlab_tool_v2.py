# -*- coding: utf-8 -*-
__Author__ = "gseng"
__Date__ = '2020/02/29 13:46'

import gitlab
from configparser import ConfigParser
import json

config = ConfigParser()
config.read("projects.ini", encoding='UTF-8')
userToken = config['DEFAULT']['user_token']
devVersion = config['DEFAULT']['dev_version']
testTimes = config['DEFAULT']['test_times']
mergeRequestsTitle = config['DEFAULT']['merge_requests_title']
merge_requests = config['DEFAULT']['mergerequests']
projects = config['project']['projects']
allProject = json.loads(projects)


def compare_project():
    for project in allProject['projects']:
        gl = gitlab.Gitlab(project["project_url"], userToken)
        ps = gl.projects.list(search=project["project_name"])
        for p in ps:
            if p.namespace.get('full_path') == project["project_scope"]:
                # print(project["project_name"] + "-------------------------------start------------------------------")
                result = p.repository_compare('test', 'dev')
                if len(result['diffs']) > 0:
                    # print(p.name + "变量数量:" + str(len(result['diffs'])))
                    mrs = p.mergerequests.list(state='opened')
                    if len(mrs) <= 0:
                        if merge_requests == 'YES':
                            pr = p.mergerequests.create(
                                {'source_branch': project["source_branch"],
                                 'target_branch': project["target_branch"],
                                 'title': mergeRequestsTitle})
                            print('提交PR链接:%s' % pr.web_url)
                    else:
                        for r in mrs:
                            print("open 中的PR" + r.web_url)
                    for commit in result['commits']:
                        if not commit['title'].find('Merge branch') >= 0:
                            print('负责人：' + commit['author_email'] + ' 变更内容： ' + commit['title'])
                    print(project["project_name"] + "-------------------------------------------------------------")
