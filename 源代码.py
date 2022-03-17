import requests
from lxml import etree
import os

def down_load_pic(describe, addition):
    url = "https://pic.netbian.com/4k{}/index{}.html".format(describe, addition)
    # Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38
    header = {
        "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q0.2",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36 Edg/93.0.961.38"

    }
    response = requests.get(url=url, headers=header)
    # response.encoding = 'utf-8'
    page_text = response.text
    tree = etree.HTML(page_text)
    img_list = list(tree.xpath('//ul[@class="clearfix"]//img/@src'))
    img_name = list(tree.xpath('//ul[@class="clearfix"]//img/@alt'))

    print(len(img_list), img_list)
    print(len(img_name), img_name)
    # src="/uploads/allimg/210423/224716-16191892361adb.jpg" alt="赛博朋克风格奇幻少女 集原美电脑4k壁纸3840x2160"
    # https://pic.netbian.com/uploads/allimg/210423/224716-1619189236e4d9.jpg
    index = 0
    while True:
        if index == len(img_list): break
        full_url = 'https://pic.netbian.com' + img_list[index]
        name = str(img_name[index])
        #
        try:
            name = name.encode('iso-8859-1').decode('gbk')
        except Exception as e:
            print("解码失败", e)
        #
        try:
            img_data = requests.get(full_url, headers=header).content
            with open('彼岸图网/' + name + '.jpg', 'wb') as file:
                file.write(img_data)
                print("保存成功！")
        except Exception as e:
            print("保存失败！", e)
        index += 1


if __name__ == '__main__':
    print("本脚本由穆哥制作，使用前请告诉一个你的朋友：\n穆哥很帅！")
    os.mkdir('彼岸图网')
    print("开始依次爬取彼岸图网的动漫，美女，游戏，人物图片")
    page_max = input("请输入每种图片爬取的页数（小于160）：")
    for details in ['dongman', 'meinv', 'youxi', 'renwu']:
        for i in range(1, page_max):
            if i == 1:
                addition = ''
                try:
                    down_load_pic(details, addition)
                except Exception as e:
                    print("下载失败", e)
            else:
                addition = '_{}'.format(i)
                try:
                    down_load_pic(details, addition)
                except Exception as e:
                    print("下载失败", e)
                else:
                    print("下载成功！")
