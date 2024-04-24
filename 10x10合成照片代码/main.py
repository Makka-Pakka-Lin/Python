import os

import PIL.Image as Image
import cv2


# 读取图片


def resize_by_width(infile, image_size, image_size_y):
    img = cv2.imread(infile)
    cv2.resize(img, (image_size, image_size_y))
    """按照宽度进行所需比例缩放"""
    im = Image.open(infile)
    # (x, y) = im.size
    # lv = round(x / image_size, 2) + 0.01
    x_s = int(image_size)
    y_s = int(image_size_y)
    print("x_s", x_s, y_s)
    out = im.resize((x_s, y_s), Image.ANTIALIAS)
    return out


# def resize_by_width(infile, image_size):
#     """按照宽度进行所需比例缩放"""
#     im = Image.open(infile)
#     (x, y) = im.size
#     lv = round(x / image_size, 2) + 0.01
#     x_s = int(x // lv)
#     y_s = int(y // lv)
#     print("x_s", x_s, y_s)
#     out = im.resize((x_s, y_s), Image.ANTIALIAS)
#     return out


def get_new_img_xy(infile, image_size):
    """返回一个图片的宽、高像素"""
    im = Image.open(infile)
    (x, y) = im.size
    lv = round(x / image_size, 2) + 0.01
    x_s = x // lv
    y_s = y // lv
    # print("x_s", x_s, y_s)
    # out = im.resize((x_s, y_s), Image.ANTIALIAS)
    return 6000, 4000


# 定义图像拼接函数
def image_compose(image_colnum, image_size, image_rownum, image_names, image_save_path, x_new, y_new):
    to_image = Image.new('RGB', (image_colnum * x_new, image_rownum * y_new))  # 创建一个新图
    # 循环遍历，把每张图片按顺序粘贴到对应位置上
    total_num = 0
    for y in range(1, image_rownum + 1):
        for x in range(1, image_colnum + 1):
            from_image = resize_by_width(image_names[image_colnum * (y - 1) + x - 1], image_size, image_size_y)
            # from_image = Image.open(image_names[image_colnum * (y - 1) + x - 1]).resize((image_size,image_size ), Image.ANTIALIAS)
            to_image.paste(from_image, ((x - 1) * x_new, (y - 1) * y_new))
            total_num += 1
            if total_num == len(image_names):
                break
    return to_image.save(image_save_path)  # 保存新图


