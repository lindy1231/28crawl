# -*- coding: utf-8 -*-
import zh_wiki
import langconv
def trad_to_sim(sentence):
    """
    将sentence中的繁体字转为简体字
    :param sentence: 待转换的句子
    :return: 将句子中繁体字转换为简体字之后的句子
    """
    sentence = langconv.Converter('zh-hans').convert(sentence)
    return sentence

print(trad_to_sim("""
"""))