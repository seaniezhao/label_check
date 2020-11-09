import fnmatch
import os
import textgrid
from pinyin_phone import pp_dict_reverse, get_all_phon, get_shengmu


def check_label(label_path):

    error_num = 0

    target_seg_tier = textgrid.IntervalTier('phoneme')

    py_grid = textgrid.TextGrid.fromFile(label_path)

    source_tier = py_grid.tiers[0]
    assert source_tier != None

    temp_list = []
    for i, interval in enumerate(source_tier):
        phn = interval.mark.strip()

        # check phn
        if phn not in get_all_phon():
            print(str(interval) + ' in file: ' + raw_path)
            error_num += 1
        else:
            target_seg_tier.addInterval(interval)

        # check pinyin
        if phn in get_shengmu():
            temp_list.append(phn)
            continue
        elif len(temp_list) > 0:
            temp_list.append(phn)
            dict_key = str(temp_list)
            if dict_key not in pp_dict_reverse:
                print(str(interval) + ' in file: ' + raw_path)
                error_num += 1
            temp_list.clear()
        else:
            pass
            # dict_key = str([phn])
            # if dict_key not in pp_dict_reverse:
            #     print(interval)

    return  error_num
    # target_grid = textgrid.TextGrid()
    # target_grid.append(target_seg_tier)
    # write_path = label_path.replace('interval', 'TextGrid')
    # target_grid.write(write_path)


if __name__ == '__main__':
    to_check_folder = './to_check'

    error_num = 0
    supportedExtensions = '*.interval'
    for dirpath, dirs, files in os.walk(to_check_folder):
        for file in fnmatch.filter(files, supportedExtensions):

            raw_path = os.path.join(dirpath, file)
            error_num += check_label(raw_path)

    if error_num == 0:
        print("pinyin and phone check passed")
    else:
        print("fail to pass the check see the output above")
