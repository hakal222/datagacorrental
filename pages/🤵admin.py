import streamlit as st
import pandas as pd

class Database:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = pd.read_csv(csv_file)

    def create_record(self, data):
        new_record = pd.DataFrame([data])
        self.df = pd.concat([self.df, new_record], ignore_index=True)
        self.df.to_csv(self.csv_file, index=False)

    def read_records(self):
        return self.df

    def update_record(self, index, data):
        self.df.loc[index] = data
        self.df.to_csv(self.csv_file, index=False)

    def delete_record(self, index):
        self.df = self.df.drop(index)
        self.df.to_csv(self.csv_file, index=False)
        

if 'admin' not in st.session_state:
    st.session_state.admin = False

# st.write(st.session_state.admin)
if st.session_state.admin:
    st.header("SELAMAT DATANG ADMIN DGR")
    db = Database("data.csv")

    st.write(db.read_records())

    for index, row in db.read_records().iterrows():
        if st.button(f"Baris {index} - Berhasil"):
            df = db.read_records()
            data = {
                'nama_pelanggan': df["nama_pelanggan"][index],
                'tanggal_penyewaan': df["tanggal_penyewaan"][index],
                'durasi_penyewaan': df["durasi_penyewaan"][index],
                'waktu_jemput': df["waktu_jemput"][index],
                'jenis_mobil': df["jenis_mobil"][index],
                'sewa_mobil': df["sewa_mobil"][index],
                'asuransi': df["asuransi"][index],
                'driver': df["driver"][index],
                'lokasi': df["lokasi"][index],
                'biaya_total': df["biaya_total"][index],
                'metode_pembayaran': df["metode_pembayaran"][index],
                'Status': 'Berhasil'
            }
            db.update_record(index,data)
            st.write(f"Baris {index} - Data berhasil diupdate.")

        if st.button(f"Baris {index} - Gagal"):
            df = db.read_records()
            data = {
                'nama_pelanggan': df["nama_pelanggan"][index],
                'tanggal_penyewaan': df["tanggal_penyewaan"][index],
                'durasi_penyewaan': df["durasi_penyewaan"][index],
                'waktu_jemput': df["waktu_jemput"][index],
                'jenis_mobil': df["jenis_mobil"][index],
                'sewa_mobil': df["sewa_mobil"][index],
                'asuransi': df["asuransi"][index],
                'driver': df["driver"][index],
                'lokasi': df["lokasi"][index],
                'biaya_total': df["biaya_total"][index],
                'metode_pembayaran': df["metode_pembayaran"][index],
                'Status': 'Gagal'
                }
            db.update_record(index,data)
            st.write(f"Baris {index} - Data gagal diupdate.")

else:
    container = st.write("LOGIN ADMIN")
    username = st.text_input("adminname")
    password = st.text_input("password")

    if st.button("Login"):
        if username == "admin" and password == "12345":
            st.session_state.admin = True
            st.rerun()
        else:
            st.write("PassWord SALAH")