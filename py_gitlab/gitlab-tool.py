# -*- coding: utf-8 -*-
__Author__ = "gseng"
__Date__ = '2020/02/29 13:46'

import gitlab
import string_tool

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

project_name = "seewo-iot-app-remote"
namespace_scope = "media/ddc/dev/be"

projects = gl.projects.list(search=project_name)
for p in projects:
    if p.namespace.get('full_path') == namespace_scope:
        # branches = p.branches.list()
        # print(branches)
        # print(p)
        result = p.repository_compare('test', 'dev')

        # print("------------------------------------------------------\n")
        print(len(result['diffs']))
        # print("------------------------------------------------------\n")
        for file_diff in result['diffs']:
            pass
            #print(file_diff)
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
