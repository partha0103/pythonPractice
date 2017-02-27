from sys import argv
script,input_file = argv

def print_all(f):
    print f.read();

def rewind(f):
    f.seek(0)

def print_a_line(line_count,f):
    print line_count,f.readline()

current_file = open(input_file)

print "First thing \n"
print_all(current_file)
print "second thing \n"
rewind(current_file)
print "Third thing\n"
print_a_line(4,current_file)
