from config.config import config
import pickle

class Correct:

    def __init__(self):
        self.config = config["correcter"]
        self.load()

    def load(self):
        print("Loading correcter from %s" % self.config["correct_path"])
        with open(self.config["correct_path"], "rb") as datafile:
            self.core = pickle.load(datafile)
        print("Done!")
        self.num_queries = self.config["num_queries"]
        
    def predict(self, sentence):
        print(sentence)
        sentences = self.core.predict([sentence])
        return sentences[0][:self.num_queries] if len(sentences) > 0 else sentence