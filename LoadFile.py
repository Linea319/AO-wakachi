import re

fileDir = 'files/'

#本の情報クラス
class BookInfo:
    def __init__(self,title,author,mainTxt):
        self.title = title
        self.author = author
        self.mainTxt = mainTxt
    #end def
#end def

#ファイル読み込み
def readSjis(fileName: str) -> str:
    """ShiftJISのテキストを読み込む
    """
    path = fileDir + fileName +'.txt'
    with open(path, mode="r", encoding='shift_jis') as f:
        text = f.read()
    return text
#end def

#本文抽出
def loadBookInfo(fileName: str) -> BookInfo:
    text = readSjis(fileName)
    lines = text.split('\n')
    #タイトル、著者名抜き出し

    title = lines[0].strip()
    author = lines[1].strip()

    # ルビ、注釈などの除去
    text = re.split(r'\-{5,}', text)[2]
    text = re.split(r'底本：', text)[0]
    text = re.sub(r'《.+?》', '', text)
    text = re.sub(r'［＃.+?］', '', text)
    # 全角スペース
    text = re.sub(r'\u3000', '', text)
    # 複数の改行
    text = re.sub(r'\n+', '\n', text)
    text = text.strip()

    info = BookInfo(title,author,text)
    return info
#end def
    
if __name__ == "__main__":
    # １つのファイル名を渡す
    info = loadBookInfo("wagahaiwa_nekodearu")
    print(info.title)
    print(info.author)
    print(info.mainTxt[:10])
#end def