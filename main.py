matn = input("Matn kiriting: ")
unli_harflar = "aeiouAEIOU"
s = sum(1 for harf in matn if harf in unli_harflar)
print(s)