from data_creater.utils import db_utils, str_utils
from data_creater.apis import portal_apis
from time import sleep
from data_creater.controllers.renewal_controller import Renewal


if __name__ == "__main__":


    # 测试用例， 学生在A班班主任未续报；学生在B班主任上拓科   不同科目
    # 当前结果：A班主任没有算拓科   B班主任不算拓科   A是正常生  B是正常生。AB老师都算拓科平分



    uid = 454
    clazz_ids = [1793,1758]

    test = Renewal()
    
    print(test.get_clazz_master_info_field(clazz_id=1793, master_id=10706952, field='service_num,conversion_num,expand_clazz_num'))
    print(test.get_clazz_master_info_field(clazz_id=1758, master_id=10636257, field='service_num,conversion_num,expand_clazz_num'))
    
    for i in range(len(clazz_ids)):
        portal_apis.apply_clazz_student_nice(uid, clazz_id=clazz_ids[i])
        sleep(1)
        # 先查询info表确定服务人数
        print("报班成功!")

    sleep(1)
    # 验证数据是否正确
    # info表分母不变算惩罚，分子不变
    print(test.get_clazz_master_info_field(clazz_id=1793, master_id=10706952, field='service_num,conversion_num,expand_clazz_num'))
    print(test.get_clazz_master_info_field(clazz_id=1758, master_id=10636257, field='service_num,conversion_num,expand_clazz_num'))

    portal_apis.apply_clazz_student_nice(uid, clazz_id=1997)
    sleep(1)
    print(test.get_clazz_master_info_field(clazz_id=1793, master_id=10706952, field='service_num,conversion_num,expand_clazz_num'))
    print(test.get_clazz_master_info_field(clazz_id=1758, master_id=10636257, field='service_num,conversion_num,expand_clazz_num'))

