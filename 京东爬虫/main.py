from selenium import webdriver
import time
import random
import sys


def scroll_to_bottom(driver):
    # 执行这段代码，会获取到当前窗口总高度
    js = "return action=document.body.scrollHeight"
    # 初始化现在滚动条所在高度为0
    height = 0
    # 当前窗口总高度
    new_height = driver.execute_script(js)

    while height < new_height:
        # 将滚动条调整至页面底部
        for i in range(height, new_height, 100):
            driver.execute_script('window.scrollTo(0, {})'.format(i))
            time.sleep(0.5)
        height = new_height
        time.sleep(2)
        new_height = driver.execute_script(js)


if __name__ == '__main__':
    url = 'https://mall.jd.com/view_search-174765-0-5-1-24-1.html'
    options = webdriver.ChromeOptions()
    port = 8080  # sys.argv[1]
    prefs = {
        'profile.default_content_setting_values': {
            'images': 2,
        }
    }
    options.add_experimental_option('prefs', prefs)
    options.add_argument('--proxy-server=http://localhost:8088')
    # options.add_experimental_option("mobileEmulation", {'deviceName': 'iPhone 6'})
    options.add_argument("--test-type")
    options.add_argument("--ignore-certificate-errors")
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1400, 900)
    browser.get(url)
    time.sleep(random.randint(5, 6))
    # 点击下一页
    for i in range(1000):
        try:
            print(i)
            # 此处有问题，需要慢慢滑动，加载数据才完整
            # scroll_to_bottom(browser)
            browser.execute_script('window.scrollBy(0,500)')
            time.sleep(3)

            browser.execute_script('window.scrollBy(0,500)')
            time.sleep(3)

            browser.execute_script('window.scrollBy(0,500)')
            time.sleep(3)

            browser.find_element_by_xpath("//a[text()='下一页']").click()
        except Exception as e:
            print(e)
