originPath = '/dssg/home/acct-stu/stu486/gigaspeech/asr1/exp/asr_stats_raw_en_bpe5000/train/speech_shape'
savePath = '/dssg/home/acct-stu/stu486/gigaspeech/asr1/kaldi_format_split/speech_shape_50'
durationPath='/dssg/home/acct-stu/stu486/gigaspeech/asr1/dump/raw/train/utt2dur'
l = 5
total_time=0
with open(originPath) as reader, open(savePath, 'w') as writer, open(durationPath) as duration:
    for index, line in enumerate(reader):
        line2=duration.readline()
        #if index % l == 0 or index % l == 3:
        if index % l == 0 :
            writer.write(line)
            _,t=line2.split()
            total_time=total_time+float(t)
            if total_time > 180000 :
                break
    writer.close()
print(total_time)
