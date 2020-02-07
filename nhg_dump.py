#!/usr/local/bin/python3.7
# coding=utf-8
import nhg_input

def nhg_dump():
	dic = nhg_input.dic
	for level, dic_level in dic.items():
		print('------等级：%s------'% level)
		for unit, dic_unit in dic_level.items():
			print('===第%s单元==='% unit)
			count = 0
			for kana, kanji in dic_unit.items():
				count += 1
				print('[%d] %s (%s)'% (count, kana, kanji))