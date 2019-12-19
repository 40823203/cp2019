# 因為 publishconf.py 在 pelicanconf.py 之後, 因此若兩處有相同變數的設定, 將以較後讀入的 publishconf.py 中的設定為主.

# 將所有靜態 html 檔案移到 blog 子目錄
SITEURL = 'https://40823203.github.io/cp2019/blog'
# 此設定用於將資料送到 gh-pages, 因此使用絕對 URL 設定
RELATIVE_URLS = False


# Following items are often useful when publishing

DISQUS_SITENAME = "40823203-cp2019"
DISQUS_DISPLAY_COUNTS = False
#GOOGLE_ANALYTICS = ""