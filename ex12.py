
print "open the file again"
file_again = raw_input(">")
file_name = open(file_again, 'w')
file_name.truncate()
