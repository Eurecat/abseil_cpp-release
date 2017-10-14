cmake_minimum_required(VERSION 2.8.3)
project(abseil_cpp)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

find_package(catkin REQUIRED)


###################################
## catkin specific configuration ##
###################################

catkin_package(
   INCLUDE_DIRS ./ cctz/include
   LIBRARIES abseil_cpp
)

###########
## Build ##
###########

## Specify additional locations of header files
## Your package locations should be listed before other locations
include_directories(
 ./
 cctz/include
 ${catkin_INCLUDE_DIRS}
)

file(GLOB_RECURSE source_list "*.cc" )
file(GLOB_RECURSE test_list "*test*.cc" )

list(REMOVE_ITEM source_list ${test_list})
list(REMOVE_ITEM source_list ${CMAKE_CURRENT_SOURCE_DIR}/absl/synchronization/internal/mutex_nonprod.cc )
list(REMOVE_ITEM source_list ${CMAKE_CURRENT_SOURCE_DIR}/cctz/src/benchmarks.cc )
list(REMOVE_ITEM source_list ${CMAKE_CURRENT_SOURCE_DIR}/cctz/src/time_tool.cc )

## Declare a C++ library
add_library(${PROJECT_NAME}  ${source_list} )


#############
## Install ##
#############

# all install targets should use catkin DESTINATION variables
# See http://ros.org/doc/api/catkin/html/adv_user_guide/variables.html

## Mark executables and/or libraries for installation
install(TARGETS ${PROJECT_NAME}
   ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
   RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
 )

## Mark cpp header files for installation
install(DIRECTORY absl/
    DESTINATION ${CATKIN_GLOBAL_INCLUDE_DESTINATION}/absl
    FILES_MATCHING PATTERN "*.h"
    PATTERN ".svn" EXCLUDE
 )

install(DIRECTORY cctz/include/
    DESTINATION ${CATKIN_GLOBAL_INCLUDE_DESTINATION}
    FILES_MATCHING PATTERN "*.h"
    PATTERN ".svn" EXCLUDE
 )
