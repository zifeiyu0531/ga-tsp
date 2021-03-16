# -*- coding: utf-8 -*-
import argparse

parser = argparse.ArgumentParser(description='Configuration file')
arg_lists = []


def add_argument_group(name):
    arg = parser.add_argument_group(name)
    arg_lists.append(arg)
    return arg


# Data
data_arg = add_argument_group('Data')
data_arg.add_argument('--city_num', type=int, default=15, help='city num')  # 城市数量
data_arg.add_argument('--pos_dimension', type=int, default=2, help='city num')  # 坐标维度
data_arg.add_argument('--individual_num', type=int, default=60, help='individual num')  # 个体数
data_arg.add_argument('--gen_num', type=int, default=400, help='generation num')  # 迭代轮数
data_arg.add_argument('--mutate_prob', type=float, default=0.25, help='probability of mutate')  # 变异概率


def get_config():
    config, unparsed = parser.parse_known_args()
    return config


def print_config():
    config = get_config()
    print('\n')
    print('Data Config:')
    print('* city num:', config.city_num)
    print('* individual num:', config.individual_num)
    print('* generation num:', config.gen_num)
    print('* probability of mutate:', config.cross_prob)
