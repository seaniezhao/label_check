import fnmatch
import os
import textgrid
from tqdm import tqdm
from pinyin_phone import pp_dict_reverse, get_all_phon, get_shengmu


def extract_from_textgrid(label_path):

    error_num = 0
    phoneme_num = 0
    syllable_num = 0

    target_seg_tier = textgrid.IntervalTier('phoneme')

    py_grid = textgrid.TextGrid.fromFile(label_path)

    source_tier = py_grid.tiers[0]

    duration = source_tier.maxTime - source_tier.minTime

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
            phoneme_num += 1

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
            else:
                syllable_num += 1
            temp_list.clear()
        else:
            pass
            # dict_key = str([phn])
            # if dict_key not in pp_dict_reverse:
            #     print(interval)

    return duration, phoneme_num, syllable_num, error_num
    # target_grid = textgrid.TextGrid()
    # target_grid.append(target_seg_tier)
    # write_path = label_path.replace('interval', 'TextGrid')
    # target_grid.write(write_path)


if __name__ == '__main__':
    to_check_folder = '/Users/zhe/Downloads/小夜'

    total_duration = 0
    phoneme_count = 0
    syllable_count = 0
    error_count = 0

    supportedExtensions = '*.interval'
    for dirpath, dirs, files in os.walk(to_check_folder):
        for file in tqdm(fnmatch.filter(files, supportedExtensions)):

            raw_path = os.path.join(dirpath, file)
            duration, phoneme_num, syllable_num, error_num = extract_from_textgrid(raw_path)

            # print('duration: {0}s, phoneme number: {1}, syllable number: {2}'
            #       .format(duration, phoneme_num, syllable_num))

            total_duration += duration
            phoneme_count += phoneme_num
            syllable_count += syllable_num
            error_count += error_num

    if error_count != 0:
        print("pinyin and phone check passed")
    else:
        print("fail to pass the check see the output above")

    print('total duration: {0}s, phoneme count: {1}, syllable count: {2}'
          .format(total_duration, phoneme_count, syllable_count))

    total_hour = total_duration / 3600.0
    phoneme_per_hour = phoneme_count / total_hour
    syllable_per_hour = syllable_count /total_hour

    print('total time: {0}h, phonemes/h: {1}, syllables/h: {2}'
          .format(total_hour, phoneme_per_hour, syllable_per_hour))
