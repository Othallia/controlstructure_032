#Print Fibonacci
def fibonacci(n):
        a, b= 0, 1
        hasil = []
        while a<=n:
             hasil.append(a)
             a, b =b, a + b
        return hasil
n = int(input("masukan nilai bilangan:"))
print("hasilnya adalah", fibonacci(n))