# used_car_sale_FULI
台灣福利汽車追蹤銷售列表

## 背景
寫這篇程式碼的時候2017年底，正好在找尋二手的Benz，於是找上了在台灣也算還有名氣的`福利汽車網站`(https://www.flcar.com.tw/cars?plat=pc)
，也去現場看過車，了解到這家的汽車轉手動率蠻高的，
歸納了幾個原因如下，隨即開始動手撰寫需要的功能．
1. 也許在當下買不到某一型號的車款，但也許沒過幾天就出現
2. 某一車款再過不久就會過保固，價格會有較大幅度的下修
3. 了解某一車款的大約價格

## 使用的程式環境
* macbook air 13 2011mid 
* Python 2.7
* Python Library
  1. urllib2
  2. Selenium
  3. beautifulsoup
  
## 程式擷取流程
1. 使用selenium 去對網站的選單做操作
2. beautifulsoup 將網站資料擷取後，以正則表達式將需要benz車款的位置編號記下
3. 建立pandas 表格，以迴圈方式將前面編號帶入網頁擷取後記錄，並輸出csv 檔案格式

## note
畢竟只是以定期搜集資訊為目的，又是直接撈取人家公司網站的資料，因此有設定不要短時間內太頻繁的擷取資料，時間會久一點
* 最後....還是沒有買
