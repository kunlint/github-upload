import numpy as np
total_file = 128  # total file size (MB)
floppy_capacity = 1.44 # capacity of 1 floppy disk (MB)
number_floppy = 120 # number of floppy disks
# take a list of filesize as argument and return a dict 
# where the key is the index of the floppy disk and the value
# is a set of the indices of the files
def file_assign(files):
	file_assignment = {} # create an empty dict
	file_index_map = {} #  a dict that maps filesize to its index
	for j in range(len(files)):
		file_index_map[files[j]] = j # assume we have no duplicate file size
	files = np.sort(files) # sort the filesize numerically (takes n log n time)
	i = 0 # index of the current floppy disk
	capacity = floppy_capacity # capacity of the current floppy disk (in MB)
	current_first = 0
	current_last = len(files)-1 
	while current_first <= current_last:
		file_assignment[i] = set() #create a new set for the ith floppy disk
		file_assignment[i].add(file_index_map[files[current_last]]) # place the current largest file
		capacity -= files[current_last] #update the capacity
		# keep adding current smallest file to the current disk until reach full capacity
		while files[current_first] < capacity:
			file_assignment[i].add(file_index_map[files[current_first]])
			capacity -= files[current_first]
			current_first += 1
		current_last -= 1  # move to the next biggest file
		i += 1  # advance to the next floppy disk
		capacity = floppy_capacity   # update the capacity
	return 	file_assignment 
# main testing 
# create random numbers (smaller than 1.44) that sum up to 128
test_files = [] # empty list of file sizes
current_sum = 0
while current_sum < total_file:
	a = np.random.random()*floppy_capacity # random number between 0 and 1.44
	current_sum += a
	test_files.append(a)
last = test_files.pop() # remove the last item because the current sum is larger than 128
test_files.append(total_file - (current_sum-last)) # append an additional element to add up to 128
test_assign = file_assign(test_files) # make assignment for test_files
print(test_assign)
print(len(test_files))
current_num = 0
# check that every floppy disk is not overloaded
for i in test_assign:
	current_sum = 0 # sum of file sizes in the ith floppy disk
	current_num += len(test_assign[i])
	for k in test_assign[i]:
		current_sum += test_files[k]
	print(current_sum) # print the total file size in the ith disk
	assert(current_sum < floppy_capacity)		
assert(current_num == len(test_files)) # check the number of files match
