
a = input('Masukkan Angka Anda Disini :')

a_split = a.split(' ')
list_a = list(a_split)

for i in range(0, len(list_a)): 
    list_a[i] = int(list_a[i]) 

evenlist_a = [] 
oddlist_a = [] 

for i in list_a: 
    if (i % 2) == 0: 
        evenlist_a.append(i) 
    else: 
        oddlist_a.append(i) 

print("Even listnya:", evenlist_a)
print("Odd listnya:", oddlist_a) 

evenlist_a.sort(reverse=True)
oddlist_a.sort(reverse=False)

print('List Setelah di Sorting Adalah : ',oddlist_a+evenlist_a)