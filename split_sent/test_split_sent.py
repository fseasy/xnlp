#!/usr/bin/env python2
# -*- coding: utf-8 -*-

from ..split_sent import split_sentence

def test_split_sent():
    # 1. normal
    t1 = u"句子1。句子2！句子三."
    gt1 = [u"句子1。", u"句子2！", u"句子三."]
    pt1 = split_sentence(t1)
    assert gt1 == pt1

    # 2. no puntuation in end 
    t2 = u"句子1。句子2！句子三"
    gt2 = [u"句子1。", u"句子2！", u"句子三"]
    pt2 = split_sentence(t2)
    assert gt2 == pt2

    # 3. single dimiter
    t3 = u"句子1。.句子2！!!"
    gt3 = [u"句子1。.", u"句子2！!!"]
    pt3 = split_sentence(t3)
    assert gt3 == pt3

    # 4. quote - no close
    t4 = u"句子1。\"句子2！!!"
    gt4 = [u"句子1。", u"\"句子2！!!"]
    pt4 = split_sentence(t4)
    assert gt4 == pt4
    # 5. quote- close, no delimiter
    t5 = u"句子1。\"句子2\"！!!"
    gt5 = [u"句子1。", u"\"句子2\"！!!"]
    pt5 = split_sentence(t5)
    assert gt5 == pt5
    # 6. quote-close
    t6 = u"句子1。\"句子2！\"!!"
    gt6 = [u"句子1。", u"\"句子2！\"!!"]
    pt6 = split_sentence(t6)
    assert gt6 == pt6

    # 7. right parenthesis
    t7 = u"句子1。\"句子2！\"!!)"
    gt7 = [u"句子1。", u"\"句子2！\"!!)"]
    pt7 = split_sentence(t7)
    assert gt7 == pt7


    

