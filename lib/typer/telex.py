import time
import itertools

class Telex:

    __map = {
        "f" : {
            "a" : "à",
            "ă" : "ằ",
            "â" : "ầ",
            "e" : "è",
            "ê" : "ề",
            "i" : "ì",
            "o" : "ò",
            "ô" : "ồ",
            "ơ" : "ờ",
            "u" : "ù",
            "ư" : "ừ",
            "y" : "ỳ",
            "ươ": "ườ"
        },
        "s" : {
            "a" : "á",
            "ă" : "ắ",
            "â" : "ấ",
            "e" : "é",
            "ê" : "ế",
            "i" : "í",
            "o" : "ó",
            "ô" : "ố",
            "ơ" : "ớ",
            "u" : "ú",
            "ư" : "ứ",
            "y" : "ý",
            "ươ": "ướ" 
        },
        "x" : {
            "a" : "ã",
            "ă" : "ẵ",
            "â" : "ẫ",
            "e" : "ẽ",
            "ê" : "ễ",
            "i" : "ĩ",
            "o" : "õ",
            "ô" : "ỗ",
            "ơ" : "ỡ",
            "u" : "ũ",
            "ư" : "ữ",
            "y" : "ỹ",
            "ươ": "ưỡ"
        },
        "r" : {
            "a" : "ả",
            "ă" : "ẳ",
            "â" : "ẩ",
            "e" : "ẻ",
            "ê" : "ể",
            "i" : "ỉ",
            "o" : "ỏ",
            "ô" : "ổ",
            "ơ" : "ở",
            "u" : "ủ",
            "ư" : "ử",
            "y" : "ỷ",
            "ươ": "ưở"
        },
        "j" : {
            "a" : "ạ",
            "ă" : "ặ",
            "â" : "ậ",
            "e" : "ẹ",
            "ê" : "ệ",
            "i" : "ị",
            "o" : "ọ",
            "ô" : "ộ",
            "ơ" : "ợ",
            "u" : "ụ",
            "ư" : "ự",
            "y" : "ỵ",
            "ươ": "ượ"
        },
        "d" : {
            "d" : "đ"
        },
        "e" : {
            "e" : "ê"
        },
        "o" : {
            "o" : "ô"
        },
        "a" : {
            "a" : "â"
        },
        "w" : {
            "a" : "ă",
            "u" : "ư",
            "o" : "ơ",
            "uo" : "ươ"
        }
    }

    __mapChar = {
        "à" : "af",
        "á" : "as",
        "â" : "aa",
        "ã" : "ax",
        "è" : "ef",
        "é" : "es",
        "ê" : "ee",
        "ẹ" : "ej",
        "ẻ" : "ej",
        "ẽ" : "ex",
        "ì" : "if",
        "í" : "is",
        "ỉ" : "ir",
        "ị" : "ij",
        "ò" : "of",
        "ó" : "os",
        "ô" : "oo",
        "õ" : "ox",
        "ù" : "uf",
        "ú" : "us",
        "ý" : "ys",
        "ă" : "aw",
        "đ" : "dd",
        "ĩ" : "ix",
        "ũ" : "ux",
        "ơ" : "ow",
        "ư" : "uw",
        "ạ" : "aj",
        "ả" : "ar",
        "ấ" : "aas",
        "ầ" : "aaf",
        "ẩ" : "aar",
        "ẫ" : "aax",
        "ậ" : "aaj",
        "ắ" : "aws",
        "ằ" : "awf",
        "ẳ" : "awr",
        "ẵ" : "awx",
        "ặ" : "awj",
        "ế" : "ees",
        "ề" : "eef",
        "ể" : "eer",
        "ễ" : "eex",
        "ệ" : "eej",
        "ọ" : "oj",
        "ỏ" : "or",
        "ố" : "oos",
        "ồ" : "oof",
        "ổ" : "oor",
        "ỗ" : "oox",
        "ộ" : "ooj",
        "ớ" : "ows",
        "ờ" : "owf",
        "ở" : "owr",
        "ỡ" : "owx",
        "ợ" : "owj",
        "ụ" : "uj",
        "ủ" : "ur",
        "ứ" : "uws",
        "ừ" : "uwf",
        "ử" : "uwr",
        "ữ" : "uwx",
        "ự" : "uwj",
        "ỳ" : "yf",
        "ỵ" : "uj",
        "ỷ" : "yr",
        "ỹ" : "yx",
        "ươ" : "uow" ,
        "ưở": "uowr",
        "ướ": "uows",
        "ườ": "uowf",
        "ưỡ": "uowx",
        "ượ": "uowj",
    }

    def __init__(self, text):
        self.text = text

    def parseOne(self, word):
        for i, c in enumerate(word):
            if c in self.__map:
                replace = self.__map[c]
                for j in range(i - 1):
                    curChunk = ''.join(word[j:j+2])
                    if curChunk in replace:
                        nextWord = word[:j] + replace[curChunk] + word[j+2:i] + word[i+1:]
                        # print(nextWord)
                        return self.parseOne(nextWord)
                for j in range(i):
                    curChar = word[j]
                    if curChar in replace:
                        nextWord = word[:j] + replace[curChar] + word[j+1:i] + word[i+1:]
                        # print(curChar, nextWord)
                        return self.parseOne(nextWord)
        return word

    def parse(self):
        start = time.time()
        self.words = self.text.split()
        for i, word in enumerate(self.words):
            self.words[i] = self.parseOne(word)
        self.text = ' '.join(self.words)
        print("Done! %.2fs" % (time.time() - start))
        return self.text

    def invert(self, word):
        result, lists = '', []
        i, cnt = 0, len(word)
        while i < cnt:
            curChar = word[i]
            if curChar in self.__mapChar:
                result += self.__mapChar[curChar]
                lists.append(list(self.__mapChar[curChar]))
            else:
                result += curChar
                lists.append(list(curChar))
            i += 1
        return result, lists


