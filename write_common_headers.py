# Generate a standardized C++ header to capture the version

def write_version_header(P2C_NAME='P2C_COMP', 
                         P2C_MAJOR_VERSION=0, 
                         P2C_MINOR_VERSION=0, 
                         P2C_PATCH_VERSION=0):

    P2C_VERSION_H = f'{P2C_NAME}_version.h'
    P2C_VERSION = f'{P2C_MAJOR_VERSION}.{P2C_MINOR_VERSION}.{P2C_PATCH_VERSION}'

    with open(P2C_VERSION_H, 'w') as pvh:
        header_text = f'''#ifndef {P2C_NAME}_VERSION_HEADER
#define {P2C_NAME}_VERSION_HEADER

#define {P2C_NAME}_VERSION {P2C_VERSION}
#define {P2C_NAME}_VERSION_STRING "{P2C_VERSION}"

#endif // {P2C_NAME}_VERSION_HEADER
'''
        pvh.write(header_text)

    return P2C_VERSION

