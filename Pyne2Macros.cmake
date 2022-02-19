# Print pyne logo
macro(pyne2_print_logo)
  set(cat_prog cat)
  if(WIN32)
    set(cat_prog type)
  endif(WIN32)
  execute_process(COMMAND ${cat_prog}
                  ${PROJECT_SOURCE_DIR}/config/logo.txt
                  OUTPUT_VARIABLE variable)
  message("${variable}")
endmacro()

macro(pyne2_set_products)
  SET(PYNE2_PROJECT_NAME "pyne2_${PYNE2_COMP_NAME}")
  SET(PYNE2_LIB_NAME "${PYNE2_PROJECT_NAME}")
  SET(PYNE2_VERSION_HEADER "${PYNE2_COMP_NAME}_version.h")
endmacro()

