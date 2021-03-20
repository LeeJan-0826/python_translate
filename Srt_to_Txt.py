import shutil
import os
path = r'/translate_txt/input_srt'
path2 = r'C:\\Users\haizeiwang\\Documents\\Tencent Files\\1299989673\\FileRecv\\pythonProject1\\Auto_Translate\\translate_txt\\input_txt'
# def text_create(name, msg):
#     desktop_path = "D:\\pythonProject1\\translate_txt\\input_txt\\"  # 新创建的txt文件的存放路径
#     full_path = desktop_path + name  # 也可以创建一个.doc的word文档
#     file = open(full_path, 'w')
#     file.write(msg)  # msg也就是下面的Hello world!
#     file.close()
#
# def change_srt_to_txt(srt_name):
#     list1 = list(srt_name)
#     n = len(srt_name)
#     list1[n-1] = 't'
#     list1[n-2] = 'x'
#     list1[n-3] = 't'
#     txt_name = ''.join(list1)
#     return txt_name
def copy_files():
    for foldName, subfolders, filenames in os.walk(path):
           for filename in filenames:
                if filename.endswith('.srt'):
                    # new_name = os.path.split(filename)[1]
                    new_name=filename.replace('.srt', '.txt')
                    shutil.copyfile(os.path.join(foldName, filename), os.path.join(path2, new_name))
                    # print(filename, "copied as", new_name)           #输出提示
if __name__ == '__main__':
    copy_files()