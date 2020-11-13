# 简单的标注检查脚本
textgrid解析来自：
https://github.com/kylebgorman/textgrid

只支持声母韵母划分的中文标注
用来检查：
 1. 标注是否都在词表中存在
 2. 标注的声母韵母是否可以构成拼音

使用方式：将要检查的标注文件放到 to_check 文件夹内，运行 label_check.py 即可

pinyin-phoneme.pkl 中存放了词表字典，如果要更新可以使用 pinyin_phone.py 中
add_pinyin_phn 或者 remove_pinyin
