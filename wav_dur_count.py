import wave
import contextlib
import os
import time
import fnmatch
from tqdm import tqdm

t = time.time()
wav_dir = "/Users/zhe/Downloads/入籍"
total_second = 0
wav_count = 0

# with open('contextlib_duration.txt', 'w', encoding='utf-8') as log:
# for file in os.listdir(wav_dir):
supportedExtensions = '*.wav'
for dirpath, dirs, files in os.walk(wav_dir):
    for file in tqdm(fnmatch.filter(files, supportedExtensions)):
        wav_count += 1
        file_path = os.path.join(dirpath, file)
        # print(file_path)
        with contextlib.closing(wave.open(file_path, 'r')) as f:
            frames = f.getnframes()         # 帧数
            rate = f.getframerate()         # 帧率（每秒的帧数）
            duration = frames / float(rate) # 单位：秒
            total_second = total_second + duration
            # content = file + " " + str(duration) + "\n"
            # log.write(content)

print("wav file count: ", wav_count)
print("total duration: ", total_second)
print("total hour: ", total_second / 3600)
# print(time.time() - t)
