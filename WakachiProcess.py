from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *
import re

maxCharNum = 8
minCharNum = 3


def wakati(text: str):
    """テキストを分かち書きにする"""

    tokenizer = Tokenizer()
    #char_filters = [RegexReplaceCharFilter(u'。', u'\n')]
    token_filters = [CompoundNounFilter(), POSStopFilter(['記号,読点'])]
    a = Analyzer(tokenizer=tokenizer,
                 token_filters=token_filters)
    resultTxt = ""

    for line in text.splitlines():
        # 行ごとに分かち書き
        section = ""

        # 結果テキストに保存するローカル関数
        def reserve(saveTxt: str):
            nonlocal resultTxt
            nonlocal section
            resultTxt += saveTxt + '\n'
            section = ""

        for token in a.analyze(line):
            # 句点は無視して次
            if '句点' in token.part_of_speech:
                reserve(section)
                continue

            # 最大値超えたら保存して次へ
            if len(section + token.surface) >= maxCharNum:
                reserve(section)
                section = token.surface
                continue

            # ここから先は結合確定
            section += token.surface

            # 助詞で最小値以上だったら次へ
            if '助詞' in token.part_of_speech and len(section) >= minCharNum:
                reserve(section)

        # sectionに文字が残ってたら保存
        if len(section) > 0:
            reserve(section)

    return resultTxt


if __name__ == "__main__":

    print(wakati("吾輩は猫である。名前はまだ無い。"))
