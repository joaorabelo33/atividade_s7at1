caractere=input()
vogal='aeiouAEIOU'
consoantes='bcdfghjklmnpqrstvxywzBCDFGHJKLMNPQRSTVXYWZ'
número='0123456789'

if caractere in vogal:
    print('vogal')
elif caractere in consoantes:
    print('consoante')
elif caractere in número:
    print('número')
else:
    print('símbolo')
   