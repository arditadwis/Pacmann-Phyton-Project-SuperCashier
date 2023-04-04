# PYTHON PACMANN PROJECT
KELAS SOFTWARE ENGINEERING - ARDITA DWI SETYONUGROHO
## Latar Belakang
Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya dengan harapan :
- Customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain.
- Customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. 

## Objektif
Membuat sistem kasir self service dengan feature sebagai berikut:
- Membuat proses untuk memasukkan ID Transaksi
- Membuat proses untuk menambahkan barang yang ini dibeli dan detail jumlah dan harganya   
- Membuat proses untuk mengupdate detail barang yang sudah diinputkan sebelumnya jika ada kesalahan input
- Membuat proses untuk menghapus salah satu pesanan yang telah diinputkan  
- Membuat proses untuk menghapus seluruh transaksi yang telah diinputkan
- Membuat proses untuk memeriksa apakah seluruh data yang diinput sudah benar dan lengkap
- Membuat proses untuk menghitung total belanja yang harus dibayarkan dan diskon yang didapatkan (jika dapat).

## Flowchart
[![flowchart](https://raw.githubusercontent.com/arditadwis/Pacmann-Phyton-Project-SuperCashier/main/flow%20chart.png)

## Penjelasan Code
a. Init Merupakan fungsi inisialisasi untuk class transaction
```
class transaction:
  def __init__(self,transactionID):
    self.transactionID = transactionID
transaction_1 = transaction(1)
transaction_123 = f'Transaksi {transaction_1.transactionID}'
print(transaction_123)    
```   
b. List Item untuk menampilkan (nama, qty, dan harga) dan variabel menu  
```
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
```
c. Add item dengan inputan menu = 1 (nama item, qty, harga)
```
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
```
d. Edit item untuk mengganti nama, qty, atau harga item (menu = 2)
```
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
```
e. Untuk menampilkan check order (menu = 3), menghapus salah satu item (menu = 4), atau menghapus semua item (menu =5)
```
elif menu == 3:
    print(list_item)

  elif menu == 4:
    print("index berapa yang ingin dihapus?")
    a=int(input())
    list_item = list_item.drop(list_item.index[a])

  elif menu == 5:
    print("semua item telah direset")
    list_item = list_item.iloc[0:0]
```
f. Menampilkan Total Harga dengan syarat- syarat untuk mendapatkan diskon
```
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
```
## Hasil Test Case
### Test 1:
Customer ingin menambahkan dua item baru:
- Nama Item: Ayam Goreng, Qty: 2, Harga: 20000
- Nama Item: Pasta Gigi, Qty: 3, Harga: 15000

| |nama_item | jumlah_item | harga_item| total_harga |
|-|----------|-------------|-----------|-------------|
|0| Ayam Goreng | 2.0 | 20000.0 | 40000.0|
|1| Pasta Gigi | 3.0    | 15000.0 |     45000.0|

### Test 2:
Ternyata Customer salah membeli salah satu item dari belanjaan yang sudah ditambahkan, maka Customer menghapus item Pasta Gigi.
|  |   nama_item|  jumlah_item|  harga_item|  total_harga|
|-|----------|-------------|-----------|-------------|
|0|  Ayam Goreng    |      2.0|     20000.0|      40000.0|

### Test 3:
Ternyata setelah dipikir - pikir Customer salah memasukkan item yang ingin dibelanjakan! Daripada menghapusnya satu - satu, maka Customer menghapus semua item yang sudah ditambahkan.
```
Empty DataFrame
Columns: [nama_item, jumlah_item, harga_item, total_harga]
```
### Test 4:
Setelah Customer selesai berbelanja, akan menghitung total belanja yang harus dibayarkan :
| | nama_item  |jumlah_item|  harga_item|  total_harga|
|-|------|-----|----------|------|
|0|   Ayam Goreng|          2.0     |20000.0|      40000.0|
|1  |  Pasta Gigi          |3.0|     15000.0      |45000.0|
|2 | Mainan Mobil          |1.0 |   200000.0     |200000.0|
|3|     Mi Instan          |5.0  |    3000.0    |  15000.0|
```
total belanja anda sebesar:300000.0
jumlah total belanjaan adalah 285000.0 dengan diskon 5%
```
## Kesimpulan
- Super cashier mempermudah customer dalam proses pembayaran 
- Untuk hasil coding silahkan dibuka di link [https://raw.githubusercontent.com/arditadwis/Pacmann-Phyton-Project-SuperCashier/main/main.py]
