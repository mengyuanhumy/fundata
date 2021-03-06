# -*- coding: utf-8 -*-

from ...client import get_api_client
#基础信息

def get_batch_player(page=0, limit=16):
	"""批量获取队员信息
	page=[int]，默认为 0
	limit=[int]，默认为 16
	返回dict格式
	"""
	client=get_api_client()
	uri="/fundata-dota2-free/v2/league/player" #队员列表
	data={}
	if page>0: data["page"]=page;
	if limit >0: data["limit"]=limit;

	return client.api(uri, data)

def get_single_player(player_id):
	"""单个获取队员信息
	player_id=[int] 队员编号
	返回dict格式
	"""
	client=get_api_client()
	uri="/fundata-dota2-free/v2/league/player/info" #队员信息
	data={}
	if player_id>0: data["player_id"]=player_id;

	return client.api(uri, data)