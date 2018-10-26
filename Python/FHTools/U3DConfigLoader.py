import xlrd
import tkinter
import tkinter.filedialog as tf
import os


# 首字母大写
def capitalize_ex(s):
    if s == 'id':
        return "ID"
    return s[0].capitalize() + s[1:]


# 类型制作
def make_type(ftype, fname):
    has_new_struct = False
    type_name = ""

    if ftype.find("int") == 0:
        type_name = "int32"
    elif ftype.find("string") == 0:
        type_name = "string"
    elif ftype.find('{int type:int id:int count}') == 0:
        type_name = "common.Item"
    else:
        type_name = capitalize_ex(fname) + "Data"
        has_new_struct = True

    i = ftype.rfind("[]")
    if i == len(ftype) - 2:
        type_name = "[]" + type_name

    return (has_new_struct, type_name)


# 分支类型制作
def make_branch_struct(type_name, tType):
    type_name = type_name.replace("[]", "")
    tType = tType.replace("[]", "")
    tType = tType.replace("{", "")
    tType = tType.replace("}", "")
    tlist = tType.split(':')

    branch_struct = '//%s ...\ntype %s struct {\n' % (
        type_name, type_name)
    for it in tlist:
        temp = it.split(" ")
        branch_struct += '\t' + capitalize_ex(temp[1]) + '\t' + temp[0]
        branch_struct += "\t`json:\"%s\"`\n" % temp[1]
    branch_struct += "}\n\n"
    return branch_struct


FILE_PATH = tf.askopenfilename()
if not FILE_PATH:
    os._exit(0)
FILE_NAME = FILE_PATH.split("/")[-1].split(".")[0]

content = 'package commonex\n\nimport (\n\t"eagle_server_base/common"\n\t"encoding/json"\n\t"fmt"\n\t"os"\n)\n\n'

# 操作开始
with xlrd.open_workbook(FILE_PATH) as book:
    sheet: xlrd.sheet.Sheet = book.sheet_by_index(0)
    field_index = [i for i, v in enumerate(
        sheet.row_values(3)) if v.find("server") >= 0]
    fields = [(sheet.row_values(1)[i], sheet.row_values(2)[i])
              for i in field_index]

    brunch_struct_list = list()

    main_struct = '//%sJSON ...\ntype %sJSON struct {\n' % (
        FILE_NAME, FILE_NAME)
    for ftype, fname in fields:
        tType = make_type(ftype, fname)
        main_struct += '\t' + \
            capitalize_ex(fname) + '\t' + tType[1]
        main_struct += "\t`json:\"%s\"`\n" % fname
        if tType[0]:
            brunch_struct_list.append(make_branch_struct(tType[1], ftype))
    main_struct += "}\n\n"

    # 添加分支类型
    for bl in brunch_struct_list:
        content += bl

    # 添加主类型
    content += main_struct

    # 添加map
    content += f"//{FILE_NAME}MapConfig  ...\nvar {FILE_NAME}MapConfig map[int32]*{FILE_NAME}JSON\n\n"

    # 添加Load函数
    content += f"//Load{FILE_NAME} ...\nfunc Load{FILE_NAME}() "
    content += '{\n\tfmt.Println("load %s config")\n\n' % FILE_NAME
    content += f'\tdata := LoadJsonData("./config/{FILE_NAME}.json")\n\n'
    content += '\tif nil == data {\n\t\tfmt.Println("load %s error")\n\t\tos.Exit(1)\n\t\treturn\n\t}\n\n' % (
        FILE_NAME)
    content += f"\tjsonData := make([]*{FILE_NAME}JSON, 0)\n\terr := json.Unmarshal(data, &jsonData)\n"
    content += '\tif err != nil {\n\t\tfmt.Println("%s json.Unmarshal err:", err)\n\t\tfmt.Println("config data:", string(data))\n' % FILE_NAME
    content += "\t\tos.Exit(1)\n\t\treturn\n\t}\n\t%sMapConfig = make(map[int32]*%sJSON)\n\n" % (
        FILE_NAME, FILE_NAME)
    content += '\tfor _, v := range jsonData {\n\t\t%sMapConfig[v.ID] = v\n\t}\n\tfmt.Println("load %s success!")\n}\n\n' % (
        FILE_NAME, FILE_NAME)

    # 添加获取函数
    content += f"//Get{FILE_NAME}ByID 用ID获取引导配置\n"
    content += "func Get%sByID(id int32) *%sJSON {\n\tif v, ok := %sMapConfig[id]; ok {\n" % (
        FILE_NAME, FILE_NAME, FILE_NAME)
    content += "\t\treturn v\n\t}\n\treturn nil\n}\n"

with open(f"load{FILE_NAME}.go", "w", encoding="utf8") as f:
    f.write(content)

os.system('pause')