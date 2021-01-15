# LEGO_detection
## Overview
LEGO是聞名全世界的玩具公司，主要生產各式各樣的積木，所有的樂高積木可以完美匹配、可以互相拼砌。越多的積木數量，帶來越多的創意。樂高公司從事生產積木至今已有約88年的歷史，所生產的積木依不同主題、系列區分，例如面向嬰幼兒的得寶系列（duplo）、面向5歲以上少年兒童直至成人的創意百變系列（Creator）、經典創意系列（Classic）等等。可以說是不受年齡、性別、國籍限制的玩具。  
每組樂高內都有數量不一的積木，數量越多的積木拚砌出的成品越大、花費的時間越長、難度越高。目前現存最大的樂高套組「The LEGO Colosseum 樂高羅馬競技場」甚至包含高達9,000多塊積木。
樂高套組內的積木通常會被分裝成數個包裝，越是進階的玩家會面對越複雜多樣的積木，而從茫茫積木海中找出說名書上的某塊積木總是消磨了很多玩家的熱情與耐心，實在是一個十分費心的環節。  
為解決這個問題，本專案透過影像辨識分類說明書上的樂高積木以及桌面上散落的實體積木，標示出所需的某塊積木位置，大幅增加尋找積木的效率，同時不減樂高帶來的遊戲體驗。  
## Hardware
1. Raspberry Pi 3 Model B+
2. Raspberry Pi Camera Moudule V2
3. LEGO積木
## Software
1. Python3
2. OpenCV
3. Microsoft Azure Custom Vision
## Approach
利用Microsoft Azure Custom Vision訓練說明書圖片辨識模型以及積木辨識模型，再透過Python使用模型  
本專案以LEGO #11008 Classic-Bricks and Houses來訓練模型
共使用___張照片訓練模型
## Tutorial
### Training Model with Custom Vision  
1. 建立一個Azure帳號([點擊前往](https://azure.microsoft.com/zh-tw/#))
2. [點擊前往Cutom Vision網站](https://www.customvision.ai/)，並登入帳號
3. 點選New Project新增物件辨識專案  
4. 在Create new project表格中輸入  
  Name: 專案名稱  
  Description: 相關敘述
5. 在Resource的地方點選create new，依照以下內容建立資源
6. 新增專案  
  Project Type:Object Detection  
  Domain: General (compact)  
  Export Capabilities: Basic platforms (Tensorflow, CoreML, ONNX, ...)  
7. 進入專案頁面點選Add images上傳訓練用圖片。若要有效地定型模型，可使用有不同視覺效果的影像(攝影角度、光源、背景...) 
8. 在欲辨識的積木上拖拉方塊、標示tag名稱，一張圖可以標示多塊積木  
  (標記名稱一定要使用**英文**，且每一個類別至少都要有**15張照片作為Dataset**，若資料量太少則無法訓練，除此之外，每個類別的資料量要盡量一樣多，以避免機率抽樣產生的誤差。)  
9. 標記好所有圖片之後，可點下右上角的綠色按鈕Train，AI就會開始訓練模型  
  Training Types: Fast Training  
10. 訓練完成會出現以下畫面，代表模型訓練完成  
  Precision(精確度): 表示識別的正確分類所得到的分數。  
  *例如，如果模型識別 100 張影像為狗，而實際上有 99 張為狗，則精確度為 99%。*  
  Recall(回收): 表示正確識別實際分類所得到的分數。  
  *例如，如果實際上有 100 張影像為蘋果，而模型識別 80 張為蘋果，則回收為 80%。*  
11. 可以點選Quick Test測試訊連完的模型，選擇上傳圖片或是輸入圖片連結
12. 完成後會標示出辨識結果及相對應信心程度
13. 測試完後依然可以繼續新增圖片，繼續訓練模型
### Run Model on Raspberry Pi   
0. setup樹梅派("
[點擊](https://github.com/juliawupei/LEGO_detection/blob/main/raspberrypi_setup.pdf)
"看詳細步驟)  
  包含安裝作業系統、設置VNC遠端連線等步驟
1. 
