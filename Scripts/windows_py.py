import pandas as pd

from windows_help_function import get_conv_num, get_conv, get_new_frame, sentimental, get_GOLD_SET, compare_will, \
    compare_haoyu

df = pd.read_csv('merged-pythondev-help-concat-group.csv')

hul = get_conv_num('merged-pythondev-help-concat-group.csv')
print(hul)

answer_list = []

pos_data = 0
neu_data = 0
neg_data = 0
cant_data = 0
get_GOLD_SET(hul,'merged-pythondev-help-concat-group.csv')
for i in hul:
    get_conv(i,'merged-pythondev-help-concat-group.csv')
    get_new_frame(i, 'test_conv.csv')
    answer_list.append({"Conv ID": i, "Result" : sentimental('test_conv_finding.csv')})

f = pd.DataFrame(answer_list, columns=["Conv ID", "Result"])
f.to_csv("./final_result.csv", index=False)

df = pd.read_csv("./final_result.csv")
for i in range(df.shape[0]):
    if (df.iloc[i]["Result"] == "Positive"):
        pos_data += 1
    elif (df.iloc[i]["Result"] == "Negative"):
        neg_data += 1
    elif (df.iloc[i]["Result"] == "Undetermined"):
        neu_data += 1
    else:
        cant_data += 1


total_data = pos_data + neg_data + neu_data + cant_data
print("The percentage of positive data is: ",pos_data/total_data)
print("The percentage of negative data is: ",neg_data/total_data)
print("The percentage of undetermined data is: ",neu_data/total_data)
print("The percentage of cannot judge data is: ",cant_data/total_data)

compare_will("./final_result.csv","Gold_Set_Analysis.csv")
compare_haoyu("./final_result.csv","Gold_Set_Analysis.csv")
