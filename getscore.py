# encode=utf-8


act_f = open("./datas/act_31.csv", 'r')
pre_f = open("./datas/ans_31.csv", 'r')

# # 真正例
# TP = 0
# # 假正例
# FP = 0
# # 假负例
# FN = 0
# # 真负例
# TN = 0

act_list = act_f.readlines()
pre_list = pre_f.readlines()
act_set = set()
pre_set = set()
for line in act_list:
    line.replace("\n", '')
    arr = line.split(',')
    act_set.add((arr[0], arr[1]))
for line in pre_list:
    line.replace("\n", '')
    arr = line.split(',')
    pre_set.add((arr[0], arr[1]))


# TP = len(pre_set & act_set)
# FP = len(pre_set) - TP
# TN = len()

# 精确率
# precision = TP/(TP+FP)
precision = len(pre_set & act_set)/len(pre_set)
# 召回率
# recall = TP/(TP+FN)
recall = len(pre_set & act_set)/len(act_set)

print("命中个数: ", len(pre_set & act_set))


# F1值
f1 = 2*precision*recall/(precision+recall)
print("Your final score is %f." % f1)

act_f.close()
pre_f.close()