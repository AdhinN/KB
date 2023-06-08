gejala = [
    {"kode" : "G01", "cf" : 0.8},
    {"kode" : "G02", "cf" : 0.6},
    {"kode" : "G03", "cf" : 0.5},
    {"kode" : "G04", "cf" : 0.2},
    {"kode" : "G05", "cf" : 0.5},
    {"kode" : "G06", "cf" : 0.5}
]
penyakit = [
    {"kode_penyakit" : "P01", "penyakit": 'A', "gejala" : ["G01", "G03"]},
    {"kode_penyakit" : "P02", "penyakit": 'B', "gejala" : ["G02", "G03", "G06"]},
    {"kode_penyakit" : "P03", "penyakit": 'C', "gejala" : ["G01", "G02", "G04", "G05"]},
    {"kode_penyakit" : "P04", "penyakit": 'D', "gejala" : ["G05", "G06"]}
]
pasien = [
    {"kode" : "G01", "cf" : 0.5},
    {"kode" : "G05", "cf" : 0.8},
    {"kode" : "G04", "cf" : 0.4},
    {"kode" : "G02", "cf" : 0.3},
    {"kode" : "G03", "cf" : 0.2}
]

def certainty_factor(penyakit, pasien):
    cf = 0
    for gejala_penyakit in penyakit["gejala"]:
        for p in pasien:
            if p["kode"] == gejala_penyakit:
                for g in gejala:
                    if g["kode"] == gejala_penyakit:
                        proses = p["cf"] * g["cf"]
                        cf = cf + proses * (1 - abs(cf))
                        break
    return cf

for penyakit in penyakit:
    print(penyakit["penyakit"], str(certainty_factor(penyakit, pasien)*100)+'%')