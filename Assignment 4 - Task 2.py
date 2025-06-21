a = input('Enter text to write to the file: ')

file = open('output.txt','w')
write1 = file.write(a + '\n')
print('Data successfully written to output.txt')
file.close()

b = input('Enter additional text to append: ')

file = open('output.txt','a')
write2 = file.write(b)
print('Data successfully appended')
file.close()