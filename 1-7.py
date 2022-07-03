# with open("test.txt",'w',encoding = 'utf-8') as f:
#  f.write("Quantrimang\n")
#  f.write("Kiến thức - Kinh nghiệm - Hỏi đáp\n\n")
#  f.write("Quantrimang.com\n")
f = open("test.txt",'r',encoding = 'utf-8')
a = f.read(12) # đọc 12 kí tự đầu tiên
print('Nội dung 11 kí tự đầu là:\n', (a))
b = f.read(35) # đọc 35 kí tự tiếp theo
print('Nội dung 35 kí tự tiếp theo là:\n', (b))
c = f.read() # đọc phần còn lại
print('Nội dung phần còn lại là:\n', (c))