from spellchecker import SpellChecker
from gensim.models import Word2Vec

#get the highlighted word as input
#let say the variable of retrieved word is w_input
ts_model = Word2Vec.load("../newtrained_model/tsdict_w2v_cbow.model")


class TSDictionary():
    def check_en(self, word):
        spell = SpellChecker()
        word = word.lower()
        try:
            i = 0
            sim = 0
            highest_sim = []
            while i < 5:
                sim_word = ts_model.wv.most_similar([str(word)], topn=5000)[sim][0]
                sim += 1
                inner_check_text = spell.unknown([sim_word])
                if len(inner_check_text) == 0:
                    if sim_word.isdigit() != True:
                        highest_sim.append(sim_word)
                        i += 1
        except Exception as e:
            print("Word is not in thesaurus")
        if len(highest_sim) != 0:
            print(highest_sim)


ts_dict = TSDictionary()
print("Enter blank space to exit")
w_input = input("Search for textspeak: ")
while w_input != "":
    ts_dict.check_en(str(w_input))
    w_input = input("Search for textspeak: ")

