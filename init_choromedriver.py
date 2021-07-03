import os
import logging
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import Chrome, ChromeOptions

'''
# Chromeを起動する関数
'''
def set_driver(headless_flg):
    # Chromeドライバーの読み込み
    options = ChromeOptions()

    # ヘッドレスモード（画面非表示モード）をの設定
    if headless_flg == True:
        options.add_argument('--headless')

    # 起動オプションの設定
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36')
    # options.add_argument('log-level=3')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--incognito')          # シークレットモードの設定を付与

    # ChromeのWebDriverオブジェクトを作成する。
    return Chrome(ChromeDriverManager().install(), options=options)

def main():
    # driverの設定
    if os.name == 'nt':  # Windows
        logging.debug("osはwindowsです")
    elif os.name == 'posix':
        logging.debug("osはmacです")
    driver = set_driver(False)
    logging.info("ドライバーを立ち上げます")
    # ページにアクセス
    driver.get("https://www.yahoo.co.jp/")

if __name__ == "__main__":
    main()