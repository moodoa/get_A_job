# get_A_job
用程式自動在 104 上投遞工作

![alt text](https://i.makeagif.com/media/6-14-2021/XF3YQ2.gif)

## __init__
* keyword : 想找的工作關鍵字 e.g., python。 
* area : 想找的工作範圍，以 list 型態輸入e.g.,[6001001000, 6001006000]。(地點編號以 104 上為主)
* page : 想讓程式幫你投幾頁工作。
* username : 104 上的帳號。 
* password : 104 上的密碼。 
* intro_idx : 自我推薦信，輸入 0 為預設，1 ~ 3 為自訂推薦信 1 ~ 3。

## _get_all_submit_url
* 收集所有符合條件之工作，回傳值為工作投遞頁面之連結。

## submit_job
* 使用 selenium 投遞工作。
* 若有今日已投遞之工作將忽略。

## Requirements
python 3

## Usage
* 需先下載相對應 chromedriver: https://chromedriver.chromium.org/downloads
```
if __name__ == "__main__":
    test = GETAJOB("工作關鍵字", [工作範圍], 頁數, "帳號", "密碼", 推薦信編號)
    all_submit_url = test._get_all_submit_url()
    test.submit_job(all_submit_url)

```
## Installation
`pip install -r requriements.txt`。