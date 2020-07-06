from untitled.接口.excle_index import *
from untitled.接口.get_post import *
from untitled.接口.test_wirte import *
import json
class all_api():
    def jiekou(self):
        excl_data = excl().all_excl()
        # print(excl_data)
        sum = 0
        succeed = 0
        fail = 0
        data_sum = 0
        for i in excl_data:
            title = i[0]
            url = i[1]#请求连接
            requet = i[2]#请求方式
            data = i[3]#传参内容
            header = i[4]#请求头
            Response = i[5]
            # data_sum = i[7]
            data_sum = data_sum + 1
            print("=================正在执行第" + str(data_sum) + "条用例模块为：" + i[0] + "===================")
            if requet == "get":
                try:
                    self.res = g_p().get_way(url,data,header)
                except BaseException as e:
                    txt().txt_add(title + e)
                if Response in self.res:
                    sum = sum + 1
                    succeed = succeed + 1
                    txt().txt_add(title + ":测试成功")
                    excl().change(data_sum, 6, "success")
                else:
                    sum = sum + 1
                    fail = fail + 1
                    txt().txt_add(title + ":测试失败")
                    excl().change(data_sum, 6, "pass")
            if requet == "post":
                try:
                    self.res2 = g_p().post_way(url,data,header)
                except BaseException as e:
                    txt().txt_add(title + e)
                if Response in self.res2:
                    sum = sum + 1
                    succeed = succeed + 1
                    txt().txt_add(title + ":测试成功")
                    print("测试成功")
                    excl().change(data_sum,6,"success")
                else:
                    sum = sum + 1
                    fail = fail + 1
                    txt().txt_add(title + ":测试失败")
                    print("测试失败")
                    excl().change(data_sum, 6, "pass")
            print("=================第" + str(data_sum) + "条用例执行结束==============================")

        txt().txt_add("--------------------------------------------------------------------------")
        succeed = str(succeed)
        fail = str(fail)
        sum = str(sum)
        txt().txt_add("成功执行" + succeed + "条用例")
        txt().txt_add("失败" + fail + "条用例")
        txt().txt_add("总共执行" + sum + "条用例")
        txt().txt_add("==========================================================================")


if __name__ == '__main__':
    all_api().jiekou()