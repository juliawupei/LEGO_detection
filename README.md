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

3. 點選**New Project**新增物件辨識專案
![step3](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(104).png)

4. 在Create new project表格中輸入  
  **Name: 專案名稱  
  Description: 相關敘述**
![step4](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(105).png)

5. 在Resource的地方點選**create new**，依照以下內容建立資源
![step5](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(106).png)

6. 新增專案  
  **Project Type:Object Detection  
  Domain: General (compact)  
  Export Capabilities: Basic platforms (Tensorflow, CoreML, ONNX, ...)**  
![step6](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(107).png)

7. 進入專案頁面點選**Add images**上傳訓練用圖片。若要有效地定型模型，可使用有不同視覺效果的影像(攝影角度、光源、背景...) 
![step7_1](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(108).png)
![step7_2](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(109).png)
![step7_3](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(110).png)

8. 在欲辨識的積木上拖拉方塊、標示tag名稱，一張圖可以標示多塊積木  
  (標記名稱一定要使用**英文**，且每一個類別至少都要有**15張照片作為Dataset**，若資料量太少則無法訓練，除此之外，每個類別的資料量要盡量一樣多，以避免機率抽樣產生的誤差。) 
![step8](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(111).png)

9. 標記好所有圖片之後，可點下右上角的綠色按鈕**Train**，AI就會開始訓練模型  
  **Training Types: Fast Training**
![step9_1](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(113).png)
![step9_2](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(114).png)
![step9_3](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(115).png)

10. 訓練完成會出現以下畫面，代表模型訓練完成  
  Precision(精確度): 表示識別的正確分類所得到的分數。  
  *例如，如果模型識別 100 張影像為狗，而實際上有 99 張為狗，則精確度為 99%。*  
  Recall(回收): 表示正確識別實際分類所得到的分數。  
  *例如，如果實際上有 100 張影像為蘋果，而模型識別 80 張為蘋果，則回收為 80%。* 
![step10](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(116).png)

11. 可以點選**Quick Test**測試訊連完的模型，選擇上傳圖片或是輸入圖片連結
![step10](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(117).png)

12. 完成後會標示出辨識結果及相對應信心程度
![step10](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(119).png)

13. 測試完後依然可以繼續新增圖片，繼續訓練模型

14. 完成模型訓練後，點選**publish**輸出模型
![step14_1](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(121).png)
![step14_2](https://github.com/juliawupei/LEGO_detection/blob/main/prtsc/%E8%9E%A2%E5%B9%95%E6%93%B7%E5%8F%96%E7%95%AB%E9%9D%A2%20(122).png)
### Run Model on Raspberry Pi   
**setup Raspberry Pi**  
包含安裝作業系統、設置VNC遠端連線等，"
[點擊](https://github.com/juliawupei/LEGO_detection/blob/main/raspberrypi_setup.pdf)
"看詳細步驟  
  
  
開啟終端機輸入指令**更新Raspbian**  
`
sudo apt-get update
sudo apt-get upgrade
`  
  
  
**安裝Python3**  
`
sudo apt install python3
`    

**測試picamera**  
在未接電源的情況下，插入排線  
注意金屬排線面向SD卡的方向插入  

打開raspberry pi configuration，在"**camera**"選擇"**enable**"
在終端機輸入指令測試相機  
`
raspistill -o image.png
`  
拍設完image.png會存在raspberrypi裡  
  
**安裝opencv**  
[參考本連結](https://qengineering.eu/install-opencv-4.4-on-raspberry-pi-4.html)
，安裝opencv

**安裝customvision、msrest**  
`
pip install azure-cognitiveservices-vision-customvision  
pip install msrest
`  
  
建立新的Python檔案並import所需packages  
`import cv2`    
`from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient`  
`from msrest.authentication import ApiKeyCredentials`  
`from picamera import PiCamera`  
`from time import sleep`  

  
  
