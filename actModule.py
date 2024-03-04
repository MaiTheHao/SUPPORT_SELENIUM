from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from os import system as ost
from selenium.webdriver.common.keys import Keys
import time, os, sys
import random as ra
from json import load as jload

remove_space = lambda x: '.'.join(x.split(' ')) # Xóa khoảng trống thay thế bằng '.'
format_lower = lambda x: x.strip().lower()
format_upper = lambda x: x.strip().upper()
clearT = lambda: ost('clear') # Xóa hiển thị ở bảng điều khiển
showLog = "terminal" # terminal; file; hidden;

with open(r"Running/runningSTATUS.txt", "w", encoding="utf-8") as f:
    f.write("<<<RUNNING PROCESS>>>\n")

def actModule_Log(value:bool):
    global showLog
    showLog = value

def log(text):
    if showLog == "hidden":
        pass
    elif showLog == "terminal":
        print(text)
    
    elif showLog == "file":
        with open(r"Running/runningSTATUS.txt", "a", encoding="utf-8") as f:
            f.write(text + "\n")

def load_json_file(path, encoding = 'utf-8'):
    """
    Lấy phần tử dựa trên kiểu và tên.

    Args:
        path: đường dẫn tới tệp Json.
        encoding: mã hóa (mặc định là 'utf-8').

    Returns:
        Đối tượng này có thể là một mảng, một đối tượng, một chuỗi, một số, hoặc một giá trị Boolean.
    """
    with open(path, 'r', encoding = encoding) as file:
        return jload(file)

def create_webdriver(browser_name="chrome", user_data_dir=None):
    browser_name = browser_name.lower()
    """
    Tạo trình duyệt web dựa trên trình duyệt được chỉ định và tùy chọn đặt thư mục dữ liệu người dùng.

    Tham số:
        browser_name (str, tùy chọn): Tên trình duyệt web cần sử dụng. Mặc định là "chrome".
        user_data_dir (str, tùy chọn): Đường dẫn đến thư mục dữ liệu người dùng cho trình duyệt. Mặc định là None.

    Trả về:
        WebDriver: Thể hiện trình duyệt web đã tạo.

    Lỗi:
        ValueError: Nếu tên trình duyệt được cung cấp không được hỗ trợ.
    """

    supported_browsers = {
        "edge": webdriver.Edge,
        "chrome": webdriver.Chrome,
        "firefox": webdriver.Firefox,
        # Thêm các trình duyệt được hỗ trợ khác nếu cần
    }
    
    browser_option = {
        "edge": webdriver.EdgeOptions(),
        "chrome": webdriver.ChromeOptions(),
        "firefox": webdriver.FirefoxOptions(),
        # Thêm các trình duyệt được hỗ trợ khác nếu cần
    }

    if browser_name not in supported_browsers:
        raise ValueError(f"Unsupported browser name: {browser_name}")

    options = browser_option[browser_name]

    if user_data_dir:
        options.add_argument(f"--user-data-dir={user_data_dir}")

    return supported_browsers[browser_name](options)

def get_element(driver, name, search_type="ID", delay=5, err=None, mode_multi=False):
    """
    Lấy phần tử dựa trên kiểu và tên.

    Args:
        drive: Đối tượng WebDriver.
        search_type (str): Kiểu tìm kiếm (mặc định là "ID").
        name: Tên phần tử cần tìm.
        delay (int): Thời gian chờ tối đa (mặc định là 5 giây).
        mode_multi (bool): True nếu muốn tìm nhiều phần tử.

    Returns:
        WebElement hoặc List[WebElement]: Phần tử(s) tìm thấy hoặc None nếu không tìm thấy.
    """
    try:
        name = remove_space(name) if search_type == "CLASS_NAME" else name
        valid_types = {"search_type": ["ID", "CLASS_NAME", "XPATH", "TAG_NAME"], "multi": [True, False]}
    
        if search_type not in valid_types["search_type"]:
            raise ValueError("Kiểu tìm kiếm không hợp lệ. Hãy sử dụng 'ID', 'CLASS_NAME', 'TAG_NAME' hoặc 'XPATH'.")
        
        elif mode_multi not in valid_types["multi"]:
            raise ValueError("Mode Multi Get Element chỉ có thể là True hoặc False")
        
        locator = eval(f"By.{search_type}")
        element_func = EC.presence_of_all_elements_located if mode_multi else EC.presence_of_element_located
        element = WebDriverWait(driver, delay).until(element_func((locator, name)))
        
        log(f"GOTTED: {name} - BY {search_type}")
        return element
        
    except Exception as e:
        log(f"ERR FIND_ELEMENT {name}: {e}" if err is None else err)
        return None

def enter_text(element, text, enter = True):
    """
    Nhập dãy kí tự vào đối tượng
    
    Args:
        element: đối tượng
        text: dãy kí tự
    """
    try:
        element.send_keys(text)
        if enter:
            element.send_keys(Keys.RETURN)
            
        log(f"ENTERED: {text} -TO- {element}")
        return True
    except Exception as e:
        log(f"ERR ENTER_TEXT {element}: {e}")

def click(element, count = 1, delay = 0.1, err = None):
    """
    Nhấn đối tượng
    
    Args:
        element: đối tượng
        count: số lần nhấn (mặc định là 1)
        delay: thời gian chờ giữa các lần nhấn (mặc định là 0.1 giây)
    """
    try:
        if count < 1:
            raise ValueError("Số lần nhấn phải lớn hơn hoặc bằng 1")
        
        for i in range(count):
            element.click()
            time.sleep(delay)
        log(f"CLICKED: {element}")
        return True
    
    except Exception as e:
        log(f"ERR CLICK {element}: {e}" if err is None else err)

if __name__ != "__main__":
    print("LOAD MODULE:", __name__, "FINISHED!")