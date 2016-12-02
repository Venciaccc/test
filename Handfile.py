#_*_ coding:utf-8 _*_
#功能：合并文件夹下同种个数文件，并lookup出需要的行，输出到指定文件
#操作：cmd 跳转到需要处理的文件夹下
#输入:python Handfile.py 参数1 参数2 参数3
#参数解释：参数1为参考文件名，参数2指定合并的文件格式，参数3指定输出文件
import glob,re,sys,os
def handle(paramter,TPF,newfile):
  result = ''
  info = 'can not find'
  list='*.'+TPF
  f1=file(paramter)
  lines1=f1.readlines()
  f1.close()
  for flag in lines1:
    pat = re.compile(flag)
    for filename in glob.glob(list):
     if filename!=paramter:
      f2 = file(filename) 
      lines2 = f2.readlines()
      f2.close()
      for line in lines2:
        match = pat.search(line)
        if match:
          result+='%s'%line
          info = 'OK!'
  if not os.path.isdir('result'):
    os.makedirs('result')
  out=open(r'result/%s'%newfile,'w')
  out.write(''.join(result))
  out.close()
  print info 
handle(sys.argv[1],sys.argv[2],sys.argv[3])
