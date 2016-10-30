# 用map()进行函数式编程。
#写一个使用文件名以及通过除去每行中所有排头和最尾的空白来“清洁“文件。
#在原始文件中读取然后写入一个新的文件，创建一个新的或者覆盖掉已存在的。
#给你的用户一个选择来决定执行哪一个。将你的解转换成使用列表解析。

def strip(strTemp):
    return strTemp.strip()
while True:
    fileName = raw_input("please enter the fileName(q to quit):")
    if fileName.lower() == "q":
        break
    choice = raw_input("n to new file, or c to cover file:")
    if choice.lower() == "n":
        newFileName = raw_input("please enter the new file name:")
        with open(newFileName,"w") as fobj:
            with open(fileName) as fobjold:
                lines = fobjold.readlines()
                for line in map(strip, lines):
                    fobj.write(repr(line))
                    fobj.write("\n")
    else:
        with open(fileName) as fobjold:
            lines = fobjold.readlines()
        with open(fileName,"w") as fobjold:
            for line in map(strip, lines):
                fobjold.write(repr(line))
                fobjold.write("\n")
if __name__ == "__main__":
	filemun()
	
	
#方法2
import os
def cleanfile(filename):
    print 'c: create a new clean file'
    print 'o: overwrite the original file'
    op=raw_input('pls input a choice:')
    if op.lower()=='c':
        newfilename=raw_input('pls input a new file name:')
        with open(filename,'r') as ofile
			with open(newfilename,'w') as dfile
				oflines=map((lambda line:line.strip()),ofile)
        #oflines=[line.strip() for line in ofile]
				for line in oflines:
					dfile.write(line)
					dfile.write(os.linesep)
    elif op.lower()=='o':
        with open(filename,'r') as ofile
        oflines=map((lambda line:line.strip()),ofile)
        #oflines=[line.strip() for line in ofile]
        with open(filename,'w') as dfile
        for line in oflines:
            dfile.write(line)
            dfile.write(os.linesep)
    else:
        print 'input error'

