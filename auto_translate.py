# 读取TXT文档
import os
input_dir = '/translate_txt/input_txt'
desktop_path = "/translate_txt/output_txt\\"  # 新创建的txt文件的存放路径
def read_txt(path):
    '''实现TXT文档的读取，一次将内容全部取出'''
    content = ''
    with open(path) as f:
        content = f.read()
    return content
# 也可以用readline()读取每一行
import urllib.request
import urllib.parse
import json


# 有道翻译方法
def youdao_translate(content):
    '''实现有道翻译的接口'''
    youdao_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    data = {}
    data['i'] = content
    data['from'] = 'AUTO'
    data['to'] = 'AUTO'
    data['smartresult'] = 'dict'
    data['client'] = 'fanyideskweb'
    data['salt'] = '1525141473246'
    data['sign'] = '47ee728a4465ef98ac06510bf67f3023'
    data['doctype'] = 'json'
    data['version'] = '2.1'
    data['keyfrom'] = 'fanyi.web'
    data['action'] = 'FY_BY_CLICKBUTTION'
    data['typoResult'] = 'false'
    data = urllib.parse.urlencode(data).encode('utf-8')

    youdao_response = urllib.request.urlopen(youdao_url, data)
    youdao_html = youdao_response.read().decode('utf-8')
    target = json.loads(youdao_html)

    trans = target['translateResult']
    ret = ''
    for i in range(len(trans)):
        line = ''
        for j in range(len(trans[i])):
            line = trans[i][j]['tgt']
        ret += line + '\n'
    return ret


# 创建一个txt文件，文件名为mytxtfile,并向文件写入msg
def text_create(name, msg):

    full_path = desktop_path + name  # 也可以创建一个.doc的word文档
    file = open(full_path, 'w')
    file.write(msg)  # msg也就是下面的Hello world!
    file.close()


    # 修改符号
def change_txt_content(content):
    # 首先找出含有'——'部分的位置记录位置，再修改并插入
    sub = '——'
    import re
    num_dir = [substr.start() for substr in re.finditer(sub, content)]
    # print(type(num_dir[0]))
    num_dir.reverse()
    # rint(num_dir)
    # 加空格，改成'--'
    # 因为content是str类型的元素，无法在内部插入空格，只能改成list类型，修改后再改回str类型
    content_list = list(content)
    # 修改'——'和添加空格，并且因为从数组后面开始取比较方便，
    for i in num_dir:
        # print(i)
        content_list[i] = '-'
        content_list[i+1] = '-'
        content_list.insert(i, ' ')
    content = ''.join(content_list)


    # 删空格
    sub_1 = '- -'
    num_dir_1 = [substr.start() for substr in re.finditer(sub_1, content)]
    num_dir_1.reverse()
    content_list_1 = list(content)
    for i in num_dir_1:   # 在数组里面轮流取值
        del content_list_1[i + 1]
        del content_list_1[i + 2]
    content = ''.join(content_list_1)
    return content

# 讲一个txt翻译完毕
def translate(txt_dir_name):
    txt_content = read_txt(txt_dir_name)
    translate_content = youdao_translate(txt_content)
    change_txt = change_txt_content(translate_content)
    txt_name = os.path.split(txt_dir_name)[1]
    text_create(txt_name, change_txt)

def get_path(txt_dir):
    pic_path=[]
    for path in os.listdir(txt_dir):
        real_path = os.path.join(txt_dir, path)
        pic_path.append(real_path)
    return pic_path
def get_path_name(txt_dir):
    pic_path = get_path(txt_dir)
    for i in range(0, len(pic_path)):
        pic_path[i] = os.path.split(pic_path[i])[1]
    # print(pic_path)
    return pic_path

def is_exist(i, output_dir):
    list_02 = get_path_name(output_dir)
    # print(list_02)
    flag = 0
    if i in list_02:
        flag = 1
    # 存在返回1，不存在返回0
    if(flag):
        return 1
    else:
        return 0
if __name__ == '__main__':
    list_txt_dir = get_path(input_dir)
    # print(list_txt_dir)
    for i in list_txt_dir:
        j = os.path.split(i)[1]
        # print(j)
        if is_exist(j, desktop_path):
            print('had translated')
        else:
            translate(i)
