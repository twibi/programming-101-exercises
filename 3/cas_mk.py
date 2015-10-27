"""
sentence = 'Чекај малку, што правам?'
new_sentence = ''
trs={'б':'b', 'в':'v', 'г':'g', 'д':'d', 'ѓ':'gj', 'ж':'zh', 'з':'z', 'ѕ':'dz', 'љ':'lj', 'њ':'nj', 'ќ':'kj', 'ч':'ch', 'џ':'dzh', 'ш':'sh'}

for n in sentence:
	if n in trs:
		new_sentence = new_sentence + trs[n]
	else:
		new_sentence = new_sentence + n

print(new_sentence)
"""



lst1=['а', 'б', 'в', 'г', 'д', 'ѓ', 'е', 'ж', 'з', 'ѕ', 'и', 'ј', 'к', 'л', 'љ', 'м', 'н', 'њ', 'о', 'п', 'р', 'с', 'т', 'ќ', 'у', 'ф', 'х', 'ц', 'ч', 'џ', 'ш', 'А', 'Б', 'В', 'Г', 'Д', 'Ѓ', 'Е', 'Ж', 'З', 'Ѕ', 'И', 'Ј', 'К', 'Л', 'Љ', 'М', 'Н', 'Њ', 'О', 'П', 'Р', 'С', 'Т', 'Ќ', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Џ', 'Ш']
lst2=['a', 'b', 'v', 'g', 'd', 'gj', 'e', 'zh', 'z', 'dz', 'i', 'j', 'k', 'l', 'lj', 'm', 'n', 'nj', 'o', 'p', 'r', 's', 't', 'kj', 'u', 'f', 'h', 'c', 'ch', 'dzh', 'sh', 'A', 'B', 'V', 'G', 'D', 'Gj', 'E', 'Zh', 'Z', 'Dz', 'I', 'J', 'K', 'L', 'Lj', 'M', 'N', 'Nj', 'O', 'P', 'R', 'S', 'T', 'Kj', 'U', 'F', 'H', 'C', 'Ch', 'Dz', 'Sh']
sentence = 'Чекај малку, што правам?'
new_sentence = ''
for n in sentence:
	if n in lst1:
		broj = lst1.index(n)
		new_sentence = new_sentence + lst2[broj]
	else:
		new_sentence = new_sentence + n
print(new_sentence)
