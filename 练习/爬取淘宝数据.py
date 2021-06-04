import re
import pymysql
import random
from time import sleep
from lxml import etree
from urllib.request import urlretrieve
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TaobaoSpider(object):
    ask = []
    # driver_path = r'D:\Python\Python38\Scripts\chromedriver.exe'
    def __init__(self):
        self.url = 'https://www.taobao.com/'
        self.options = webdriver.ChromeOptions()
        self.options.add_argument("--proxy-server=http://171.35.167.32:9999")   ##设置代理IP
        # self.driver = webdriver.Chrome(chrome_options=self.options)
        # self.driver = webdriver.Chrome(executable_path=TaobaoSpider.driver_path)
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()  ##使浏览器窗口最大化
        self.baili_url = 'https://ebelle.tmall.com/search.htm?spm=a1z10.1-b-s.w17839663-14900112884.9.44ac5a3dvUsdOH'
        self.own_baili = 'https://ebelle.tmall.com/search.htm?spm=a1z10.3-b-s.w17839663-14900112884.9.346e3897Pm6zl7'




    def run(self):

        wait = WebDriverWait(driver=self.driver,timeout= 20)
        self.driver.get(self.url)

        wait.until(EC.presence_of_all_elements_located((By.XPATH,'//div[@class="site-nav-menu-hd"]')))##等待所有元素加载出来
        self.driver.find_element_by_xpath('//a[@class="h"]').click()   ##点击登入，让后自己扫描登入
        sleep(10)
        print('已经登入啦')
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//a[@class="site-nav-login-info-nick "]')))##等待所有元素加载出来
        self.driver.find_element_by_xpath('//*[@class="search-triggers search-tab-header J_SearchTabBox"]').click() ##点击店铺
        print('已经点了店铺')
        sleep(0.5)
        self.driver.find_element_by_xpath('//*[@id="q"]').send_keys('百丽旗舰店') ##输入百丽旗舰店
        print('输入了店铺')
        sleep(0.5)
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="J_TSearchForm"]/div[1]/button')))##等待页面加载完
        self.driver.find_element_by_xpath('//*[@id="J_TSearchForm"]/div[1]/button').click()   ##点击搜索
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="list-container"]')))  ##等待页面加载完


        self.driver.find_element_by_xpath('//*[@id="j-picture-0"]/li[1]/ul/li[1]/a/img').click() ##点击百丽店,然后会弹出第二个框
        self.driver.switch_to.window(self.driver.window_handles[1])  ###跳转到第二个界面
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//*[@class="jdb abs a9Odl-P7uf"]')))##等待页面加载完
        self.driver.find_element_by_xpath('//*[@class="jdb abs a9Odl-P7uf"]').click()  ##点击所有宝贝，然后会跳出第三个窗口
        self.driver.switch_to.window(self.driver.window_handles[2])  ###跳转到第三个界面
        sleep(0.5)
        source = self.driver.page_source
        link = etree.HTML(source)
        sleep(0.5)
        htmls = link.xpath('//div[@class="item4line1"]//a[@class="J_TGoldData"]/@href')   #获取连接
        sleep(0.5)
        for html in htmls:          ##详情页面
            TaobaoSpider.ask.append(html)
            self.parse_url(html)
            TaobaoSpider.ask.clear()
            sleep(random.randint(1,4))

    def parse_url(self,url):
        wait =WebDriverWait(driver=self.driver,timeout=1000)
        self.driver.execute_script("window.open('%s')" % url)  #第4个窗口打开
        self.driver.switch_to.window(self.driver.window_handles[3])  ###跳转到第4个界面
        wait.until(EC.presence_of_all_elements_located((By.XPATH,'//*[@id="detail"]')))  ##等待
        source = self.driver.page_source
        self.jiexi_url(source)
        self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[2])  ##跳转到第三个界面

    def jiexi_url(self,source):
        html = etree.HTML(source)
        self.img_download(html)
        name = html.xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[1]/h1/text()')#产品名
        price = html.xpath('//*[@id="J_PromoPrice"]/dd/div/span/text()') #价格
        sale = html.xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/ul/li[1]/div/span[2]/text()')  #月销
        shaky = html.xpath('//*[@id="J_DetailMeta"]/div[1]/div[1]/div/div[2]/dl[3]/div[1]/dd/text()')  ##活动
        assess = html.xpath('//*[@id="J_ItemRates"]/div/span[2]/text()')  ##评价
        content = {
            'url' : TaobaoSpider.ask,
            'name': name,
            'price': price,
            'sale' : sale,
            'shaky': shaky,
            'assess': assess
        }

        print(content)
        sleep(2)
    def img_download(self,url):
        img_url = url.xpath('//div[@class="tb-booth"]//img')  ##img标签
        aa = img_url[0].attrib  ##获取img标签所有属性，这是一个字典的形式
        name = aa['alt']  # 获取标签中alt的值名字
        url = aa['src']  # 获取标签中alt的值网页
        filename = name + '.jpg'
        urlretrieve(url, filename)

if __name__ == '__main__':
    spider = TaobaoSpider()
    spider.run()