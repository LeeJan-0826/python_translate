# str = 'a b cdef'
# list = list(str)
# list.insert(2,'eee')
# str1 = ''.join(list)
# del list[1]
# print(str1)
# print(list)
import os
txt_dir = 'C:\\Users\\haizeiwang\\Desktop\\test'
def get_path(txt_dir):
    pic_path=[]
    for path in os.listdir(txt_dir):
        real_path = os.path.join(txt_dir, path)
        pic_path.append(real_path)
    return pic_path
def get_path_name(txt_dir):
    pic_path = get_path(txt_dir)
    # print(type(pic_path))
    for i in range(0, len(pic_path)):
        pic_path[i] = os.path.split(pic_path[i])[1]
    print(pic_path)
def tet():
    list = ['1', '2']
    flag = -10
    if '4444' in list:
        flag = 1
    if(flag):
        print('true')
    else:
        print('flase')
if __name__ == '__main__':
    tet()
    # get_path_name(txt_dir)