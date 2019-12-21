
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
        parser.loadWordCorrect(configInfo["wordCorrectFile"])
        parser.loadSentenceCorrect(configInfo["sentenceCorrectFile"])
        parser.loadSynonym()
        history = [
            "mongodb",
            "sao Hoa",
            "bong ma ben ngoai cua so",
            "cai gi z troi",
            "search ngu qua a"
        ]
        while True:
            query = input("Enter your query: ")
            print(parser.predict(query, history))

if __name__ == "__main__":
    Main()
