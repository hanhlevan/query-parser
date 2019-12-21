from app.words import WordGetter
from app.correct_word import WordCorrector
from app.connector import AccessDatabase
# from app.sentence import Sentence

class Main:

    def __init__(self):
        # wordGet = WordGetter(fileName="./data/Viet74K.txt")
        # wordGet.fit()

        accessor = AccessDatabase("127.0.0.1", 27017, "visearch")
        data = accessor.find("index", {}, {"term" : True, "_id" : False})
        words = set()
        for item in data:
            term = item["term"]
            words.add(term)
        # print(list(words)[:10])

        correct = WordCorrector()
        # correct.load()
        correct.setWords(words)
        correct.fit()

        while True:
            query = input("Enter your query: ")
            correct.predict(query)

        # accessor = AccessDatabase("127.0.0.1", 27017, "visearch")
        # data = accessor.find("index", {}, {"term" : True, "listIDs" : True, "_id" : False})
        # words = set()
        # for item in data:
        #     term = item["term"]
        #     term = Sentence(term).remove_accents()
        #     tokens = term.split("_")
        #     words.update(tokens)
        # print(list(words)[:10])
        # print(len(words))
        # count = dict()
        # for i in range(0, 10):
        #     count[i] = set()
        #     for term in words:
        #         if len(term) > i:
        #             count[i].add(term[i])
        #     print(len(count[i]), count[i])

Main()





from app.models.config_reader import ConfigReader
from app.models.parser import QueryParser
from app.models.judge.judger import Judger
from app.models.learning.learner import MachineLearner

class Main:

    def __init__(self):
        configer = ConfigReader("./app/config/service.conf")
        configer.parseFile()
        configInfo = configer.config
        dbHost, dbPort, dbName = configInfo["dbHost"], configInfo["dbPort"], configInfo["dbName"]
        parser = QueryParser(dbHost, dbPort, dbName)
        parser.loadModelCategory(configInfo["vectorFile"], configInfo["learnerModelFile"])
        parser.fit()
        parser.saveWordCorrect("./resource/wordCorrect.sav")

if __name__ == "__main__":
    Main()