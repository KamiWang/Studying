# CMake最低版本
CMAKE_MINIMUM_REQUIRED (VERSION 2.8)

# 项目名称
PROJECT (Studying)

# 添加目录下的所有源文件
AUX_SOURCE_DIRECTORY(./DesignPatterns/ DesignPatternsSource)

# 设置为C++最新标准
INCLUDE(CheckCXXCompilerFlag)
IF(MSVC)
	CHECK_CXX_COMPILER_FLAG("/std:c++latest" _cpp_latest_flag_supported)
	IF(_cpp_latest_flag_supported)
		ADD_COMPILE_OPTIONS("/std:c++latest")
	ENDIF()
ELSE()
	CHECK_CXX_COMPILER_FLAG("-std=c++17" _cpp_latest_flag_supported)
	if(_cpp_latest_flag_supported)
		ADD_DEFINITIONS("-std=c++17")
	endif()
ENDIF()


MESSAGE(STATUS "操作系统:${CMAKE_SYSTEM}")
MESSAGE(STATUS "编译器:${CMAKE_CXX_COMPILER}")

# 指定生成目标
ADD_EXECUTABLE(studying main.cpp ${DesignPatternsSource})




