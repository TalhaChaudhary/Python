# In this task we will create a list by user and then store that list in a file and later read that file as a list again

a = []
file = open("Lists.txt", 'w')
while True:
	value = input("Enter values to add in list: ")
	if value == 'done':
		break

	a.append(value)
	
for words in a:
    file.write('%s\n' % words)
file.close()


with open('Lists.txt', 'r') as f:
    my_list = [line.rstrip('\n') for line in f]
    print(my_list)