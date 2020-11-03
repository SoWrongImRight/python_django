try:
    f = open('simple.txt', 'r')
    f.write("test write to simple text!")
except:
    print("error, could not find file or read data")
else:
    print("Success")
    f.close()
finally:
    print("I always work")
