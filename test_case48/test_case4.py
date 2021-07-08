from data_creater.utils import db_utils, str_utils
from data_creater.apis import portal_apis
from time import sleep
from data_creater.controllers.renewal_controller import Renewal


if __name__ == "__main__":
    # 测试用例， 报名构成续报的课程 分子加一；并且退构成续报的课程，分子减一

    
    test = Renewal()
    # 先查询info表确定服务人数
    service_num,conversion_num = test.get_clazz_master_info_field(clazz_id=1793, master_id=10706952,field='service_num,conversion_num')

    uid = 450
    # # 报春季班、四年级数学
    portal_apis.apply_clazz_student_nice(uid, clazz_id=1793) 
    sleep(1)
    # 验证数据是否正确
    # info表分母加一，分子不变
    new_service_num = test.get_clazz_master_info_field(clazz_id=1793, master_id=10706952, field='service_num')[0]
    assert new_service_num-service_num == 1, "报班后分母没有加一" 
    print("报班功能测试通过!")
    
    # TODO: 可以使用装饰器封装查询数据
    portal_apis.apply_clazz_student_nice(uid, clazz_id=1987)
    sleep(20)
    new_conversion_num = test.get_clazz_master_info_field(clazz_id=1793, master_id=10706952, field='conversion_num')[0]
    # 验证数据是否正确
    # info表分子加一
    assert new_conversion_num-conversion_num == 1, "续报后分子没有加一" 
    print("续报功能测试通过!")

    clazz_id = 1987
    order_id = str_utils.int2list(test.get_order_id_from_payment(uid,clazz_id))
    test.quit_clazz(order_id)
    sleep(2)
    # 验证数据是否正确
    # info表分母不变算惩罚，分子不变
    conversion_num = test.get_clazz_master_info_field(clazz_id=1793, master_id=10706952, field='conversion_num')[0]
    assert new_conversion_num-conversion_num == 1, "退课后分子没有减一" 
    print("退续报课功能测试通过!")

