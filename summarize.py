from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

def summarize_transcript(document):
    auto_abstractor = AutoAbstractor()
    auto_abstractor.tokenizable_doc = SimpleTokenizer()
    auto_abstractor.delimiter_list = [".", "\n"]
    abstractable_doc = TopNRankAbstractor()
    
    result_dict = auto_abstractor.summarize(document, abstractable_doc)

    summarized_text = []
    for sentence in result_dict["summarize_result"]:
        summarized_text.append(sentence)
        
    summarized_text = " ".join(summarized_text)
    
    return summarized_text
