// generated from rosidl_generator_c/resource/rosidl_generator_c__visibility_control.h.in
// generated code does not contain a copyright notice

#ifndef IM_ACTIONS__MSG__ROSIDL_GENERATOR_C__VISIBILITY_CONTROL_H_
#define IM_ACTIONS__MSG__ROSIDL_GENERATOR_C__VISIBILITY_CONTROL_H_

#ifdef __cplusplus
extern "C"
{
#endif

// This logic was borrowed (then namespaced) from the examples on the gcc wiki:
//     https://gcc.gnu.org/wiki/Visibility

#if defined _WIN32 || defined __CYGWIN__
  #ifdef __GNUC__
    #define ROSIDL_GENERATOR_C_EXPORT_im_actions __attribute__ ((dllexport))
    #define ROSIDL_GENERATOR_C_IMPORT_im_actions __attribute__ ((dllimport))
  #else
    #define ROSIDL_GENERATOR_C_EXPORT_im_actions __declspec(dllexport)
    #define ROSIDL_GENERATOR_C_IMPORT_im_actions __declspec(dllimport)
  #endif
  #ifdef ROSIDL_GENERATOR_C_BUILDING_DLL_im_actions
    #define ROSIDL_GENERATOR_C_PUBLIC_im_actions ROSIDL_GENERATOR_C_EXPORT_im_actions
  #else
    #define ROSIDL_GENERATOR_C_PUBLIC_im_actions ROSIDL_GENERATOR_C_IMPORT_im_actions
  #endif
#else
  #define ROSIDL_GENERATOR_C_EXPORT_im_actions __attribute__ ((visibility("default")))
  #define ROSIDL_GENERATOR_C_IMPORT_im_actions
  #if __GNUC__ >= 4
    #define ROSIDL_GENERATOR_C_PUBLIC_im_actions __attribute__ ((visibility("default")))
  #else
    #define ROSIDL_GENERATOR_C_PUBLIC_im_actions
  #endif
#endif

#ifdef __cplusplus
}
#endif

#endif  // IM_ACTIONS__MSG__ROSIDL_GENERATOR_C__VISIBILITY_CONTROL_H_
