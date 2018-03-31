# encode=utf-8
import time
import numpy as np


# 1-30天的训练数据
train_data = []
# 预测第31天的购买
pre_data = []

# 读入数据
f = open('./datas/train_user.csv', 'r')
context = f.readlines()
f.close()

pre_f = open('./datas/act_31.csv', 'w')
pre_f.write("user_id,item_id\n")

# 预处理特征及标签
ui_dict = [{} for i in range(4)]
ui_buy = {}
for line in context:
    line = line.replace('\n', '')
    arr = line.split(',')
    if arr[0] == 'user_id':
        continue
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
        if no < 30:
            ui_buy[uid] = 1
        elif no == 30:
            pre_f.write(uid[0])
            pre_f.write(",")
            pre_f.write(uid[1])
            pre_f.write("\n")

    if no < 31:
        train_data.append(uid)
    else:
        pre_data.append(uid)
train_data = list(set(train_data))
pre_data = list(set(pre_data))
pre_f.close()


# 设置训练参数 X and y
X = np.zeros((len(train_data), 4))
y = np.zeros((len(train_data)))
for id, uid in enumerate(train_data):
    for i in range(4):
        X[id][i] = np.math.log1p(ui_dict[i][uid] if uid in ui_dict[i] else 0)
    y[id] = 1 if uid in ui_buy else 0


# 训练
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X, y)


# 设置第31天的特征
pX = np.zeros((len(pre_data), 4))
for id, uid in enumerate(pre_data):
    for i in range(4):
        pX[id][i] = np.math.log1p(ui_dict[i][uid] if uid in ui_dict[i] else 0)


# 评估
py = model.predict_proba(pX)
npy = []
for a in py:
    npy.append(a[1])
py = npy


# 将特征与预测概率绑定
lx = zip(pre_data, py)

# 按预测概率逆序排序
lx = sorted(lx, key=lambda x:x[1], reverse=True)


# 输出预测结果
psf = open("./datas/ans_31.csv", 'w')
psf.write("user_id,item_id,P\n")
for item in lx:
    if item[1] < 0.5:
        break
    psf.write('%s,%s,%f\n' % (item[0][0], item[0][1], item[1]))
psf.close()

