#!/usr/local/bin/python3.7
# coding=utf-8
import sys
import nhg_input, nhg_dump, nhg_save, nhg_test

VER = '0.1'
FNAME = 'nihongo.txt'

def usage():
	print("""
日语词汇测试 version %s. 模式说明：
	input: 新增词汇到本地词典
	dump:  显示本地词典所有词汇
	save:  保存本地字典到文件
	test:  随机测试词汇
	exit:  退出程序
		"""% VER)

def input_mode():
	level = input("等级(n5/n4/n3/n2/n1):")
	unit = input("单元(1/2/3/...):")
	nhg_input.nhg_input(level, unit)

def test_mode():
	nhg_test.nhg_test()

def dump_mode():
	nhg_dump.nhg_dump()

def save_mode():
	nhg_save.nhg_save(FNAME)

def exit_mode():
	sys.exit(0)

def nhg_init():
	# 从文件加载本地词典
	nhg_input.nhg_input_init(FNAME)

def nhg_main(mode):
	if mode=='input':
		input_mode()
	elif mode=='test':
		test_mode()
	elif mode=='dump':
		dump_mode()
	elif mode=='save':
		save_mode()
	elif mode=='exit':
		exit_mode()
	else:
		usage()

if __name__=='__main__':
	nhg_init()

	while True:
		usage()
		mode = input("选择模式:");
		nhg_main(mode)