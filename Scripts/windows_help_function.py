import pandas as pd
import re
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.download('vader_lexicon')

from pandas.core.indexing import convert_from_missing_indexer_tuple

def get_conv_num(a_csv):
    df = pd.read_csv(a_csv)
    have_url_list = []
    for i in range(df.shape[0]):
        if (df.iloc[i]["message"].count('http', 0, len(df.iloc[i]["message"]))):
            if df.iloc[i]["thread"] not in have_url_list:
                have_url_list.append(df.iloc[i]["thread"])
    return  have_url_list

def get_conv(a_conv_number,a_csv):
    conv_context = []
    df = pd.read_csv(a_csv)
    for i in range(df.shape[0]):
        if(df.iloc[i]["thread"]) == a_conv_number:
            conv_context.append({"speaker": df.iloc[i]["speaker"], "message": df.iloc[i]["message"]})
    f = pd.DataFrame(conv_context, columns=["speaker", "message"])
    f.to_csv("./test_conv.csv", index=False)
    ##print(conv_context)

def get_new_frame(id, a_csv):
    conv_context = []
    df = pd.read_csv(a_csv)
    for i in range(df.shape[0]):
        if "http" in df.iloc[i]["message"]:
            if (i != df.shape[0]-1):
                conv_context.append({"id": id, "Response": df.iloc[i+1]["message"]})
            else:
                conv_context.append({"id": id, "Response": "Nothing there"})
    f = pd.DataFrame(conv_context, columns=["id", "Questioner","Question","Response"])
    f.to_csv("./test_conv_finding.csv", index=False)

def get_GOLD_SET(ids, a_csv):
    conv_context = []
    df = pd.read_csv(a_csv)
    count = 0
    for each_id in ids:
        for i in range(df.shape[0]):
            if df.iloc[i]["thread"] == each_id:
                if "http" in df.iloc[i]["message"]:
                    if (df.iloc[i+1]["thread"] == df.iloc[i]["thread"]):
                        conv_context.append({"id": each_id,"Response": df.iloc[i+1]["message"]})
                    else:
                        conv_context.append({"id": each_id,"Response": "Nothing there"})
        count += 1
        if count == 100:
            break
    f = pd.DataFrame(conv_context, columns=["id","Response"])
    f.to_csv("./for_gold_set.csv", index=False)


def sentimental(a_csv):
    data = []
    df = pd.read_csv(a_csv)
    for i in range(df.shape[0]):
        data.append(df.iloc[i]["Response"])

    sid = SentimentIntensityAnalyzer()
    pos_score = 0
    neu_score = 0
    neg_score = 0

    for sen in data:
        if sen != "Nothing there":
            ss = sid.polarity_scores(sen)
            for k in ss:
                if (k == 'neg'):
                    neg_score += ss[k]
                elif(k == 'neu'):
                    neu_score += ss[k]
                elif(k == 'pos'):
                    pos_score += ss[k]
    if(pos_score+neg_score+neu_score) != 0:
        if(pos_score+neg_score > 0.03):
            if(pos_score > neg_score):
                return("Positive")
            else:
                return("Negative")
        else:
            return("Understatement")
    else:
        return ("Undetermined")

def compare_will(a_test,a_gold):
    right_list = []
    wrong_list = []
    ad = pd.read_csv(a_test)
    dd = pd.read_csv(a_gold)
    for i in range(69):
        if(ad.iloc[i]["Result"] != dd.iloc[i]["WILL DETERMINATION"]):
            wrong_list.append(ad.iloc[i]["Conv ID"])

        else:
            right_list.append(ad.iloc[i]["Conv ID"])
    print("Compare with Will's determination:")
    print("Right Conv ID are:" )
    print(right_list)
    print("Wrong Conv ID are:" )
    print(wrong_list)

def compare_haoyu(a_test,a_gold):
    right_list = []
    wrong_list = []
    ad = pd.read_csv(a_test)
    dd = pd.read_csv(a_gold)
    for i in range(69):
        if(ad.iloc[i]["Result"] != dd.iloc[i]["HAOYU DETERMINATION"]):
            wrong_list.append(ad.iloc[i]["Conv ID"])

        else:
            right_list.append(ad.iloc[i]["Conv ID"])
    print("Compare with Haoyu's determination:")
    print("Right Conv ID are:" )
    print(right_list)
    print("Wrong Conv ID are:" )
    print(wrong_list)