class Generator:

    def __init__(self, word, lists):
        self.__word = word
        self.__lists = lists
        self.__size = len(word)
        self.__len = len(lists)
        self.__starts = [0]
        for item in self.__lists:
            self.__starts.append(
                self.__starts[-1] + len(item))
    
    def __createLinkOnce(self, cnt, items):
        for i in range(len(items)):
            self.__link[i + cnt] = []
        if len(items) == 1: return 
        if len(items) == 2:
            nodeFirst = cnt
            nodeSecond = cnt + 1
            self.__link[nodeFirst].append(nodeSecond)
        if len(items) == 3:
            nodeFirst = cnt
            nodeSecond = cnt + 1
            nodeThird = cnt + 2
            self.__link[nodeFirst].append(nodeSecond)
            # self.__link[nodeFirst].append(nodeThird)
            self.__link[nodeSecond].append(nodeThird)
            # self.__link[nodeThird].append(nodeSecond)

    def __buildGraph(self):
        self.__link = dict()
        for i, items in enumerate(self.__lists):
            self.__createLinkOnce(self.__starts[i], items)
        for i in range(self.__len - 1):
            itemsi = self.__lists[i]
            for posi, itemi in enumerate(itemsi[1:]):
                nodeI = self.__starts[i] + 1 + posi
                for j in range(i + 1, self.__len):
                    for posj, itemj in enumerate(self.__lists[j]):
                        nodeJ = self.__starts[j] + posj
                        self.__link[nodeJ].append(nodeI)
            self.__link[self.__starts[i]].append(self.__starts[i + 1])

    def __setInit(self):
        self.__visited = [False] * self.__starts[-1]
        self.__path = []

    def __dfs(self, uVertex):
        self.__visited[uVertex] = True
        self.__path.append(self.__word[uVertex])
        if len(self.__path) == self.__size:
            print(''.join(self.__path))
            return 
        for v in self.__link[uVertex][::-1]:
            if not self.__visited[v]:
                self.__dfs(v)

    def run(self):
        self.__buildGraph()
        print(self.__link)
        self.__setInit()
        self.__dfs(0)

def main():
    typer = Telex("xin")
    # print(typer.parse())
    word, lists = typer.invert("đường")
    gen = Generator(word, lists)
    print(word, lists)
    gen.run()
    
main()