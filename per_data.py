# code=utf-8
import time
import datetime

start_time = datetime.datetime.now()

train_day29 = []
offline_candidate_day30 = []
online_candidate_day31 = []

# 筛选出28-31的数据
out = open('./28_31.csv', 'w')
with open('./train_user.csv') as f:
    context = f.readlines()
    for line in context:
        line1 = line.replace('\n', '')
        arr = line1.split(',')
        if arr[0] == 'user_id':
            continue
        date = arr[-1]
        d = time.strptime(date, "%Y-%m-%d %H")
        month = d.tm_mon
        day = d.tm_mday
        if month == 11:
            no = day-18
        else:
            no = day+13
        if no > 27:
            out.write(line)
out.close()




# 将数据读入
# with open('./train_user.csv') as f:
# with open('./test.csv') as f:
#     context = f.readlines()
#     for line in context:
#         line = line.replace('\n', '')
#         arr = line.split(',')
#         if arr[0] == 'user_id':
#             continue
#         date = arr[-1]
#         d = time.strptime(date, "%Y-%m-%d %H")
#         month = d.tm_mon
#         day = d.tm_mday
#         if month == 11:
#             no = day-18
#         else:
#             no = day+13
#
#         uid = (arr[0], arr[1], no)
#         print(no)
#         if no == 29:
#             train_day29.append(uid)
#         elif no == 30:
#             offline_candidate_day30.append(uid)
#         elif no == 31:
#             online_candidate_day31.append(uid)
#
# train_day29 = list(set(train_day29))
# offline_candidate_day30 = list(set(offline_candidate_day30))
# online_candidate_day31 = list(set(online_candidate_day31))
#
# out1 = open("./29.txt", 'w')
# out2 = open("./30.txt", 'w')
# out3 = open("./31.txt", 'w')
#
# out1.writelines(train_day29)
# out2.writelines(offline_candidate_day30)
# out3.writelines(online_candidate_day31)
#
# # print("train_day29 length = ", len(train_day29))
# # print("offline_candidate_day30 length = ", len(offline_candidate_day30))
# # print("online_candidate_day31 length = ", len(online_candidate_day31))
#
# out1.close()
# out2.close()
# out3.close()

end_time = datetime.datetime.now()
print("程序运行时间: %ds" % (end_time-start_time).seconds)