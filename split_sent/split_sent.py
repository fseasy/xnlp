#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
split sentence from a text.

@time 2017-04-21 
@place CMOS
'''

class PunctHelper4SentSplit(object):
    '''
    punctuation helper class for sentence splitting.
    '''
    DELIMITERS = set([
            # EN delimiters
            u"!",
            u".",
            u"?",
            u";",
            u"~",
            # CN delimieters
            u"！",
            u"。",
            u"？",
            u"；",
            u"…",
            # explicit delimiters
            u"\r",
            u"\n"
        ])
    EN_DOUBLE_QUOTE = u"\""
    EN_SINGLE_QUOTE = u"'"
    CN_DOUBLE_QUOTE_L = b"\xe2\x80\x9c".decode("utf-8")
    CN_DOUBLE_QUOTE_R = b"\xe2\x80\x9d".decode("utf-8")
    CN_SINGLE_QUOTE_L = b"\xe2\x80\x98".decode("utf-8")
    CN_SINGLE_QUOTE_R = b"\xe2\x80\x99".decode("utf-8")
    CN_TRADITIONAL_SINGLE_QUOTE_L = u"「"
    CN_TRADITIONAL_SINGLE_QUOTE_R = u"」"
    CN_TRADITIONAL_DOUBLE_QUOTE_L = u"『"
    CN_TRADITIONAL_DOUBLE_QUOTE_R = u"』"

    EN_RIGHT_PARENTHESIS = u")"
    CN_RIGHT_PARENTHESIS = u"）"
    
    def __init__(self):
        quote_closed = dict()
        # using the list to get the reference
        # -> L, and R should control one value.
        # no pointer in Python, so use list as replacement
        quote_closed[self.EN_DOUBLE_QUOTE] = [True]
        quote_closed[self.EN_SINGLE_QUOTE] = [True]
        quote_closed[self.CN_DOUBLE_QUOTE_L] = [True]
        quote_closed[self.CN_DOUBLE_QUOTE_R] = quote_closed[self.CN_DOUBLE_QUOTE_L]
        quote_closed[self.CN_SINGLE_QUOTE_L] = [True]
        quote_closed[self.CN_SINGLE_QUOTE_R] = quote_closed[self.CN_SINGLE_QUOTE_L]
        quote_closed[self.CN_TRADITIONAL_SINGLE_QUOTE_L] = [True]
        quote_closed[self.CN_TRADITIONAL_SINGLE_QUOTE_R] = quote_closed[
                self.CN_TRADITIONAL_SINGLE_QUOTE_L]
        quote_closed[self.CN_TRADITIONAL_DOUBLE_QUOTE_L] = [True]
        quote_closed[self.CN_TRADITIONAL_DOUBLE_QUOTE_R] = quote_closed[
                self.CN_TRADITIONAL_DOUBLE_QUOTE_L]

        self._quote_closed = quote_closed

        right_parenthesis_set = {self.EN_RIGHT_PARENTHESIS,
                self.CN_RIGHT_PARENTHESIS}
        self._right_parenthesis_set = right_parenthesis_set

    def is_quote(self, char):
        return char in self._quote_closed

    def has_quote_closed(self, quote_char):
        return self._quote_closed[quote_char][0]

    def toggle_quote_state(self, quote_char):
        state_ref = self._quote_closed[quote_char]
        state_ref[0] = not state_ref[0]
        return state_ref[0]

    def is_right_parenthesis(self, char):
        return char in self._right_parenthesis_set

    @classmethod
    def is_delimiter(cls, char):
        return char in cls.DELIMITERS
    

def split_sentence(text):
    '''
    split text to list of sentence.
    
    Parameters
    ----------
    text : str(unicode)

    Returns
    ---------
    sent_list, list of sentence.
    '''
    punc_helper = PunctHelper4SentSplit()
    # the element not store str directly, but storing the list of str,
    # because we may handle the sent previous saved, but str is not
    # changeable in Python, so use list instead.
    sent_list = []
    text_len = len(text)
    pos = 0
    start_pos = 0
    is_prev_char_a_delimiter = lambda pos: (pos >= 1 and 
            punc_helper.is_delimiter(text[pos - 1]))
    def put_sent():
        # keep the punctuation
        sent = text[start_pos: pos+1]
        if len(sent) ==  1 and len(sent_list) > 0:
            # only a delimiter, put previous sent
            sent_list[-1].append(sent)
        else:
            # - save list instead of str
            sent_list.append([sent, ])

    while pos < text_len:
        char = text[pos]
        # 1. 如果是DELIMIETERS， 那么直接必然切分
        if punc_helper.is_delimiter(char):
            put_sent()
            start_pos = pos + 1
        # 2. 如果是引号，且在读到当前引号之前是开放状态
        #    那么读入这个引号，必然就封闭了
        #    在这个状态下，检查前一个字符是否是DELIMITER,
        #    如果是，那么这个引号就应该属于前一个句子！
        elif punc_helper.is_quote(char):
            # firstly toggle the quote state
            punc_helper.toggle_quote_state(char)
            # if closed?
            if punc_helper.has_quote_closed(char):
                # check whether previous char is DELIMIETER
                if is_prev_char_a_delimiter(pos):
                    # current quote belongs to previous sent
                    #  - because previous char is DELIMIETER,
                    #    so assert(len(sent_list) > 0) 
                    sent_list[-1].append(char)
                    start_pos = pos + 1 # move start pos to next char!!
        # 3. 如果是右括号，那么检查前面的字符是否是DELIMITER
        #    如果是，则把右括号放到前一个句子！
        elif punc_helper.is_right_parenthesis(char):
            if is_prev_char_a_delimiter(pos):
                sent_list[-1].append(char)
                start_pos = pos + 1
        pos += 1
    if start_pos < text_len:
        # left char
        # because pos has been text_len, while in put_sent,
        # do pos + 1!
        pos -= 1
        put_sent()
    # join
    return [ u"".join(sub_sent) for sub_sent in sent_list]


