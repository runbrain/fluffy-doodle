import pickle

#имя файла для сохранения объекта
shoplistfile = 'shoplist.data'
#список покупок
shoplist = ['яблоки','манго','морковь']

#запись в файл
f = open(shoplistfile,'wb')
pickle.dump(shoplist, f)
f.close()

del shoplist

f=open(shoplistfile, 'rb')
storedlist = pickle.load(f)
print(storedlist)