def get_image_list_fullpath(dir_path):
    file_name_list = ['1.JPG', '2.JPG', '3.JPG', '4.JPG', '5.JPG', '6.JPG', '7.JPG', '8.JPG', '9.JPG',
                      '10.JPG', '11.JPG', '12.JPG', '13.JPG', '14.JPG', '15.JPG', '16.JPG', '17.JPG', '18.JPG',
                      '19.JPG', '20.JPG', '21.JPG', '22.JPG', '23.JPG', '24.JPG', '25.JPG', '26.JPG', '27.JPG',
                      '28.JPG', '29.JPG', '30.JPG', '31.JPG', '32.JPG', '33.JPG', '34.JPG', '35.JPG', '36.JPG',
                      '37.JPG', '38.JPG', '39.JPG', '40.JPG', '41.JPG', '42.JPG', '43.JPG', '44.JPG', '45.JPG',
                      '46.JPG', '47.JPG', '48.JPG', '49.JPG', '50.JPG', '51.JPG', '52.JPG', '53.JPG', '54.JPG',
                      '55.JPG', '56.JPG', '57.JPG', '58.JPG', '59.JPG', '60.JPG', '61.JPG', '62.JPG', '63.JPG',
                      '64.JPG', '65.JPG', '66.JPG', '67.JPG', '68.JPG', '69.JPG', '70.JPG', '71.JPG', '72.JPG',
                      '73.JPG', '74.JPG', '75.JPG', '76.JPG', '77.jpg', '78.JPG', '79.JPG', '80.JPG', '81.JPG',
                      '82.JPG', '83.JPG', '84.JPG', '85.jpg', '86.JPG', '87.JPG', '88.JPG', '89.jpg', '90.JPG',
                      '91.JPG', '92.JPG', '93.JPG', '94.JPG', '95.JPG', '96.JPG', '97.JPG', '98.JPG', '99.JPG',
                      '100.JPG']
    # file_name_list = ['40.JPG']
    # file_name_list = ['0.JPG', '1.JPG', '2.JPG', '3.JPG', '4.JPG', '5.JPG', '6.JPG', '7.JPG', '8.JPG', '9.JPG',
    #                   '10.JPG', '11.JPG', '12.JPG', '13.JPG', '14.JPG', '15.JPG', '16.JPG', '17.JPG', '18.JPG',
    #                   '19.JPG', '20.JPG', '21.JPG', '22.JPG', '23.JPG', '24.JPG', '25.JPG', '26.JPG', '27.JPG',
    #                   '28.JPG', '29.JPG', '30.JPG', '31.JPG', '32.JPG', '33.JPG', '34.JPG', '35.JPG', '36.JPG',
    #                   '37.JPG', '38.JPG', '39.JPG', '40.JPG', '41.JPG', '42.JPG', '43.JPG', '44.JPG', '45.JPG',
    #                   '46.JPG', '47.JPG', '48.JPG', '49.JPG', '50.JPG', '51.JPG', '52.JPG', '53.JPG', '54.JPG',
    #                   '55.JPG', '56.JPG', '57.JPG', '58.JPG', '59.JPG', '60.JPG', '61.JPG', '62.JPG', '63.JPG',
    #                   '64.JPG', '65.JPG', '66.JPG', '67.JPG', '68.JPG', '69.JPG', '70.JPG', '71.JPG', '72.JPG',
    #                   '73.JPG', '74.JPG', '75.JPG', '76.JPG', '77.jpg', '78.JPG', '79.JPG', '80.JPG', '81.JPG',
    #                   '82.JPG', '83.JPG', '84.JPG', '85.jpg', '86.JPG', '87.JPG', '88.JPG', '89.jpg', '90.JPG',
    #                   '91.JPG', '92.JPG', '93.JPG', '94.JPG', '95.JPG', '96.JPG', '97.JPG', '98.JPG', '99.JPG']
    image_fullpath_list = []
    for file_name_one in file_name_list:
        file_one_path = os.path.join(dir_path, file_name_one)
        if os.path.isfile(file_one_path):
            image_fullpath_list.append(file_one_path)
        else:
            img_path_list = get_image_list_fullpath(file_one_path)
            image_fullpath_list.extend(img_path_list)
    return image_fullpath_list


def merge_images(image_dir_path, image_size, image_colnum):
    # 获取图片集地址下的所有图片名称
    image_fullpath_list = get_image_list_fullpath(image_dir_path)
    print("image_fullpath_list", len(image_fullpath_list), image_fullpath_list)

    image_save_path = r'{}.jpg'.format(image_dir_path)  # 图片转换后的地址
    # image_rownum = 4  # 图片间隔，也就是合并成一张图后，一共有几行
    image_rownum_yu = len(image_fullpath_list) % image_colnum
    if image_rownum_yu == 0:
        image_rownum = len(image_fullpath_list) // image_colnum
    else:
        image_rownum = len(image_fullpath_list) // image_colnum + 1

    x_list = []
    y_list = []
    for img_file in image_fullpath_list:
        img_x, img_y = get_new_img_xy(img_file, image_size)
        x_list.append(img_x)
        y_list.append(img_y)

    print("x_list", sorted(x_list))
    print("y_list", sorted(y_list))
    x_new = int(x_list[len(x_list) // 5 * 4])
    y_new = int(y_list[len(y_list) // 5 * 4])
    print(" x_new, y_new", x_new, y_new)
    image_compose(image_colnum, image_size, image_rownum, image_fullpath_list, image_save_path, x_new, y_new)  # 调用函数
    # for img_file in image_fullpath_list:
    #     resize_by_width(img_file,image_size)


# if __name__ == '__main__':
#     for i in range(1, 9):
#         image_dir_path = r'C:/Users/Android/Pictures/2023_1/122/' + str(i)  # 图片集地址
#         image_size = 6000  # 每张小图片的大小
#         image_size_y = 4000
#         image_colnum = 10  # 合并成一张图后，一行有几个小图
#         merge_images(image_dir_path, image_size, image_colnum)
if __name__ == '__main__':
    image_dir_path = r'C:/Users/Android/Pictures/2023_1/6'  # 图片集地址
    image_size = 6000  # 每张小图片的大小
    image_size_y = 4000
    image_colnum = 10  # 合并成一张图后，一行有几个小图
    merge_images(image_dir_path, image_size, image_colnum)
