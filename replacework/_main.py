import os

import replacework
import doc_replace
import name_replace

# 多改多
if __name__ == '__main__':
    # 需要的文件名
    list = []
    # 要在word 内替换进去的文字
    list1 = []
    # 要在word 内替换进去的文字
    list2 = []
    # 文件所在文件夹路径 作业文件放到doc文件夹下即可
    path = r'C:\Users\86413\PycharmProjects\pythonProject3\doc'
    filelist = os.listdir(path)
    print(filelist)
    k = 0

    # 按照字典序排序 需要保证实验报告在文件夹中的顺序与实验报告顺序一致
    sorted(filelist)
    print(list[0])
    for ll in list:
        i = 0
        print(list[k])
        # 创建一个以list[k]为名字的文件夹
        folder = r'C:\Users\86413\PycharmProjects\pythonProject3\target' + '/' + list[k] + '/'
        print(folder)
        if not os.path.exists(folder):
            os.makedirs(folder)
        for s in filelist:
            oldname = path + os.sep + filelist[i]
            # print(oldname)
            pos = oldname.find('.')
            # 新的文件名 注意实验不能超过十,即该处自动取原名字的最后一位作为编号，如果oldname[:3]即取前三位
            newname = filelist[i][:3] + list[k]
            # print(filelist[i][:3])
            # print(newname)
            username = name_replace.replace_name(folder, oldname, newname)
            print(username)
            # 需要被修改的字符串 , 如果有多处，多写两个就行了
            doc_replace.replace_doc("xxx", list1[k], username)
            doc_replace.replace_doc("xxxx", list2[k], username)
            i += 1
        k += 1
