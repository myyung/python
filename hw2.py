Python 3.10.10 (tags/v3.10.10:aad5f6a, Feb  7 2023, 17:20:36) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def get_integer(prompt):
...   a=int(input(prompt))
...   return a
... 
... def exchange(c):
...   오백원=c//500
...   c%=500
...   백원=c//100
...   c%=100
...   오십원=c//50
...   c%=50
...   십원=c//10
...   print('500원 동전의 개수:',오백원)
...   print('100원 동전의 개수:',백원)
...   print('50원 동전의 개수:',오십원)
...   print('10원 동전의 개수:',십원)
... 
... a=get_integer('동전으로 교환하고자 하는 금액은?')
