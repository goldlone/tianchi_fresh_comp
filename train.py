# code=utf-8
import time
import math
import numpy as np


train_day29 = []
offline_candidate_day30 = []
online_candidate_day31 = []

# 读入数据
f = open('./28_31.csv', 'r')
context = f.readlines()

# 预处理特征及标签
ui_dict = [{} for i in range(4)]
ui_buy = {}
for line in context:
    line = line.replace('\n', '')
    arr = line.split(',')
    # if arr[0] == 'user_id':
    #     continue
    date = arr[-1]
    d = time.strptime(date, "%Y-%m-%d %H")
    month = d.tm_mon
    day = d.tm_mday
    if month == 11:
        no = day - 18
    else:
        no = day + 13
    uid = (arr[0], arr[1], no)
    op = int(arr[2]) - 1
    # 选择特征
    if uid in ui_dict[op]:
        ui_dict[op][uid] += 1
    else:
        ui_dict[op][uid] = 1
    # 设置标签
    if op == 3:
        ui_buy[uid] = 1

    if no == 29:
        train_day29.append(uid)
    elif no == 30:
        offline_candidate_day30.append(uid)
    elif no == 31:
        online_candidate_day31.append(uid)
train_day29 = list(set(train_day29))
offline_candidate_day30 = list(set(offline_candidate_day30))
online_candidate_day31 = list(set(online_candidate_day31))

# dd = ui_dict[3]
# for i in dd:
#     print(i)

# dd = ui_buy
# print("The length is %d" % len(ui_buy))
# print()
# for k, v in dd.items():
#     print(k, " - ", v)

# fout = open('./ooo.txt', 'w')

# 设置训练参数 X and y
# print(len(train_day29))
X = np.zeros((len(train_day29), 4))
y = np.zeros((len(train_day29)))
for id, uid in enumerate(train_day29):
    # last_uid = (uid[0], uid[1], uid[2])
    last_uid = uid
    for i in range(4):
        X[id][i] = math.log1p(ui_dict[i][last_uid] if last_uid in ui_dict[i] else 0)
        # print("X[%d][%d] -> %f" % (id, i, X[id][i]))
        # fout.write("X[%d][%d] -> %f\n" % (id, i, X[id][i]))
    if uid in ui_buy:
        y[id] = 1
    else:
        y[id] = 0

    # y[id] = 1 if uid in ui_buy else 0
    # print("y[%d] -> %f" % (id, y[id]))
    # fout.write("y[%d] -> %f\n" % (id, y[id]))

# fout.close()

# for i in range(50):
#     print(X[i])
#     print(y[i])
#     print()



# 设置第30天的特征
pX = np.zeros((len(offline_candidate_day30), 4))
for id, uid in enumerate(offline_candidate_day30):
    # last_uid = (uid[0], uid[1], uid[2] - 1)
    last_uid = uid
    for i in range(4):
        pX[id][i] = math.log1p(ui_dict[i][last_uid] if last_uid in ui_dict[i] else 0)




# 训练
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X, y)

# print("------------")
# print("weight = ", model.class_weight)
# print("coef = ", model.coef_)
# print("------------")


# 评估
py = model.predict_proba(pX)
print("py = ", py)
print()
npy = []
for a in py:
    npy.append(a[1])
py = npy
print("pX = ", pX)
print()



# combine
lx = zip(offline_candidate_day30, py)
# print lx
# print("-----------")
# print(lx)
# print("-----------")



# sort by predict score
lx = sorted(lx, key=lambda x : x[1], reverse=True)
# print lx
print("-----------")
print(lx)

wf = open("ans.cvs", 'w')
wf.write('user_id,item_id\n')
for item in lx:
    print("user_id=%s,item_id=%s,P=%f" % (item[0][0], item[0][1], item[1]))
    if item[1] > 0.5:
        wf.write('%s,%s,%f\n' % (item[0][0], item[0][1], item[1]))

# for i in range(len(lx)):
#     item = lx[i]
#     wf.write('%s,%s,%f\n' % (item[0][0], item[0][1], item[1]))

wf.close()
f.close()