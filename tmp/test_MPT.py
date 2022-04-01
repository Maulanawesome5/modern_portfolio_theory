# Load package
import numpy as np
import pandas as pd
from pandas_datareader import data
import matplotlib.pyplot as plt

# Membaca data harga saham dengan metode scrapping
test = data.DataReader(
    ['APLN.JK', 'ASRI.JK'], 'yahoo',
    start = '2020/12/07',
    end = '2021/12/07')

# Harga closing
test = test['Adj Close']
print(test.head())

# Menghitung persentase perubahan harga
apln = test['APLN.JK'].pct_change().apply(lambda x: np.log(1 + x))
asri = test['ASRI.JK'].pct_change().apply(lambda x: np.log(1 + x))
print("\n", apln.head(), asri.head())

# Menghitung varians harga saham
varians_apln = apln.var()
varians_asri = asri.var()
print("\n",f"Varians APLN.JK = {varians_apln}, Varians ASRI.JK = {varians_asri} ")

# Menghitung volatilitas pergerakan saham
apln_volatile = np.sqrt(varians_apln * 250)
asri_volatile = np.sqrt(varians_asri * 250)
print("\n",f"Volatilitas APLN.JK = {apln_volatile}, Volatilitas ASRI.JK = {asri_volatile} ")

# Menampilkan volatilitas kedua saham menjadi bentuk diagram batang
test.pct_change().apply(
    lambda x: np.log(1 + x)).std().apply(
        lambda x: x*np.sqrt(250)).plot(kind='bar')
# plt.show()

# Persentase perubahan
test1 = test.pct_change().apply(lambda x: np.log(1+x))
print(test1.head())

# Menghitung covariance kedua saham
test1['APLN.JK'].cov(test1['ASRI.JK'])
print("\n\tNilai Covariance antara APLN dengan ASRI \n",test1)

# Menghitung correlation antara kedua saham
test1['APLN.JK'].corr(test1['ASRI.JK'])
print("\n\tNilai Correlation antara APLN dengan ASRI \n", test1)

# Menghitung Expected Return kedua saham
test2 = test.pct_change().apply(lambda x: np.log(1 + x))
print("\n\tNilai Expected Return antara APLN dengan ASRI \n", test2)

# Menghitung bobot (weight) untuk alokasi dana terhadap kedua saham
bobot = [0.2, 0.8] # define bobot untuk alokasi dana
e_r_ind = test2.mean()
print("\n\tBobot expected return APLN dengan ASRI \n",e_r_ind)

# Total expected return
e_r = (e_r_ind * bobot).sum()
print("\n\tTotal expected return saham ASRI dan APLN \n", e_r)
