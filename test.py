import pickle

my = ['knife', 'ball']
save_file = open('C:\\Users\\user\\Desktop\\питон\\save.txt', 'wb')
pickle.dump(my, save_file)
save_file.close()
t = open('C:\\Users\\user\\Desktop\\питон\\save.txt', 'rb')
d = pickle.load(t)
t.close()
print(d)