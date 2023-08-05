import tkinter
import tkinter.font
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

import time

tk = tkinter.Tk()
tk.geometry("350x200")
font = tkinter.font.Font(
    size = 20
)

def test_button():
    driver = webdriver.Chrome()

    try:
        driver.get('https://www.pref.saitama.lg.jp/a0212/densinyusatsu/index.html')
    
        # 要素が表示されるまで最大10秒待機
        wait = WebDriverWait(driver, 100)

        # 現在のウィンドウハンドルを保存
        current_window = driver.current_window_handle
   
        element = driver.find_element(By.LINK_TEXT, "入札情報公開システム")

        element.click()

        # 新しいウィンドウハンドルを取得
        new_window = driver.window_handles[-1]
        # 新しいタブに切り替え
        driver.switch_to.window(new_window)

        time.sleep(1)
        driver.switch_to.frame(2)

        time.sleep(1) 
        #情報公開システムの区分を選択
        dropdown=driver.find_element_by_id("chotatsuType")
        select = Select(dropdown)
        select.select_by_value('00')

        #発注情報の検索リンクを押すボタン。
        kensaku = driver.find_element(By.LINK_TEXT, "発注情報の検索")
        kensaku.click()

        #ページの切り替え
        driver.switch_to.window(driver.window_handles[-1])
        driver.switch_to.frame(2)

        time.sleep(1)
    
        ropdown=driver.find_element_by_name("supplytype")
        select = Select(ropdown)
        select.select_by_value("00")
        time.sleep(1)
        kensaku = driver.find_element_by_css_selector("input.CystageBtn")  # CSSセレクタを使用して要素を取得
        kensaku.click()

        #電子入札ボタンが表示されたか検索する
        densinyuusatu = driver.find_element_by_tag_name("img")
        print("1")

        time.sleep(1)
    
        driver.quit()
    except:
        driver.quit()
        s ="エラー"
        textbox.delete("1.0",tkinter.END)
        textbox.insert("1.0",s)

    else:    
        s = "成功"
        textbox.delete("1.0",tkinter.END)
        textbox.insert("1.0",s)
    
    return

def test2_button (taitlename,yuserid,passward,a):
    driver = webdriver.Chrome()

        # 以降、WebDriverを使用した処理を記述
    try:
        # Webページの読み込み
        driver.get('https://www.pref.saitama.lg.jp/a0212/densinyusatsu/index.html')

        # 要素が表示されるまで最大10秒待機
        wait = WebDriverWait(driver, 100)

        # 現在のウィンドウハンドルを保存
        current_window = driver.current_window_handle

        element = driver.find_element(By.LINK_TEXT, "競争入札参加資格申請受付システム")
        element.click()

        # 新しいウィンドウハンドルを取得
        new_window = driver.window_handles[-1]
        # 新しいタブに切り替え
        driver.switch_to.window(new_window)

        time.sleep(1)
        element = driver.find_element(By.LINK_TEXT, taitlename)
        element.click()

        time.sleep(1) 

        # 新しいウィンドウハンドルを取得
        new_window = driver.window_handles[-1]
        # ログインのタブに切り替え
        driver.switch_to.window(new_window)

        #ログインをクリック
        rogin=driver.find_element(By.LINK_TEXT,"ログイン")
        rogin.click()

        new_window = driver.window_handles[-1]
        # 新しいタブに切り替え
        driver.switch_to.window(new_window)

        selectyear=driver.find_element_by_name("modeSub")
        selectyear.click()
        #ユーザーIDの入力
        ID=driver.find_element_by_name("userid")
        ID.send_keys(yuserid)
        #パスワードの入力
        Password=driver.find_element_by_name("passwd")
        Password.send_keys(passward)
        #送信ボタンをクリック
        sousinn=driver.find_element_by_class_name("CystageBtn")
        sousinn.click()

        #わざとエラーを起こしています
        element = driver.find_element(By.LINK_TEXT, "競争入札参加資格申請受付システム")

        time.sleep(3)
    except:
        if a==2 :
            driver.quit()
            t ="エラー"
            textbox2.delete("1.0",tkinter.END)
            textbox2.insert("1.0",t)
        else:
            driver.quit()
            j = "エラー"
            textbox3.delete("1.0",tkinter.END)
            textbox3.insert("1.0",j)
    else:
        if a==2 :
            driver.quit()
            t ="成功"
            textbox2.delete("1.0",tkinter.END)
            textbox2.insert("1.0",t)
        else:
            driver.quit()
            j = "成功"
            textbox3.delete("1.0",tkinter.END)
            textbox3.insert("1.0",j)
             
    return

def all_button():
        test_button()
        test2_button("工事等",567,"4564",2)
        test2_button("物品等",223,"d",3)

        return

tk.title("動作確認")

frame = tkinter.Frame()
testbutton=tkinter.Button(tk,text="情報公開",command=test_button)
testbutton.place(y=30)

testbutton2=tkinter.Button(tk,text="受付工事",command=lambda : test2_button("工事等",567,"4564",2))
testbutton2.place(y=60)

testbutton3=tkinter.Button(tk,text="受付物品",command=lambda : test2_button("物品等",223,"d",3))
testbutton3.place(y=90)

allbutton=tkinter.Button(tk,text="オールチェック",command=lambda :all_button())
allbutton.place(x=110,y=120)

#seikou = test_button
textbox = tkinter.Text(width=30,height=1,)
textbox.place(x=85,y=35)

textbox2 = tkinter.Text(width=30,height=1)
textbox2.place(x=85,y=65)

textbox3 = tkinter.Text(width=30,height=1)
textbox3.place(x=85,y=95)


tk.mainloop()