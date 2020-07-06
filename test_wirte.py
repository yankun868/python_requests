
class txt():
    #写入日志，追加到txt文件内容后面
    def txt_add(self,i):
        with open(r"C:\Users\Administrator\PycharmProjects\untitled\接口\log.txt", "a",encoding="utf8") as f:
            f.write(str(i) + "\n")
    #读取日志，把txt文件里面的内容全部读取出来
    def txt_wirte(self):
        f = open(r"C:\Users\Administrator\PycharmProjects\untitled\接口\log.txt",'r')
        reads = f.read()
        print(reads)

