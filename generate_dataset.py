''' 
Created 5/27/2020 chiahohsiung

Pre-process data from three sources
DSD100
	Instrument: Vocals
	root: 'home/chiahohsiung/NAS_189/Database/DSD100/Source/DSD100/Sources'
Jason
	Instrument: Guitar
	root: 'home/chiahohsiung/NAS_189/homes/cloud60138/guitar_transciption/Data/audio_strumming'
Remy
	Instrument: Piano
	root: '140.109.21.189/homes/remy/generation/data/mp3/Animenzzz'
	'home/chiahohsiung/NAS_189/homes/remy/generation/data/mp3/Animenzzz'
	'home/chiahohsiung/NAS_189/homes/remy/generation/data/mp3/DooPiano'
	'home/chiahohsiung/NAS_189/homes/remy/generation/data/mp3/TheTheorist'

Dataset Type: SourceFolderDataset (sourcefolder)
To-Do: 
	Add more instrument?

Edited 6/05/2020 chiahohsiung

Use all data and sliced the tracks into clips with length of 10 seconds
'''

# Pre-process Jason's guitar tracks


root = '/home/chiahohsiung/NAS_189/homes/cloud60138/guitar_transciption/Data/audio_strumming'
from pydub import AudioSegment
import numpy as np
import os
import random
import librosa

sample_rate = 44100

out_dir_train = '/home/chiahohsiung/NAS_189/home/open-unmix-pytorch-master/data_whole_clips/train/guitar'
out_dir_test = '/home/chiahohsiung/NAS_189/home/open-unmix-pytorch-master/data_whole_clips/test/guitar'
stem = 'guitar'
guitar_filenames = [filename for filename in os.listdir(root) if 'mp3' in filename]

random.shuffle(guitar_filenames)
print('---------------------')
print('There are', len(guitar_filenames), 'guitar tracks(files) in total.')
print('Filename_example: ', guitar_filenames[0])

total_guitar_length = 0 # in seconds
out_dir = out_dir_test
for i in range(len(guitar_filenames)):	
    
    if i > round(len(guitar_filenames)/9):
        out_dir = out_dir_train
