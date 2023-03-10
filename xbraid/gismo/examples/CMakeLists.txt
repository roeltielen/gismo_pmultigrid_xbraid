### CMakeLists.txt ---
##
## Author: Angelos Mantzaflaris
## Author: Harald Weiner
## Copyright (C) 2012-2018 - RICAM-Linz.
######################################################################

project(examples)

set(CMAKE_DIRECTORY_LABELS "${PROJECT_NAME}") #CMake 3.10

# Add a grouping target that builds all tests this is equivalent to
# running "make" inside the tests build folder
add_custom_target(${PROJECT_NAME})
set_target_properties(${PROJECT_NAME} PROPERTIES LABELS "${PROJECT_NAME}" FOLDER "${PROJECT_NAME}")

#find_package(gismo REQUIRED)
#include_directories( ${GISMO_INCLUDE_DIRS})
#link_directories   ( ${GISMO_LIBRARY_DIR} )
#include( ${GISMO_USE_FILE})

# Collect source file names
aux_cpp_directory(${CMAKE_CURRENT_SOURCE_DIR} FILES)
#message("found files: ${FILES}")

#set(CPP_FILES_98 )
#set(CPP_FILES_11 ${CPP_FILES_98} )
#set(CPP_FILES_14 ${CPP_FILES_98} ${CPP_FILES_11} )

foreach(file ${FILES})

    add_gismo_executable(${file})
    get_filename_component(tarname ${file} NAME_WE) # name without extension
    set_property(TEST ${tarname} PROPERTY LABELS "${PROJECT_NAME}")
    set_target_properties(${tarname} PROPERTIES FOLDER "${PROJECT_NAME}")
    add_dependencies(${PROJECT_NAME} ${tarname})

    # install the example executables (optionally)
    install(TARGETS ${tarname} DESTINATION "${BIN_INSTALL_DIR}" COMPONENT exe OPTIONAL)

endforeach(file ${FILES})

list(LENGTH FILES len)
message(STATUS "Number of examples to compile: ${len}")

set(EXECUTABLE_OUTPUT_PATH ${CMAKE_BINARY_DIR}/bin/)
