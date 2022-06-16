import csv
from fpdf import FPDF
import os

judul = "JAKARTA PYTHON AIRLINES"
judul = judul.center(96)
harga = 15000000
tujuan = "SYDNEY"
waktu = "08.00 WIB"
pesawat = "PY 2021 INF"
seat = ['1A', '1B', '1C', '2A', '2B', '2C', '3A', '3B', '3C', '4A', '4B', '4C', '5A', '5B', '5C']
pilihan = []

def data_nama():
    global nama
    nama = str(input("Nama Pembeli\t\t\t\t: "))
    if nama == "":
        print("Belum ada data yang diinputkan")
        data_nama()
    return nama
def data_no():
    global no
    try:
        no = int(input("Nomor HP\t\t\t\t: +62 "))
        if no == "":
            print("Belum ada data yang diinputkan")
            data_no()
    except ValueError:
        print("Nomor HP tidak valid, ulangi sekali lagi")
        data_no()
    return no
def data_asal():
    global asal
    asal = str(input("Asal Kota\t\t\t\t: "))
    if asal == "":
        print("Belum ada data yang diinputkan")
        data_asal()
    return asal
    
def hitung():
    global bayar
    def nota(): 
        print(judul, "\n ")
        print("Nama pembeli\t\t\t\t:", nama)
        print("No HP\t\t\t\t\t: +62", no)
        print("Asal kota\t\t\t\t:", asal)
        print("Tujuan\t\t\t\t\t:", tujuan)
        print("Waktu\t\t\t\t\t:", waktu)
        print("Seat\t\t\t\t\t:", end=" ")
        for i in range(len(pilihan)):
            if i == len(pilihan)-1:
                print(pilihan[i])
            else:
                print(pilihan[i], end=", ")
        print("Pesawat\t\t\t\t\t:", pesawat)
        print("Total pembayaran\t\t\t: Rp", int(bayar))
    beli = len(pilihan)
    if beli % 5 == 0:
        diskon = beli / 5
        potongan = harga * 5 * diskon * 5/100
        total = (harga * beli) - potongan
        print('Total pembelian: Rp', int(total))
        print("Pajak 10%")
        pajak = total * 10/100
        bayar = total + pajak
        print("Jumlah pembayaran Anda: Rp", int(bayar))
        uang = int(input("Jumlah uang: Rp "))
        kembalian = uang - bayar
        print("Uang kembalian sebesar: Rp", int(kembalian))
        nota()
    elif beli % 5 != 0:
        total = harga * beli
        print()
        print('Total pembelian\t\t\t\t: Rp', int(total))
        print("\t\t\t\t\t\t\t\t\t\t+Pajak 10%")
        pajak = total * 10/100
        bayar = total + pajak
        print("Jumlah pembayaran Anda\t\t\t: Rp", int(bayar))
        uang = int(input("Jumlah uang\t\t\t\t: Rp "))
        kembalian = uang - bayar
        print("Uang kembalian sebesar\t\t\t: Rp", int(kembalian))
        print()
        nota()

def P():
    def Q():
        print()
        print('Seat:', seat)
        print()
        print("Seat terpilih\t\t\t\t: ", pilihan)
        print()
        y = str(input("Apakah ada pilihan seat lagi? (Y/N)\t: "))
        if y == "Y":
            P()
        elif y == "N":
            hitung()
        else:
            print("Terjadi kesalahan input, coba periksa kembali")
            Q()
    print()
    print('Seat:', seat)
    print()
    x = str(input("Pilih seat\t\t\t\t: "))
    if x == '':
        print("Terjadi kesalahan input, coba periksa kembali")
        P()
    else:
        if seat.count(x) != 0:
            seat.remove(x)
            pilihan.append(x)
            Q()    
        elif seat.count(x) == 0:
            print("Seat tidak tersedia, coba seat lain")
            P()

def logbill():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    kursi = ''
    for i in range(len(pilihan)):
        if i == len(pilihan) - 1:
            kursi = kursi + pilihan[i] 
        else:    
            kursi = kursi + pilihan[i] + ', '
    bill = nama, no, asal, tujuan, waktu, kursi, pesawat, int(bayar)
    with open('{}\\LOGTIKET.csv'.format(dir_path), 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=";")
        csv_writer.writerow(bill)

def PDF():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    pdf=FPDF()
    pdf.add_page()
    pdf.set_font("Arial","B", size=14)
    pdf.cell(200,10, txt='JAKARTA PYTHON AIRLINES', ln=1, align="C")
    pdf.set_font("Arial", size=12)
    pdf.cell(100,10, txt="Nama Pembeli: {}".format(nama),ln=2, align="L")
    pdf.cell(100,10, txt="No Hp: +62 {} ".format(no), ln=2, align="L")
    pdf.cell(100,10, txt="Asal Kota: {}".format(asal), ln=2, align="L")
    pdf.cell(100,10, txt="Tujuan: {}".format(tujuan), ln=2, align="L")
    pdf.cell(100,10, txt="Waktu: {}".format(waktu), ln=2, align="L")
    kursi = ''
    for i in range(len(pilihan)):
        if i == len(pilihan) - 1:
            kursi = kursi + pilihan[i] 
        else:    
            kursi = kursi + pilihan[i] + ', '
    pdf.cell(100,10, txt="Seat: {}".format(kursi), ln=2, align="L")
    pdf.cell(100,10, txt="Pesawat: {}".format(pesawat), ln=2, align="L")
    pdf.cell(100,10, txt="Total Pembayaran: Rp{}".format(int(bayar)), ln=2, align="L")
    pdf.output("{}\\TIKET.pdf".format(dir_path))
            
def main():
    def runapp():
        run = str(input("Mengulang aplikasi? (Y/N)\t\t: "))
        if run == "Y":
            pilihan.clear()
            print()
            main()
        elif run == "N":
            pass
        else:
            print("Terjadi kesalahan input, coba periksa kembali")
            runapp()
    print(judul, "\n ")
    data_nama()
    data_no()
    data_asal()
    P()
    logbill()
    PDF()
    print()
    runapp()

if __name__ == "__main__":
    main()