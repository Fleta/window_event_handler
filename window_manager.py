import win32gui
import win32con
import re

class WindowMgr:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        self._handle = None

    def find_window(self, class_name, window_name=None):
        """find a window by its class_name"""
        self._handle = win32gui.FindWindow(class_name, window_name)
        print(self._handle)

    def _window_enum_callback(self, hwnd, wildcard):
        """Pass to win32gui.EnumWindows() to check all the opened windows"""
        if re.match(wildcard, str(win32gui.GetWindowText(hwnd))) is not None:
            self._handle = hwnd

    def find_window_wildcard(self, wildcard):
        """find a window whose title matches the wildcard regex"""
        self._handle = None
        win32gui.EnumWindows(self._window_enum_callback, wildcard)
        return self

    def show_window(self):
        """put the window in the foreground"""
        # win32gui.SetForegroundWindow(self._handle)
        win32gui.ShowWindow(self._handle, win32con.SW_SHOWMAXIMIZED)
