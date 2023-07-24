#include <iostream>
#include <string>
#include <Windows.h>

int main() {
    std::wstring chinese = L"ÄãºÃ£¬ÊÀ½ç£¡";
    WriteConsoleW(GetStdHandle(STD_OUTPUT_HANDLE), chinese.c_str(), chinese.length(), NULL, NULL);
    return 0;
}

