# Import thư viện
from actModule import *
from random import choice

# Khởi tạo trình duyệt
browser = create_webdriver()

# Mở trang web GitHub
print("**Tiến hành mở web git của tôi**")
browser.get("https://github.com/MaiTheHao/SUPPORT_SELENIUM")
print("**Đang delay để nhìn giao diện**")
time.sleep(5)

# MỞ GOOGLE CHỌN NÚT NHẬP VÀ TÌM GIT CỦA TÔI
print("\n\n**Tiến hành mở googleSearch**")
browser.get("https://www.google.com/")
time.sleep(1)

# Tìm thẻ nhập bằng ID thẻ
print("**Tiến tìm thẻ nhập bằng ID thẻ**")
inputLabel = get_element(browser, "APjFqb")
time.sleep(1)

# In ra ID của thẻ input
print(f"**ID của thẻ input: {inputLabel.get_attribute('id')}")

# Nhập kí tự vào thẻ
print("**Nhập kí tự vào thẻ và tự động enter**")
enter_text(inputLabel, "PYTHON là gì")
time.sleep(1)

# In ra thông báo sau khi nhấn Enter
print("**Đã nhấn Enter**")

# DELAY GIAO DIỆN LẦN CUỐI
print("**DELAY GIAO DIỆN LẦN CUỐI**")
time.sleep(10)
