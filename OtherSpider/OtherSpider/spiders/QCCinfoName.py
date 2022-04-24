import scrapy
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
f=open("../resource/QccinfoName.txt")

title_list=eval(f.read())

class QccinfonameSpider(scrapy.Spider):
    name = 'QCCinfoName'
    # allowed_domains = ['xxx.com']
    start_urls=title_list

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(
                url=url,
                headers={
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                    'accept-encoding': 'gzip, deflate, br',
                    'accept-language': 'zh-CN,zh;q=0.9',
                    'cache-control': 'no-cache',
                    'cookie': 'qcc_did=33213b33-97cf-47f6-bfb3-4ada13d561f0; UM_distinctid=17f43dbebb09a5-00ca89c96828dc-a3e3164-1fa400-17f43dbebb110dc; QCCSESSID=3bac48cc49954a47bcedb6f3e3; acw_tc=3ad8379c16469780258193824e04803c88b1693eec2763e95c077267e2; CNZZDATA1254842228=787216255-1646101019-%7C1646978028',
                    'pragma': 'no-cache',
                    'referer': 'https://www.qcc.com/web/search/person?key=%E4%B8%AD%E5%9B%BD',
                    'sec-ch-ua': '"Not A;Brand";v="99", "Chromium";v="99", "Google Chrome";v="99"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'document',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-user': '?1',
                    'upgrade-insecure-requests': '1',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
                    'img': ''
                },
                callback=self.parse
            )

    def __init__(self):
        super(QccinfonameSpider, self).__init__()
        chrome_options = Options()
        chrome_options.add_argument('--ignore-certificate-errors')
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        # 添加特殊配置
        options = webdriver.ChromeOptions()
        # 设置默认编码为 utf-8，也就是中文
        options.add_argument('lang=zh_CN.UTF-8')
        # 模拟 android QQ浏览器
        options.add_argument(
            'user-agent="MQQBrowser/26 Mozilla/5.0 (Linux; U; Android 2.3.7; zh-cn; MB200 Build/GRJ22; CyanogenMod-7) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1"')
        # 禁止硬件加速
        options.add_argument('--disable-gpu')
        # 取消沙盒模式
        options.add_argument('--no-sandbox')
        # 禁止弹窗广告
        options.add_argument('--disable-popup-blocking')
        # 最大界面
        options.add_argument('--window-size=1920,1080')
        # 去掉反扒标志
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        # 此方法针对V78版本及以上有效，同时可以解决部分网站白屏的问题。
        options.add_experimental_option('useAutomationExtension', False)
        # # 大量渲染时候写入/tmp而非/dev/shm
        options.add_argument("-–disable-dev-shm-usage")
        desired_capabilities = DesiredCapabilities.CHROME
        desired_capabilities["pageLoadStrategy"] = "none"
        # 忽略证书错误 （实操没卵用）
        options.add_argument('--ignore-certificate-errors')
        # 真实浏览器
        self.bro = webdriver.Chrome(executable_path='../../../driver/chromedriver.exe',
                                    chrome_options=chrome_options)
        self.bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                                       Object.defineProperty(navigator, 'webdriver', {
                                         get: () => undefined
                                       })
                                     """
        })



    def parse(self, response,**kwargs):
        item={}
        item["name"] = response.css("div.title div span h1.copy-value::text").get()
        item['status'] =response.css("div.title div span span::text").get()
        print(item)

        yield item