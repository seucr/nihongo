#!/usr/local/bin/python3.7
# coding=utf-8
import json, os

'''
{
	'n5':
	{
		'1':
		{
			'にほんご':'日本語',
			...
		},
		'2':{...},
		'3':{...}
	}, 
	'n4':{...},
	'n3':{...},
}
'''
dic = {}

def nhg_input_init(fname):
	global dic
	if os.path.exists(fname):
		fo = open(fname, "r")
		str = fo.read()
		#print(str)
		dic = json.loads(str)
		'''
		for level, dic_level in dic.items():
			print ("------等级：%s------"%level)
			for unit, dic_unit in dic_level.items():
				print ("===第%s单元==="% unit)
				count = 0
				for kana, kanji in dic_unit.items():
					count += 1
					print ("[%d] %s (%s)"%(count, kana, kanji))
		'''


def nhg_input(level, unit):
	print('''
------进入输入模式------
     %s 第 %s 单元
  先输入假名，再输入汉字
  输入del， 删除已存在的单词
  输入done，退出输入模式
''' % (level, unit))

	global dic
	new_word = {}
	#print("dic:", dic)

	if level in dic.keys():
		dic_level = dic[level]
	else:
		dic_level = {}
		dic[level] = dic_level

	#print("dic_level:", dic_level)

	if unit in dic_level.keys():
		dic_unit = dic_level[unit]
	else:
		dic_unit = {}
		dic_level[unit] = dic_unit

	#print("dic_unit:", dic_unit)

	# 添加单词到单元
	while True:
		kana = input("仮名:")
		if kana=='done':
			break
		elif kana=='del':
			kana = input('输入要删除的假名:')
			del dic_unit[kana]
			print('已删除...')
			continue

		kanji = input("漢字:")
		new_word[kana] = kanji
		dic_unit.update(new_word)
		print('新增词汇：%s(%s)'% (kana, kanji))
		#print("dic_unit:", dic_unit)

	print('''
------退出输入模式------
''')