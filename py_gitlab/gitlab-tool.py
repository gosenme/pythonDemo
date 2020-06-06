# -*- coding: utf-8 -*-
__Author__ = "gseng"
__Date__ = '2020/02/29 13:46'

import gitlab

url = "https://gitlab.gz.cvte.cn"
token = "ABAE9gRzA1MpDmrpwnzb"

# 登录
gl = gitlab.Gitlab(url, token)

# 获取第一页project
# projects = gl.projects.list()
# 获取所有的project
# projects = gl.projects.list(all=True)


# for p in gl.projects.list(all=True, as_list=False):
#    print(p.name, p.id)

projects = ["seewo-iot-app-remote", "seewo-ucp-core", "seewo-iot-app-stat", "seewo-iot-app-file", "seewo-iot-app-proxy",
            "seewo-iot-app-wake", "seewo-iot-app-admin",
            "seewo-iot-timer-monitor"]
for pp in projects:
    project = gl.projects.list(search=pp)
    # project_name = "seewo-iot-app-remote,seewo-ucp-core"
    namespace_scope = "media/ddc/dev/be"
    # project = gl.projects.list(search=project_name.split(","))
    for p in project:
        if p.namespace.get('full_path') == namespace_scope:
            # branches = p.branches.list()
            # print(branches)
            # print(p)
            result = p.repository_compare('test', 'dev')
            if len(result['diffs']) > 0:
                # print("------------------------------------------------------>")
                print(p.name + "变量数量:" + str(len(result['diffs'])))
                #if p.name == 'seewo-iot-app-admin':
                r = p.mergerequests.create({'source_branch': 'dev', 'target_branch': 'test', 'title': '1.1.8 A1合并'})
                print(r.web_url)
                # print("------------------------------------------------------>")
            else:
                print(p.name + ":代码没有变更")
                # for file_diff in result['diffs']:
                # pass
            # print(file_diff)
            # 获取文件完整路径
        #     old_path = file_diff.get('old_path')
        #     # 不是新文件
        #     new_file = file_diff.get('new_file')
        #     # 不是文件重命名
        #     renamed_file = file_diff.get('renamed_file')
        #     # 不是删除文件
        #     deleted_file = file_diff.get('deleted_file')
        #     if old_path.endswith('.java') and not new_file and not renamed_file and not deleted_file:
        #         print("类名:", old_path.split('java/')[1])
        #         print("**********************************")
        #         diff_list = file_diff.get('diff').split('\n')
        #         i = 0
        #         base_index = 0
        #         for diff in diff_list:
        #             if diff.startswith('@@'):
        #                 i = 0
        #                 print("提示行:", diff)
        #                 temp1 = string_tool.get_str_btw(diff, "@@", "@@")
        #                 temp2 = temp1.split("+")
        #                 temp3 = temp2[1].split(",")
        #                 base_index = int(temp3[0])
        #                 print(">>>>>>>>>>>>>:", temp3[0])
        #                 continue
        #             if diff.startswith('+') or diff.startswith('-'):
        #                 print("变更行:", diff)
        #                 print("变更行号码:", base_index + i)
        #                 i = i + 1
        #                 continue
        #             print("正常行:", diff)
        #             i = i + 1
        #        print("--------------------------------------------------------------")

# projects = gl.projects.list(visibility='public')
# for p in projects:
#     print(p.name, p.id)
