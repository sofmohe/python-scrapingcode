#coding:utf-8
import os
import sys
sys.path.append("");#自作関数のあるディレクトリ
import myFunc as mf
import glob


#現在の年月日を取得
presentYMD = mf.presentDay();
fileName = presentYMD + ".txt";


#今日の日付のファイルを作成
with open(fileName, 'w') as fmake:
	fmake.write("これはテストです。");

#txtファイル名のリスト作成
path = './';
pathFile = path + '*.txt';
textList = [];
textList = glob.glob(pathFile);
nameList = [];
filterDate = int(presentYMD);

#過去ファイルの削除
for i,val in enumerate(textList):
	nameList.append(val.lstrip("./").rstrip(".txt"));
	if int(nameList[i]) < filterDate:
		os.remove(path + nameList[i] + ".txt");






