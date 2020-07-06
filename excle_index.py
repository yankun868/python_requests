import xlrd
from openpyxl import load_workbook
from openpyxl import Workbook
import xlwt
import os
import xlrd
from xlutils.copy import copy
class excl:
    #获取Excel表里的所有内容
    def all_excl(self):
        url = r"C:\Users\Administrator\PycharmProjects\untitled\接口\test_case.xlsx"
        data = xlrd.open_workbook(url)
        # print(data.sheet_names()) #输入的时sheet菜单表
        workSheet = data.sheet_by_name('Sheet1') #把名字为Sheet1的表信息复制给workSheet
        text = workSheet.row_values(1)#输入sheet1表下表为1的列所有信息
        li = []
        for i in range(workSheet.nrows):  #打印出所有的行数 i的数值为3
            if i == 0:
                pass
            else:
                row_demo = workSheet.row_values(i)   #将i的值传入进去读取excl的每行的信息
                li.append(row_demo)
        # print(li)
        # text1 = workSheet.col_values(4)#输入sheet1表下表为4的行所有信息
        return li

    # 新建一个Excel中的sheet表，往里面添加数据，但是会清空Excel里的所有内容(不适用)
    def write(self,line,row,data,K=None):
        """写入单个数据"""
        path = r'C:\Users\Administrator\PycharmProjects\untitled\接口\test_case.xlsx'
        rb = xlwt.Workbook()  # 新建一个Excel
        sheet = rb.add_sheet(u'sheet%d'%K, cell_overwrite_ok=True)  # 新建sheet
        sheet.write(line,row,data)  # 向第0行第0列写入foo
        rb.save(path)

    def change(self,lie,hang,data):  #保存原有的数据进行写入数据
        url = r'C:\Users\Administrator\PycharmProjects\untitled\接口\test_case.xlsx'
        work = xlrd.open_workbook(url)
        # print(work)
        # 对数据表格进行复制
        old_content = copy(work)
        # 定位到Sheet1表
        ws = old_content.get_sheet(0)
        ws.write(lie,hang,data)
        # if judge == 200:
        #     # 在sheet1表中写入内容
        #     ws.write(line, row, "success")
        #     # 对修改后的内容进行保存
        # else:
        #     ws.write(line, row, "pass")
        old_content.save(url)


# if __name__ == '__main__':
#     aa = excl()
#     # print(aa.all_excl())
#     # aa.write(1)
#     aa.change()

