espanglish = {}
palabras = input ('Please enter a word in english : and here its traduction in spnish separed by an , betwen each traduction: ')
translation_list = palabras.split(",")

for palabra in translation_list: 
    values_list = translation_list.split(":")
    print (values_list)
    key_english = values_list [0]
    key_spanish = values_list [1]
    translation_list[0]=1

input_to_translate = input ("Please enter a phrase to trasnlate:")
word_list = input_to_translate.split(" ")
word_result = ""

for word in word_list:
  word_result+= espanglish.get{word,word}

