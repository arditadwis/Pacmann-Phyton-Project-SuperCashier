from tabulate import tabulate
from dataclasses import dataclass
import numpy as np
import pandas as pd

class transaction:
  def __init__(self,transactionID):
    self.transactionID = transactionID

transaction_1 = transaction(1)
transaction_123 = f'Transaksi {transaction_1.transactionID}'
print(transaction_123)    
    

list_item = ({
    'nama_item':[],
    'jumlah_item' :[],
    'harga_item':[],
    'total_harga':[]
})

menu1 = 'y'

while menu1 == 'y':
  print("==========Toko Andi Kasir Mandiri==========")
  print("Pilih menu: " )
  print("1.input item " )
  print("2.edit item ")
  print("3.check list ")
  print("4.delete item ")
  print("5.reset semua item")
  print("6.total harga ") 
  print("7.exit")
  print("===========================================")
  print(list_item)
  menu=int(input())
  if menu == 1:
      a=input("masukan nama item : ")
      b=int(input("masukan jumlah item :"))
      c=int(input("masukan harga item :"))
      d= b*c
      df = pd.DataFrame.from_dict(list_item)
      new_row = {'nama_item':a, 'jumlah_item' : b, 'harga_item':c, 'total_harga':d}
      df = df.append(new_row, ignore_index=True)
      list_item = df
  elif menu == 2:
    print("apa yang ingin diganti?")
    print("1.nama item ")
    print("2.jumlah item ")
    print("3.harga item ")
    submenu1=int(input())
    if submenu1 == 1:
        a=input("masukan nama item yang ingin diganti :")
        b=input("masukan nama item baru : ")
        list_item = list_item.replace([a], b)
    elif submenu1 == 2:
        a=int(input("masukan jumlah item yang ingin diganti : "))
        b=int(input("masukan jumlah item baru ;"))
        list_item['jumlah_item'] = list_item['jumlah_item'].replace([a], b)

    elif submenu1 == 3:
        a=int(input("masukan harga item yang ingin diganti :"))
        b=int(input("masukan harga item baru :"))
        list_item['harga_item'] = list_item['harga_item'].replace([a], b)
    else:
        print("kata kunci salah, kembali ke menu utama")

  elif menu == 3:
    print(list_item)

  elif menu == 4:
    print("index berapa yang ingin dihapus?")
    a=int(input())
    list_item = list_item.drop(list_item.index[a])

  elif menu == 5:
    print("semua item telah direset")
    list_item = list_item.iloc[0:0]

  elif menu == 6:
    Total = list_item['total_harga'].sum()
    print(f'total belanja anda sebesar:{Total}')
    if Total >= 200000 :
          diskon=Total*0.05
          Total=Total-diskon
          print(f'jumlah total belanjaan adalah {Total} dengan diskon 5%')
    elif Total >= 300000 :
          diskon=Total*0.08
          Total=Total-diskon
          print(f'jumlah total belanjaan adalah {Total} dengan diskon 8%')
    elif Total >= 500000:
          diskon=Total*0.1
          Total=Total-diskon
          print(f'jumlah total belanjaan adalah {Total} dengan diskon 10%')

  elif menu == 7:
    menu1 = 'n'