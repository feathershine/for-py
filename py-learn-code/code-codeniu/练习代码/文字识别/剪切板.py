import win32con
from win32 import win32clipboard as w
    #把剪切板的文字取出来
class GetTexts(object):

    def getText(self):
        w.OpenClipboard()
        d = w.GetClipboardData(win32con.CF_UNICODETEXT)
        w.CloseClipboard()
        return d

    def setText(self,aStr):
        w.OpenClipboard()
        w.EmptyClipboard()
        d = w.SetClipboardData(win32con.CF_UNICODETEXT,aStr)
        w.CloseClipboard()

#GetTexts().setText('123')
d=GetTexts().getText()
print(d)