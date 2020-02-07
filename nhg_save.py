#!/usr/local/bin/python3.7
# coding=utf-8
import os
import json
import nhg_input

def nhg_save(fname):
	dic = nhg_input.dic
	fo = open(fname, "w")
	str = json.dumps(dic)
	fo.write( str )
	fo.close()
