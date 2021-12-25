arr = [1,3,4,2,5,6,3,2]
setarr= set(arr)
if len(arr) == len(setarr):
    print('все элементы уникальны')
else:
    print ('не все элементы уникальны')
print('длина arr=', len(arr))
print('длина setarr=', len(setarr))
