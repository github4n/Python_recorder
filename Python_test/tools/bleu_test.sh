# !/bin/bash

#python3 corpus_test.py
#en-zh

#线上测试的地址
url_up=""
#测试环境的地址
url_down=""

field1="it"
direc1="en-zh.zh"
direc2="en-zh.en"
direc3="zh-en.tran"
direc4="zh-en.google"
#direc5="en-zh.baidu"
#direc6="en-zh.youdao"
#direc7="en-zh.xiaoniu"
filename_ori_for_tran="../"$field1"/origin/"$direc1
filename_ori_for_comp="../"$field1"/origin/"$direc2
filename_tran="../"$field1"/tran/"$direc3
filename_google="../"$field1"/google/"$direc4
#filename_baidu="../"$field1"/baidu/"$direc5
#filename_youdao="../"$field1"/youdao/"$direc6
#filename_xiaoniu="../"$field1"/xiaoniu/"$direc7
filename_other="../"$field1"/other"
#echo $filename_ori_for_tran
#echo $filename_ori_for_comp
#echo $filename_tran
echo 新译翻译：
python3 corpus_test.py $url_down $filename_ori_for_tran $filename_tran
echo 谷歌翻译：

#xx-zh
#python3 google_tran.py $filename_ori_for_tran $filename_google ${direc1:0-2} ${direc2:0-2}"-CN"

#zh-xx
python3 google_tran.py $filename_ori_for_tran $filename_google ${direc1:0-2}"-CN" ${direc2:0-2}

#vi-zh
#filename_tmp="../patent/origin/en-zh.zh"
#filename_ref="../patent/tran/en-zh.tran"
#filename_google="../patent/google/en-zh.google"

#为标准译文结巴分词
#python3 -m jieba ${filename_ori_for_comp} -d > $filename_other"/stan.cut" 
#为机翻译文结巴分词
#python3 -m jieba ${filename_tran} -d > $filename_other"/ntran.cut"
#为谷歌译文结巴分词
#python3 -m jieba ${filename_google} -d > $filename_other"/google.cut"
#为百度译文结巴分词
#python3 -m jieba ${filename_baidu} -d > $filename_other"/baidu.cut
#为有道译文结巴分词
#python3 -m jieba ${filename_youdao} -d > $filename_other"/youdao.cut
#为小牛译文结巴分词
#python3 -m jieba ${filename_xiaoniu} -d > $filename_other"/xiaoniu.cut

#为结巴分词后的标准译文英语分词
#./tokenizer.perl -l en < $filename_other"/stan.cut" > $filename_other"/stan.cut.tok"
#为结巴分词后的机翻译文英语分词
#./tokenizer.perl -l en < $filename_other"/ntran.cut" > $filename_other"/ntran.cut.tok"
#为结巴分词后的谷歌译文英语分词
#./tokenizer.perl -l en <  $filename_other"/google.cut" > $filename_other"/google.cut.tok"
#为结巴分词后的百度译文英语分词
#./tokenizer.perl -l en <  $filename_other"/baidu.cut" > $filename_other"/baidu.cut.tok"
#为结巴分词后的有道译文英语分词
#./tokenizer.perl -l en <  $filename_other"/youdao.cut" > $filename_other"/youdao.cut.tok"
#为结巴分词后的小牛译文英语分词
#./tokenizer.perl -l en <  $filename_other"/xiaoniu.cut" > $filename_other"/xiaoniu.cut.tok"

#为预处理好的语料进行bleu测试
#./multi-bleu.perl -lc $filename_other"/stan.cut.tok" < $filename_other"/ntran.cut.tok" > $filename_other"/bleu.result.ntran"
#./multi-bleu.perl -lc $filename_other"/stan.cut.tok" < $filename_other"/google.cut.tok" > $filename_other"/bleu.result.google"
#./multi-bleu.perl -lc $filename_other"/stan.cut.tok" < $filename_other"/baidu.cut.tok" > $filename_other"/bleu.result.baidu"
#./multi-bleu.perl -lc $filename_other"/stan.cut.tok" < $filename_other"/youdao.cut.tok" > $filename_other"/bleu.result.youdao"
#./multi-bleu.perl -lc $filename_other"/stan.cut.tok" < $filename_other"/xiaoniu.cut.tok" > $filename_other"/bleu.result.xiaoniu"


#english
#为标准英语译文英语分词
./tokenizer.perl -l en < $filename_ori_for_comp> $filename_other"/stan.tok"
#为机翻译文英语分词
./tokenizer.perl -l en < $filename_tran > $filename_other"/ntran.tok"
#为谷歌译文英语分词
./tokenizer.perl -l en <  $filename_google > $filename_other"/google.tok"
#为百度译文英语分词
#./tokenizer.perl -l en <  $filename_baidu > $filename_other"/baidu.tok"
#为有道译文英语分词
#./tokenizer.perl -l en <  $filename_youdao > $filename_other"/youdao.tok"
#为小牛译文英语分词
#./tokenizer.perl -l en <  $filename_xiaoniu > $filename_other"/xiaoniu.tok"


#为预处理好的语料进行bleu测试
./multi-bleu.perl -lc $filename_other"/stan.tok" < $filename_other"/ntran.tok" > $filename_other"/bleu.result.ntran"
./multi-bleu.perl -lc $filename_other"/stan.tok" < $filename_other"/google.tok" > $filename_other"/bleu.result.google"
#./multi-bleu.perl -lc $filename_other"/stan.tok" < $filename_other"/baidu.tok" > $filename_other"/bleu.result.baidu"
#./multi-bleu.perl -lc $filename_other"/stan.tok" < $filename_other"/youdao.tok" > $filename_other"/bleu.result.youdao"
#./multi-bleu.perl -lc $filename_other"/stan.tok" < $filename_other"/xiaoniu.tok" > $filename_other"/bleu.result.xiaoniu"


#输出bleu值
#echo {$direc1}
#echo {$direc2}
origin1=${direc1:0-2}
origin2=${direc2:0-2}
echo ${origin1} "-->" ${origin2}
echo 新译： 
cat ${filename_other}"/bleu.result.ntran"
echo 谷歌: 
cat ${filename_other}"/bleu.result.google"
#echo 百度：
#cat $filename_other"/bleu.result.baidu"
#echo 有道： 
#cat $filename_other"/bleu.result.youdao"
#echo 小牛：
#cat $filename_other"/bleu.result.xiaoniu"

