#!/usr/local/bin/python3.7
# coding=utf-8
import random
import nhg_input

def nhg_do_test(num, test_dic):
	count = 0

	kana_list = []
	kanji_list = []
	for kana, kanji in test_dic.items():
		kana_list.append(kana)
		kanji_list.append(kanji)
	total_num = len(kana_list)

	print('''
测试开始!
   输入y: 已记住该单词(降低出现频率，直到不再出现)
   输入n: 不认识该单词(加大出现频率)
   输入stop: 中止测试
   输入其他: 继续
''')
	while count < num:
		count += 1
		if len(kana_list) == 0:
			print('没有待测试的单词了...退出测试')
			break;

		i = random.randint(0, total_num-1)
		kana = kana_list[i]
		kanji = kanji_list[i]
		print('[%d] %s'%(count, kana))

		_i = input("")	# input any key to continue: show kanji
		if _i=='stop':	# input 'stop' to stop test
			break;
		elif _i=='y':
			kana_list.remove(kana)
			kanji_list.remove(kanji)
			total_num = len(kana_list)
		elif _i=='n':
			kana_list.append(kana)
			kanji_list.append(kanji)
			total_num = len(kana_list)

		print('   ->%s'%kanji)

def nhg_do_unit_test(num):
	level = input('测试等级(n5/n4/n3/n2/n1):')
	unit = input('测试单元(1/2/3/...):')

	dic = nhg_input.dic
	dic_level = dic[level]
	dic_unit = dic_level[unit]

	dic_test = dic_unit
	nhg_do_test(num, dic_test)

def nhg_do_level_test(num):
	level = input('测试等级(n5/n4/n3/n2/n1):')

	dic = nhg_input.dic
	dic_test = {}
	dic_level = dic[level]
	for unit, dic_unit in dic_level.items():
		dic_test.update(dic_unit)

	nhg_do_test(num, dic_test)

def nhg_do_random_test(num):
	dic = nhg_input.dic
	dic_test = {}
	for level, dic_level in dic.items():
		for unit, dic_unit in dic_level.items():
			dic_test.update(dic_unit)

	nhg_do_test(num, dic_test)

def nhg_test():
	print('------进入测试模式------')

	mode = input('''
选择测试模式：
	1: 单元测试
	2: 等级测试
	3: 随机测试
''')
	num = int(input('测试词汇数:'))

	if mode=='1':
		nhg_do_unit_test(num)
	elif mode=='2':
		nhg_do_level_test(num)
	elif mode=='3':
		nhg_do_random_test(num)
	else:
		print("错误的测试模式")

	print('------退出测试模式------')