import os
import sox
import fnmatch
from tqdm import tqdm

wav_dir = "/Users/zhe/Downloads/入籍"
total_second = 0
wav_count = 0

supportedExtensions = '*.wav'
for dirpath, dirs, files in os.walk(wav_dir):
    for file in tqdm(fnmatch.filter(files, supportedExtensions)):
        wav_count += 1
        file_path = os.path.join(dirpath, file)
        # print(file_path)
        try:
            wav_info = sox.file_info.info(file_path)
            wav_duration = wav_info['duration']
            total_second += wav_duration
        except Exception as e:
            print(e, file_path)

print("wav file count: ", wav_count)
print("total duration: ", total_second)
print("total hour: ", total_second / 3600)
