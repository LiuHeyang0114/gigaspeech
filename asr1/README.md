# ASR Project
## Additional folder and files
- ./kaldi_format_data:` splited data for 50h、100h subset and its original 250h set`
- split.py: `code to select training subset`
- run_withlm.sh: `training scripts with language model fusion`

Since we've already selected subsets of the training set, you don't need to run split.py anymore.
## Modifications to asr.sh
### Extra parameters
These parameters can be specified in run.sh.
- time:` The length of the training set,with options of 50, 100 and 250.`

### Recommended parameters
These parameters use default values in the original training script, but we recommend that you specify them explicitly.
- gpu_inference:` Use gpu to boost your decoding speed.`
- inference_asr_model:` Choose your decoding model, such as valid.acc.ave.pth,valid.acc.best.pth,5epoch.pth`
- inference_lm:` The language model path used for decoding. For example, you use the Language Model Project to generate a language model and specify its path like model.pt.`

## Additional notes on ./conf
We provide training parameters for three models.

- train_asr.yaml:` CTC:Compress and adjust parameters based on the original model.`
- train_asr_rnn.yaml:` RNN:Training with an RNN model based on an encoder-decoder paradigm.`
- train_asr_streaming_transformer.yaml:` Streaming Transformer: Training with Transformer in streaming fashion.`
- decode_asr_transformer.yaml:` Decoding for Transformer based model.`

## Result for different models
|dataset|Snt|Wrd|Corr|Sub|Del|Ins|Err|S.Err|
|---|---|---|---|---|---|---|---|---|
exp/asr_train_asr_raw_en_bpe5000/decode_asr_asr_model_valid.acc.ave/dev/score_wer/result.txt:|1000|22670|66.4|27.9|5.7|8.2|41.9|98.5|
exp/asr_train_asr_raw_en_bpe5000/decode_asr_asr_model_valid.acc.ave/test/score_wer/result.txt:|1000|19165|65.9|28.6|5.5|7.7|41.8|96.5|
exp/asr_train_asr_rnn_raw_en_bpe5000/decode_asr_asr_model_valid.acc.ave/dev/score_wer/result.txt:|1000|22670|76.5|24.1|7.5|4.0|35.6|94.5|
exp/asr_train_asr_rnn_raw_en_bpe5000/decode_asr_asr_model_valid.acc.ave/test/score_wer/result.txt:|1000|19165|76.6|23.9|7.7|3.6|35.2|92.2|
exp/asr_train_asr_streaming_transformer_raw_en_bpe5000/decode_asr_transformer_asr_model_valid.acc.ave/dev/score_wer/result.txt:|1000|22670|75.5|19.9|4.6|5.2|29.7|93.5|
exp/asr_train_asr_streaming_transformer_raw_en_bpe5000/decode_asr_transformer_asr_model_valid.acc.ave/test/score_wer/result.txt:|1000|19165|75.6|20.1|4.4|5.0|29.4|90.2|

The contents of ./data and ./dump are the same as the original code, and a soft connection can be used to reduce memory overhead.

In addition, please rename the exp.orig folder of the original recipe to exp and save it in the current path.