import re
import collections
from typing import List, Optional, Union


class Tokenizer:
    def __init__(self, corpus: Optional[Union[List[str], str]] = None):
        if not isinstance(corpus, Union[List[str], str, None]):
            raise TypeError("'corpus' should be a string/a list of strings")
        if isinstance(corpus, List[str]):
            self.corpus = " ".join(self.corpus)
        else:
            self.corpus = corpus

    def add_corpus(self, corpus: Union[List[str], str]) -> None:
        if not isinstance(corpus, Union[List[str], str]):
            raise TypeError("'corpus' should be a string/a list of strings")
        if isinstance(corpus, List[str]):
            corpus = " ".join(corpus)
            self.corpus += " " + corpus
        else:
            self.corpus += " " + corpus

class text_preprocess:
    def __init__(self, text: str):
        self.text = text
        regex = r"[^a-zA-Z]"
        self.text = re.sub(regex, " ", self.text)
        self.text = self.text.lower()
        return self.text

class BPETokenizer(Tokenizer):
    def __init__(self, corpus):
        super().__init__(corpus)
        self.vocab = {}
    
    def add_corpus(self):
        self.add_corpus()
        
    def make_vocab(self):
        words = self.corpus.split()
        for word in words:
            self.vocab[' '.join(word)+' </w>'] = self.corpus.count(word)
        return self.vocab
            
    def get_stats(self):
        self.pairs = collections.defaultdict(int)
        for word, freq in self.vocab.items():
            symbols = word.split()
            self.pairs.update(zip(zip(symbols, symbols[1:]), [freq] * (len(symbols) - 1)))
        return self.pairs    
    
    def merge_vocab(self):
        v_out = {}
        bigram = re.escape(' '.join(self.pairs))
        p = re.compile(r'(?<!\S)' + bigram + r'(?!\S)')
        for word, count in self.vocab.items():
            w_out = p.sub(''.join(self.pairs), word)
            v_out[w_out] = count
        return v_out
    
    def tokenize(
        text: Union[List[str], str],
        padding: bool = False,
        max_length: Optional[int] = None
        ) -> Union[List[List[int]], List[int]]:
        if not isinstance(text, Union[List[str], str]):
            raise TypeError("'text' should be a string/a list of strings")
        if isinstance(text, List[str]):
            text = " ".join(text)
            text += " " + text
        else:
            text += " " + text
            

class WordTokenizer(Tokenizer):
    def __init__(self, corpus):
        super().__init__(corpus)
        self.vocab = {}
        
    def add_corpus(self):
        self.add_corpus()
        
    def make_vocab(self, text: str):
        words = text.split()
        for word in words:
            self.vocab[word + '</w>'] = text.count(word)
        return self.vocab
        
    def tokenizer(
        self,
        text: Union[List[str], str],
        padding: bool = False,
        max_length: Optional[int] = None
        ) -> Union[List[List[int]], List[int]]:        
        if not isinstance(text, Union[List[str], str]):
            raise TypeError("'text' should be a string/a list of strings")
        if isinstance(text, List[str]):
            string = " ".join(text)
            string += " " + string
        else:
            string = " " + text
            
        self.make_vocab(string)
        vocab = list(self.vocab.keys())
        token_id = {}
        for id, token in zip(range(len(vocab)), vocab):
            token_id[token] = id
        
        if isinstance(text, List[str]):
            tokenized = []
            for t in text:
                l = t.split()
                for i, w in zip(range(len(l)), l):
                    l[i] = token_id[w]        
                tokenized.append(t)
        else:
            l = text.split()
            for i, w in zip(range(len(l)),l):
                l[i] = token_id[w] 
                tokenized = l
        
        if isinstance(text, List[str]) & padding:
            text.sorted(key=len, reverse=True)
            maxlen = len(text[0])
            for i ,s in zip(range(len(tokenized)), tokenized):
                if len(s) < maxlen:
                    tokenized[i] = s.extend([0] * (maxlen - len(s)))
                    
        if max_length:
            for i ,s in zip(range(len(tokenized)), tokenized):
                if len(s) > max_length:
                    tokenized[i] = s[:max_length]  
                    
        return tokenized
        
        