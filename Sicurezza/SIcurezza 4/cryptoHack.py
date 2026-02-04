from Crypto.PublicKey import RSA

# chiave fornita
chiave = ("ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQCtPLqba+GF"
+"vDHdFVs1Vvdk56cKqqw5cdomlu034666UsoFIqkig8H5kNsNefSpaR/iU7G0ZK"
+"CiWRRuAbTsuHN+Cz526XhQvzgKTBkTGYXdF/WdG/6/umou3Z0+wJvTZgvEmeEcl"
+"vitBrPZkzhAK1M5ypgNR4p8scJplTgSSb84Ckqul/Dj/Sh+fwo6sU3S3j92qc27B"
+"VGChpQiGwjjut4CkHauzQA/gKCBIiLyzoFcLEHhjOBOEErnvrRPWCIAJhALkwV2rU"
+"bD4g1IWa7QI2q3nB0nlnjPnjjwaR7TpH4gy2NSIYNDdC1PZ8reBaFnGTXgzhQ2t0ROB"
+"Nb+ZDgH8Fy+KTG+gEakpu20bRqB86NN6frDLOkZ9x3w32tJtqqrJTALy4Oi3MW0XPO61"
+"UBT133VNqAbNYGE2gx+mXBVOezbsY46C/V2fmxBJJKY/SFNs8wOVOHKwqRH0GI5VsG1YZ"
+"ClX3fqk8GDJYREaoyoL3HKQt1Ue/ZW7TlPRYzAoIB62C0= bschneier@facts")

'''
la funziona importKey capisce automaticamente che tipo di chiave le viene
passata come argomento: si occupa dell'analisi dell'intestazione, della pulizia
delle parti non necessarie, decodifica e interpreta matematicamente il contenuto
'''
key = RSA.importKey(chiave)

print(key.n)
# n, divenuta proprietà di key, è il modulo che stiamo cercando