#     print(guitar_filenames[i]) 
    # read waveform from the audio file
    guitar = AudioSegment.from_file(os.path.join(root, guitar_filenames[i])) 
    total_guitar_length += len(guitar) / 1000

    # print(total_guitar_length)

    # Note: if the audio has multiple channels, the samples for each channel will be serialized 
    # guitar_arr = guitar.get_array_of_samples()
    # guitar_arr = np.array(guitar_arr)
    # print('guitar_arr.shape: ', guitar_arr.shape)

    # make sure the sampling rate is 44100 
    guitar = guitar.set_frame_rate(sample_rate)
    # convert stereo to mono 
    guitar = guitar.set_channels(1) 

    duration = librosa.get_duration(filename=os.path.join(root, guitar_filenames[i]))
    print("Duration(length): ", duration)
    # duration = song.duration_seconds
    subclip_duration = 10
    num_subclips = int(duration // subclip_duration)

    # guitar_arr = guitar.get_array_of_samples() 
    # guitar_arr = np.array(guitar_arr)
    # print('guitar_arr.shape: ', guitar_arr.shape)
#     out_path = os.path.join(out_dir, os.path.splitext(guitar_filenames[i])[0] + f'.{start}_{end}' + '.wav')
#     print('Out path:', out_path)
#     guitar.export(out_path, format='wav')

    for n in range(num_subclips):
        start = n * subclip_duration
        end = (n+1) * subclip_duration
        print(guitar_filenames[i], start, end)

        out_path = os.path.join(out_dir, os.path.splitext(guitar_filenames[i])[0] + f'.{start}_{end}' + '.wav')
        if os.path.exists(out_path):
            print('Done before')
            continue

        subclip = guitar[start*1000:end*1000]
        subclip.export(out_path, format='wav')
#         exit()
    
print('Total length of guitar tracks:', total_guitar_length, 'seconds')
# Total length of vocals tracks: 52899.5 seconds

# #############  Pre-process DSD100's vocals tracks ############# 

print('----------Processing Vocals tracks-----------')
root = '/home/chiahohsiung/NAS_189/Database/DSD100/Source/DSD100/Sources/Dev'
out_dir = '/home/chiahohsiung/NAS_189/home/open-unmix-pytorch-master/data_whole_clips/train/vocals'
stem = 'vocals'
vocals_filenames = os.listdir(root)
print('There are', len(vocals_filenames), 'training vocals tracks(files) in total.')
print('filename_example: ', vocals_filenames[0])

total_vocals_length = 0 # in seconds
for i in range(len(vocals_filenames)):
    vocals = AudioSegment.from_file(os.path.join(root, vocals_filenames[i]) + '/vocals.wav') 
    total_vocals_length += len(vocals) / 1000
    print(total_vocals_length)
    # make sure the sampling rate is 44100 
    vocals = vocals.set_frame_rate(sample_rate)
    # convert stereo to mono 
    vocals = vocals.set_channels(1) 
    # out_path = os.path.join(out_dir, vocals_filenames[i] + '.wav')
    # print('Out path:', out_path)
    # vocals.export(out_path, format='wav')
    # clips
    duration = librosa.get_duration(filename=os.path.join(root, vocals_filenames[i]) + '/vocals.wav') 
    print("Duration(length): ", duration)
    subclip_duration = 10
    num_subclips = int(duration // subclip_duration)

    for n in range(num_subclips):
        start = n * subclip_duration
        end = (n+1) * subclip_duration
        print(vocals_filenames[i], start, end)

        out_path = os.path.join(out_dir, vocals_filenames[i] + f'.{start}_{end}' + '.wav')
        if os.path.exists(out_path):
            print('Done before')
            continue
        subclip = vocals[start*1000:end*1000]
        subclip.export(out_path, format='wav')

print('Total length of vocals tracks:', total_vocals_length, 'seconds for training')

root = '/home/chiahohsiung/NAS_189/Database/DSD100/Source/DSD100/Sources/Test'
out_dir = '/home/chiahohsiung/NAS_189/home/open-unmix-pytorch-master/data_whole_clips/test/vocals'
stem = 'vocals'
vocals_filenames = os.listdir(root)
print('There are', len(vocals_filenames), 'testing vocals tracks(files) in total.')
print('filename_example: ', vocals_filenames[0])

total_vocals_length = 0 # in seconds
for i in range(len(vocals_filenames)):
    vocals = AudioSegment.from_file(os.path.join(root, vocals_filenames[i]) + '/vocals.wav') 
    total_vocals_length += len(vocals) / 1000
    print(total_vocals_length)
    # make sure the sampling rate is 44100 
    vocals = vocals.set_frame_rate(sample_rate)
    # convert stereo to mono 
    vocals = vocals.set_channels(1) 
#     out_path = os.path.join(out_dir, vocals_filenames[i] + '.wav')
#     print('Out path:', out_path)
#     vocals.export(out_path, format='wav')
#     clips
    duration = librosa.get_duration(filename=os.path.join(root, vocals_filenames[i]) + '/vocals.wav') 
    print("Duration(length): ", duration)
    subclip_duration = 10
    num_subclips = int(duration // subclip_duration)

    for n in range(num_subclips):
        start = n * subclip_duration
        end = (n+1) * subclip_duration
        print(vocals_filenames[i], start, end)

        out_path = os.path.join(out_dir, vocals_filenames[i] + f'.{start}_{end}' + '.wav')
        if os.path.exists(out_path):
            print('Done before')
            continue
        subclip = vocals[start*1000:end*1000]
        subclip.export(out_path, format='wav')

# print('Total length of vocals tracks:', total_vocals_length, 'seconds for testing')
# For the original 50 test example: Total length of vocals tracks: 12162.25 seconds

#############  Pre-process Remy's piano tracks ############# 
root_list = ['/home/chiahohsiung/NAS_189/homes/remy/generation/data/mp3/Animenzzz',
			'/home/chiahohsiung/NAS_189/homes/remy/generation/data/mp3/DooPiano',
			'/home/chiahohsiung/NAS_189/homes/remy/generation/data/mp3/TheTheorist']

# root = random.choice(root_list)
out_dir_train = '/home/chiahohsiung/NAS_189/home/open-unmix-pytorch-master/data_whole_clips/train/piano'
out_dir_test = '/home/chiahohsiung/NAS_189/home/open-unmix-pytorch-master/data_whole_clips/test/piano'

stem = 'piano'
out_dir = out_dir_test
total_piano_length = 0
for root in root_list:
    print('ROOT: ', root)
    piano_filenames = os.listdir(root)
    print('There are', len(piano_filenames), 'piano tracks(files) in ', root)
    random.shuffle(piano_filenames)
#     piano_filenames.sort()
    # print(piano_filenames)
    # print('filename_example: ', piano_filenames[0])
    out_dir = out_dir_test
    for i in range(len(piano_filenames)):       
        print('Filename:', piano_filenames[i])
        'Ignore hidden file .DS_STORE'
        if piano_filenames[i].startswith('.'):
            continue
        if i > round(len(piano_filenames)/9):
            out_dir = out_dir_train
        # read waveform from the audio file
        
#         if piano_filenames[i] == 'Sparkling Daydream - Chuunibyou demo Koi ga Shitai! OP.mp3':
#             continue
        piano = AudioSegment.from_file(os.path.join(root, piano_filenames[i]), format="mp3") 
        total_piano_length += len(piano) / 1000

        # make sure the sampling rate is 44100 
        piano = piano.set_frame_rate(sample_rate)
        # convert stereo to mono 
        piano = piano.set_channels(1) 
        
        duration = librosa.get_duration(filename=os.path.join(root, piano_filenames[i]))    
        print("Duration(length): ", duration)
        # duration = song.duration_seconds
        subclip_duration = 10
        num_subclips = int(duration // subclip_duration)

        for n in range(num_subclips):
            start = n * subclip_duration
            end = (n+1) * subclip_duration
            print(piano_filenames[i], start, end)

            out_path = os.path.join(out_dir, os.path.splitext(piano_filenames[i])[0] + f'.{start}_{end}' + '.wav')
            if os.path.exists(out_path):
                print('Done before')
                continue
            subclip = piano[start*1000:end*1000]
            subclip.export(out_path, format='wav')

print('Total piano length: ', total_piano_length, 'seconds')