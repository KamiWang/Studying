# CMake最低版本
cmake_minimum_required (VERSION 2.8)

# 项目名称
project (Studying)

# 添加目录下的所有源文件
aux_source_directory(./DesignPatterns/ DesignPatternsSource)

# 指定生成目标
add_executable(studying main.cpp ${DesignPatternsSource})
