import LoadFile
import WakachiProcess

# テキストファイル読み込み
filename = "wagahaiwa_nekodearu"
bookInfo = LoadFile.loadBookInfo(filename)

# 分かち書きさせる
wakachiResult = WakachiProcess.wakati(bookInfo.mainTxt)

# 保存
resultDir = "results/"
with open(resultDir + filename + ".txt", "w", encoding="utf-8", newline='\n') as f:
    f.writelines([bookInfo.title+"\n", bookInfo.author+"\n"])
    f.write(wakachiResult)
