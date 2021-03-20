import shutil
import os
path = r'/translate_txt/output_txt'
path2 = r'C:\\Users\haizeiwang\\Documents\\Tencent Files\\1299989673\\FileRecv\\pythonProject1\\Auto_Translate\\translate_txt\\output_srt'
# # 将翻译好的txt文件重新转换成srt文件
# def change_txt_to_srt(txt_name):
#     list1 = list(txt_name)
#     n = len(txt_name)
#     list1[n-1] = 't'
#     list1[n-2] = 'r'
#     list1[n-3] = 's'
#     txt_name = ''.join(list1)
#     return txt_name
# def text_create(name, msg):
#     desktop_path = "D:\\pythonProject1\\translate_txt\\output_srt\\"  # 新创建的txt文件的存放路径
#     full_path = desktop_path + name  # 也可以创建一个.doc的word文档
#     file = open(full_path, 'w')
#     file.write(msg)  # msg也就是下面的Hello world!
#     file.close()
# if __name__ == '__main__':
#     import os
#     txt_content = open("translate_txt/input_srt/2.Meet Your Instructors.srt")
#     txt_dir = '/translate_txt/output_txtput_txt/2.Meet Your Instructors.srt'
#     txt_name = os.path.split(txt_dir)[1]
#     txt_content = ''
#     line = txt_content.readline()
#     while line:
#         # print(line)
#         txt_content += line
#         line = txt_content.readline()
#     text_create(change_txt_to_srt(txt_name), txt_content)

# 直接改后缀名即可，不用读取内容
# def change_txt_to_srt(txt_name):
#     list1 = list(txt_name)
#     n = len(txt_name)
#     list1[n-1] = 't'
#     list1[n-2] = 'r'
#     list1[n-3] = 's'
#     txt_name = ''.join(list1)
#     return txt_name
def copy_files():
    for foldName, subfolders, filenames in os.walk(path):
           for filename in filenames:
                if filename.endswith('.txt'):
                    # new_name = os.path.split(filename)[1]
                    new_name=filename.replace('.txt', '.srt')
                    shutil.copyfile(os.path.join(foldName, filename), os.path.join(path2, new_name))
if __name__ == '__main__':
    copy_files()
