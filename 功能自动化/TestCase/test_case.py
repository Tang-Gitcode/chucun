# 应用层
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

# 定义测试类
class TestCase(unittest.TestCase):

    # 定义测试方法
    def test_login(self):

        # 配置全局变量
        global driver

        # 打开浏览器
        driver = webdriver.Chrome()

        # 最大化界面
        driver.maximize_window()

        # 加载地址
        driver.get("http://t-admin.helitong.cn/login")

        """登录"""
        driver.find_element(
            By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13530600569")
        time.sleep(0.2)
        driver.find_element(
            By.XPATH, "//input[@placeholder='请输入登录密码']").send_keys("t123456")
        time.sleep(0.2)
        driver.find_element(By.XPATH, "//button[span='登录']").click()
        time.sleep(1)

        # 关闭浏览器
        driver.close()



    # 定义测试方法

    def test_threeOrder(self):

        # 配置全局变量
        global driver

        # 打开浏览器
        driver = webdriver.Chrome()

        # 最大化界面
        driver.maximize_window()

        # 加载地址
        driver.get("http://t-admin.helitong.cn/login")

        """登录"""
        driver.find_element(
            By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13530600569")
        time.sleep(0.2)
        driver.find_element(
            By.XPATH, "//input[@placeholder='请输入登录密码']").send_keys("t123456")
        time.sleep(0.2)
        driver.find_element(By.XPATH, "//button[span='登录']").click()
        time.sleep(1)

        """订单管理"""
        driver.find_element(By.XPATH, "//div[span='订单管理']").click()
        time.sleep(0.5)

        driver.find_element(By.XPATH, "//*[span='三方订单']").click()
        time.sleep(0.5)

        # 点击日期选择框
        driver.find_element(By.XPATH, "//input[@placeholder='开始日期']").click()
        # 等待时间
        time.sleep(1)

        # 选择三方时间
        driver.find_element(By.XPATH, '//tr[5]/td[7]').click()

        driver.find_element(By.XPATH, '//tr[5]/td[7]').click()

        # 确定时间
        driver.find_element(
            By.XPATH, '//div[@class="el-picker-panel__footer"]/button[2]').click()

        # 搜索
        driver.find_element(
            By.XPATH, '//div[@class="custom-form-btn"]/button').click()
        time.sleep(0.5)

        # 关闭浏览器
        driver.close()

    def test_goods(self):
        """创建商品"""
        # 加载谷歌浏览器
        driver = webdriver.Chrome()
        # 加载地址
        driver.get("http://t-admin.helitong.cn/login")
        # 最大化界面
        driver.maximize_window()
        # 输入登录账号
        driver.find_element(
            By.XPATH, "//input[@placeholder='请输入登录账号']").send_keys("13530600569")
        # 输入登录密码
        driver.find_element(
            By.XPATH, "//input[@placeholder='请输入登录密码']").send_keys("t123456")
        # 点击登录按钮
        driver.find_element(By.XPATH, '//button[span="登录"]').click()
        time.sleep(2)

        """编辑基本信息"""
        # 点击商品管理菜单
        driver.find_element(By.XPATH, "//div[span='商品管理']").click()
        time.sleep(2)
        # 重新加载商品管理页面
        driver.get("http://t-admin.helitong.cn/goods/creatGoods")
        time.sleep(1)
        # driver.find_element(By.XPATH, "/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div/div/ul/li[3]/ul/li[1]").click()
        # time.sleep(5)
        # 商品类目
        driver.find_element(By.XPATH, "//form//div//span/span").click()
        time.sleep(0.5)
        # 一级类目
        driver.find_element(
            By.XPATH, '/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[1]').click()
        # time.sleep(2)
        # 二级类目
        driver.find_element(By.XPATH, "//ul/li[span='户外']").click()
        # time.sleep(0.2)
        # 三级类目
        driver.find_element(By.XPATH, "//ul/li[span='耳机']").click()
        # time.sleep(5)

        # 商品分类
        driver.find_element(By.XPATH, "//form//div[2]//span/span").click()
        time.sleep(2)
        # 一级分类
        driver.find_element(
            By.XPATH, '/html/body/div[3]/div[1]/div/div[1]/ul/li[1]').click()
        # time.sleep(2)
        # 二级分类
        driver.find_element(By.XPATH, "//ul/li[span='智能设备']").click()
        # time.sleep(0.2)
        # 三级分类
        driver.find_element(By.XPATH, "//ul/li[span='智能机器人']").click()
        # time.sleep(5)

        # 商品渠道
        driver.find_element(By.XPATH, "//form//div[3]//span/span").click()
        time.sleep(2)
        # 选择商品来源
        driver.find_element(By.XPATH, "//ul/li[span='自有']").click()
        time.sleep(0.2)

        # 品牌名称
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入品牌名称（无品牌请输入无）"]').send_keys("无")
        time.sleep(0.2)

        # 商品名称
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入商品名称"]').send_keys("测试商品")
        time.sleep(0.5)

        # 商品六九码
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入商品六九码"]').send_keys("1234567890123")
        time.sleep(0.5)

        # 商品单位
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入商品单位，如：件、个、台..."]').send_keys("个")
        time.sleep(0.5)

        # 发货地址
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入发货地址"]').send_keys("上海")
        time.sleep(0.5)

        # 商品图片
        # 上传6张图片，遍历上传操作6次
        for num in range(6):
            driver.find_element(By.NAME, "file")\
                .send_keys(f'C:/Users/administered/Desktop/缺陷图片/11.25/' + str(num + 1)+ '.png')
            time.sleep(0.5)
            if num > 6:
                break
        time.sleep(1)

        # 下一步
        driver.find_element(By.XPATH, '//*[span="下一步"]').click()
        time.sleep(2)

        """编辑商品详情"""
        driver.find_element(By.XPATH, '//*[p="图片上传:"]//input') \
                    .send_keys(f'C:/Users/administered/Desktop/images/多功能酸奶机/详情图.jpg')

        time.sleep(8)

        # 下一步
        driver.find_element(
            By.XPATH, '//div[@class="form_button"]/following::button[4]').click()
        time.sleep(2)

        """编辑价格库存"""
        # 规格名片
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入规格名片"]').send_keys("规格")
        time.sleep(2)
        # 点击按钮
        driver.find_element(By.XPATH, '//*[span="添加规格名"]').click()
        time.sleep(2)

        # 规格值
        # 输入规格值
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入规格值"]').send_keys("550ml")
        time.sleep(2)
        # 点击按钮
        driver.find_element(By.XPATH, '//*[span="添加规格值"]').click()
        time.sleep(1)
        # 点击展示图片
        driver.find_element(By.XPATH, '//*[span="关闭"]').click()
        time.sleep(3)
        # 添加图片
        driver.find_element(By.XPATH, '//div[@class="img_con"]/following::input[5]')\
            .send_keys(f'C:/Users/administered/Desktop/缺陷图片/11.25/1.png')
        time.sleep(5)

        # 规格明细
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入市场价"]').send_keys("1000")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入销售价"]').send_keys("900")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入供货价"]').send_keys("800")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入结算价"]').send_keys("700")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入集采价"]').send_keys("600")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入集采结算价"]').send_keys("500")
        time.sleep(1)
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入库存"]').send_keys("9999")
        time.sleep(1)
        # 点击确定
        driver.find_element(By.XPATH, '//button[span="确定"]').click()
        time.sleep(2)
        # 输入已售件数
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入已售件数"]').send_keys("0")
        time.sleep(1)
        # 输入集采量
        driver.find_element(
            By.XPATH, '//input[@placeholder="请输入集采量"]').send_keys("10")
        time.sleep(1)

        # 其他设置
        # 点击有售后
        driver.find_element(By.XPATH, '//*[@class="el-radio__inner"]').click()
        time.sleep(2)
        # 点击换货
        driver.find_element(
            By.XPATH, '//span[@class="el-checkbox__inner"]').click()
        time.sleep(1)
        # 点击退货
        driver.find_element(
            By.XPATH, '//input[@value="退货"]/preceding-sibling::span').click()
        time.sleep(1)

        # 点击上架
        driver.find_element(By.XPATH, '//button[span="上架"]').click()
        time.sleep(5)


# 执行测试
if __name__ == '__main__':
    print("---------------------TestCase-----------------")
    unittest.main()


