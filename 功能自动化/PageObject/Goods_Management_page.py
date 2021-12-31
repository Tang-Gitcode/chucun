"""商品管理页"""
import time
from selenium.webdriver.common.by import By
from 功能自动化.PageObject.login_page import LoginPage
from 功能自动化.base.base_page import BasePage


class GoodsManagementpage(BasePage):
    """编辑基本信息"""
    # 点击商品管理
    goods_page = (By.XPATH, "//div[span='商品管理']")

    # 类目
    goods_category = (By.XPATH, "//form//div//span/span")

    # 一级类目
    first_category = (By.XPATH, "/html/body/div[2]/div[1]/div[1]/div[1]/ul/li[15]")
    
    # 二级类目
    second_category = (By.XPATH, "//ul/li[span='户外']")
    
    # 三级类目
    third_category = (By.XPATH, "//ul/li[span='耳机']")
    
    # 分类
    goods_classification = (By.XPATH, "//form//div[2]//span/span")
    
    # 一级分类
    first_classification = (By.XPATH, "/html/body/div[3]/div[1]/div/div[1]/ul/li[1]")
    
    # 二级分类
    second_classification = (By.XPATH, "//ul/li[span='智能设备']")
    
    # 三级分类
    third_classification = (By.XPATH, "//ul/li[span='智能机器人']")
    
    # 商品渠道
    goods_channel = (By.XPATH, "//form//div[3]//span/span")
    goods_source = (By.XPATH, "//ul/li[span='自有']")
    
    # 品牌名称
    brand_name = (By.XPATH, "//input[@placeholder='请输入品牌名称（无品牌请输入无）']")
    
    # 商品名称
    goods_name = (By.XPATH, "//input[@placeholder='请输入商品名称']")
    
    # 商品六九码
    goods_Liujiu_code = (By.XPATH, "//input[@placeholder='请输入商品六九码']")
    
    # 商品单位
    goods_unit = (By.XPATH, "//input[@placeholder='请输入商品单位，如：件、个、台...']")
    
    # 发货地址
    delivery_address = (By.XPATH, "//input[@placeholder='请输入发货地址']")
    
    # 商品图片
    goods_picture = (By.NAME, "file")
    
    # 下一步
    first_next_step = (By.XPATH, "//*[span='下一步']")


    """编辑商品详情"""
    # 详情图
    Details_figure = (By.XPATH, "//*[p='图片上传:']//input")

    # 下一步
    second_next_step = (By.XPATH, "//div[@class='form_button']/following::button[4]")


    """编辑价格库存"""
    # 规格名片
    sku_name_card = (By.XPATH, '//input[@placeholder="请输入规格名片"]')

    # 点击按钮
    first_button = (By.XPATH, '//*[span="添加规格名"]')

    #输入规格值
    specification_values = (By.XPATH, '//input[@placeholder="请输入规格值"]')

    # 点击按钮
    second_button = (By.XPATH, '//*[span="添加规格值"]')

    # 点击展示图片
    open = (By.XPATH, '//*[span="关闭"]')

    # 添加图片
    add_images = (By.XPATH, '//div[@class="img_con"]/following::input[5]')

    # 规格明细
    # 市场价
    market_price = (By.XPATH, '//input[@placeholder="请输入市场价"]')

    # 销售价
    sale_price = (By.XPATH, '//input[@placeholder="请输入销售价"]')

    # 供货价
    supply_price = (By.XPATH, '//input[@placeholder="请输入供货价"]')

    # 结算价
    Settlement_price = (By.XPATH, '//input[@placeholder="请输入结算价"]')

    # 集采价
    Set_CaiJia = (By.XPATH, '//input[@placeholder="请输入集采价"]')

    # 集采结算价
    Jicai_settlement_price = (By.XPATH, '//input[@placeholder="请输入集采结算价"]')
    
    # 库存
    inventory = (By.XPATH, '//input[@placeholder="请输入库存"]')

    # 点击确定
    determine = (By.XPATH, '//button[span="确定"]')

    # 输入已售件数
    quantity_sold = (By.XPATH, '//input[@placeholder="请输入已售件数"]')

    # 输入集采量
    set_CaiLiang = (By.XPATH, '//input[@placeholder="请输入集采量"]')

    #点击有售后
    have_after = (By.XPATH, '//*[@class="el-radio__inner"]')

    # 点击换货
    exchange = (By.XPATH, '//span[@class="el-checkbox__inner"]')

    # 点击退货
    return_goods = (By.XPATH, '//input[@value="退货"]/preceding-sibling::span')

    # 点击上架
    shelves = (By.XPATH, '//button[span="上架"]')



    def Create_Goods(self):
        # 登录
        lp = LoginPage(self.driver)
        lp.login_admin()

        self.driver.get("http://t-admin.helitong.cn/goods/creatGoods")
        time.sleep(2)


        # 点击和输入事件
        """编辑基本信息"""
        # 商品管理
        self.click(GoodsManagementpage.goods_page)

        # 类目
        self.click(GoodsManagementpage.goods_category)
        time.sleep(2)

        # 一级类目
        self.click(GoodsManagementpage.first_category)
        time.sleep(0.2)

        # 二级类目
        self.click(GoodsManagementpage.second_category)
        time.sleep(0.2)

        # 三级类目
        self.click(GoodsManagementpage.third_category)
        time.sleep(0.2)

        # 分类
        self.click(GoodsManagementpage.goods_classification)
        time.sleep(0.5)

        # 一级分类
        self.click(GoodsManagementpage.first_classification)
        time.sleep(0.2)

        # 二级分类
        self.click(GoodsManagementpage.second_classification)
        time.sleep(0.2)

        # 三级分类
        self.click(GoodsManagementpage.third_classification)
        time.sleep(0.2)

        # 商品渠道
        self.click(GoodsManagementpage.goods_channel)
        time.sleep(0.5)
        self.click(GoodsManagementpage.goods_source)
        time.sleep(0.2)

        # 品牌名称
        self.send_keys(GoodsManagementpage.brand_name, "无")
        time.sleep(0.5)        
        
        # 商品名称
        self.send_keys(GoodsManagementpage.goods_name, "测试商品")
        time.sleep(0.5)

        # 商品六九码
        self.send_keys(GoodsManagementpage.goods_Liujiu_code, "1234567890123")
        time.sleep(0.5)
        
        # 商品单位
        self.send_keys(GoodsManagementpage.goods_unit, "个")
        time.sleep(0.5)

        # 发货地址
        self.send_keys(GoodsManagementpage.delivery_address, "上海")
        time.sleep(0.5)

        # 商品图片
        for num in range(6):
            self.send_keys(GoodsManagementpage.goods_picture, f'C:/Users/administered/Desktop/缺陷图片/11.25/' + str(num + 1)+ '.png')
            time.sleep(0.5)
            if num > 6:
                break
        time.sleep(1)

        # 下一步        
        self.click(GoodsManagementpage.first_next_step)
        time.sleep(1)

        """编辑商品详情"""
        # 详情图
        self.send_keys(GoodsManagementpage.Details_figure, f'C:/Users/administered/Desktop/images/多功能酸奶机/详情图.jpg')
        time.sleep(10)

        # 下一步
        self.click(GoodsManagementpage.second_next_step)
        time.sleep(1)


        """编辑价格库存"""
        # 规格名片
        self.send_keys(GoodsManagementpage.sku_name_card, "规格")
        time.sleep(2)

        # 点击按钮
        self.click(GoodsManagementpage.first_button)
        time.sleep(2)

        # 输入规格值
        self.send_keys(GoodsManagementpage.specification_values, "550ml")
        time.sleep(0.5)

        # 点击按钮
        self.click(GoodsManagementpage.second_button)
        time.sleep(2)

        # 打开图片
        self.click(GoodsManagementpage.open)
        time.sleep(1)

        # 添加图片
        self.send_keys(GoodsManagementpage.add_images, f'C:/Users/administered/Desktop/缺陷图片/11.25/1.png')
        time.sleep(3)

        # 市场价
        self.send_keys(GoodsManagementpage.market_price, "1000")
        time.sleep(0.5)

        # 销售价
        self.send_keys(GoodsManagementpage.sale_price, "900")
        time.sleep(0.5)

        # 供货价
        self.send_keys(GoodsManagementpage.supply_price, "800")
        time.sleep(0.5)

        # 结算价
        self.send_keys(GoodsManagementpage.Settlement_price, "700")
        time.sleep(0.5)

        # 集采价
        self.send_keys(GoodsManagementpage.Set_CaiJia, "600")
        time.sleep(0.5)

        # 集采结算价
        self.send_keys(GoodsManagementpage.Jicai_settlement_price, "500")
        time.sleep(0.5)

        # 库存
        self.send_keys(GoodsManagementpage.inventory, "9999")
        time.sleep(0.5)

        # 确定
        self.click(GoodsManagementpage.determine)
        time.sleep(0.5)

        # 已售件数
        self.send_keys(GoodsManagementpage.quantity_sold, "0")
        time.sleep(0.5)

        # 集采量
        self.send_keys(GoodsManagementpage.set_CaiLiang, "10")
        time.sleep(0.5)

        # 有售后
        self.click(GoodsManagementpage.have_after)
        time.sleep(0.5)

        # 换货
        self.click(GoodsManagementpage.exchange)
        time.sleep(0.5)

        # 退货
        self.click(GoodsManagementpage.return_goods)
        time.sleep(0.5)

        # 上架
        self.click(GoodsManagementpage.shelves)
        time.sleep(5)
