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
print("**Nhập kí tự vào thẻ**")
enter_text(inputLabel, "PYTHON là gì")
time.sleep(1)

# In ra nội dung của thẻ input
print(f"**Nội dung của thẻ input: {inputLabel.get_attribute('value')}")

# Nhấn Enter
print("**Keys.RETURN <=> Nhấn Enter**")
enter_text(inputLabel, Keys.RETURN)
time.sleep(1)

# In ra thông báo sau khi nhấn Enter
print("**Đã nhấn Enter**")

# Tìm các trang web ở kết quả và chọn ngẫu nhiên 1
print("\n**Tiến hành tìm các trang web ở kết quả và chọn ngẫu nhiên 1**")
list_Web = get_element(browser, "ULSxyf", "CLASS_NAME", mode_multi=True)[:4]
print(f"**Số lượng kết quả tìm kiếm: {len(list_Web)}")
time.sleep(1)

# Chọn ngẫu nhiên một trang web
selected_web = choice(list_Web)

# In ra URL của trang web được chọn
print(f"**URL trang web được chọn: {get_element(selected_web, "a", "TAG_NAME").get_attribute('href')}")
time.sleep(1)

# Click vào trang web được chọn
click(selected_web)
time.sleep(1)

# DELAY GIAO DIỆN LẦN CUỐI
print("**DELAY GIAO DIỆN LẦN CUỐI**")
time.sleep(10)
