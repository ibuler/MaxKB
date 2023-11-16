# coding=utf-8
"""
    @project: maxkb
    @Author：虎
    @file： common.py
    @date：2023/10/16 16:42
    @desc:
"""
import importlib
from functools import reduce
from typing import Dict


def query_params_to_single_dict(query_params: Dict):
    return reduce(lambda x, y: {**x, **y}, list(
        filter(lambda item: item is not None, [({key: value} if value is not None and len(value) > 0 else None) for
                                               key, value in
                                               query_params.items()])), {})


def get_exec_method(clazz_: str, method_: str):
    """
    根据 class 和method函数 获取执行函数
    :param clazz_:   class 字符串
    :param method_:  执行函数
    :return: 执行函数
    """
    clazz_split = clazz_.split('.')
    clazz_name = clazz_split[-1]
    package = ".".join([clazz_split[index] for index in range(len(clazz_split) - 1)])
    package_model = importlib.import_module(package)
    return getattr(getattr(package_model, clazz_name), method_)