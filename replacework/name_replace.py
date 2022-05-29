import os
import shutil

import doc_replace


def replace_name(path, oldname, newname):
    # 获取该目录下所有文件，存入列表中
    pos = oldname.find('.')
    print(oldname)
    # 设置新文件名
    newname = path + os.sep + newname + '.doc'
    print(newname)
    shutil.copyfile(oldname,newname)
    # os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    print(oldname, '======>', newname)

    return newname
