cmake_minimum_required(VERSION 3.5 FATAL_ERROR)

project(ggMatrixElements)
set(PROJECT_VERSION 1)
set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O3")
set(CMAKE_BUILD_TYPE Release)
set(EXECUTABLE_OUTPUT_PATH "${PROJECT_BINARY_DIR}/bin")

include_directories(${PROJECT_SOURCE_DIR})

find_package(GSL REQUIRED)
find_package(Boost COMPONENTS system python REQUIRED)
find_package(Python COMPONENTS Interpreter Development REQUIRED)

file(GLOB LIBRARY_SOURCES src/*.cc)

add_library(ggMatrixElements SHARED ${LIBRARY_SOURCES})
target_link_libraries(ggMatrixElements GSL::gsl ${Boost_LIBRARIES})
target_include_directories(ggMatrixElements PUBLIC ${Python_INCLUDE_DIRS} ${Boost_INCLUDE_DIRS})
set_target_properties(ggMatrixElements PROPERTIES PREFIX "")
install(TARGETS ggMatrixElements DESTINATION ${CMAKE_INSTALL_LIBDIR})
