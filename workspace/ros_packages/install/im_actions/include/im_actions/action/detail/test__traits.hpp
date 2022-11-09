// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from im_actions:action/Test.idl
// generated code does not contain a copyright notice

#ifndef IM_ACTIONS__ACTION__DETAIL__TEST__TRAITS_HPP_
#define IM_ACTIONS__ACTION__DETAIL__TEST__TRAITS_HPP_

#include "im_actions/action/detail/test__struct.hpp"
#include <rosidl_runtime_cpp/traits.hpp>
#include <stdint.h>
#include <type_traits>

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<im_actions::action::Test_Goal>()
{
  return "im_actions::action::Test_Goal";
}

template<>
inline const char * name<im_actions::action::Test_Goal>()
{
  return "im_actions/action/Test_Goal";
}

template<>
struct has_fixed_size<im_actions::action::Test_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<im_actions::action::Test_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<im_actions::action::Test_Goal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<im_actions::action::Test_Result>()
{
  return "im_actions::action::Test_Result";
}

template<>
inline const char * name<im_actions::action::Test_Result>()
{
  return "im_actions/action/Test_Result";
}

template<>
struct has_fixed_size<im_actions::action::Test_Result>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<im_actions::action::Test_Result>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<im_actions::action::Test_Result>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<im_actions::action::Test_Feedback>()
{
  return "im_actions::action::Test_Feedback";
}

template<>
inline const char * name<im_actions::action::Test_Feedback>()
{
  return "im_actions/action/Test_Feedback";
}

template<>
struct has_fixed_size<im_actions::action::Test_Feedback>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<im_actions::action::Test_Feedback>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<im_actions::action::Test_Feedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'goal'
#include "im_actions/action/detail/test__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<im_actions::action::Test_SendGoal_Request>()
{
  return "im_actions::action::Test_SendGoal_Request";
}

template<>
inline const char * name<im_actions::action::Test_SendGoal_Request>()
{
  return "im_actions/action/Test_SendGoal_Request";
}

template<>
struct has_fixed_size<im_actions::action::Test_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<im_actions::action::Test_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<im_actions::action::Test_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<im_actions::action::Test_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<im_actions::action::Test_SendGoal_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<im_actions::action::Test_SendGoal_Response>()
{
  return "im_actions::action::Test_SendGoal_Response";
}

template<>
inline const char * name<im_actions::action::Test_SendGoal_Response>()
{
  return "im_actions/action/Test_SendGoal_Response";
}

template<>
struct has_fixed_size<im_actions::action::Test_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<im_actions::action::Test_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<im_actions::action::Test_SendGoal_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<im_actions::action::Test_SendGoal>()
{
  return "im_actions::action::Test_SendGoal";
}

template<>
inline const char * name<im_actions::action::Test_SendGoal>()
{
  return "im_actions/action/Test_SendGoal";
}

template<>
struct has_fixed_size<im_actions::action::Test_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<im_actions::action::Test_SendGoal_Request>::value &&
    has_fixed_size<im_actions::action::Test_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<im_actions::action::Test_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<im_actions::action::Test_SendGoal_Request>::value &&
    has_bounded_size<im_actions::action::Test_SendGoal_Response>::value
  >
{
};

template<>
struct is_service<im_actions::action::Test_SendGoal>
  : std::true_type
{
};

template<>
struct is_service_request<im_actions::action::Test_SendGoal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<im_actions::action::Test_SendGoal_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<im_actions::action::Test_GetResult_Request>()
{
  return "im_actions::action::Test_GetResult_Request";
}

template<>
inline const char * name<im_actions::action::Test_GetResult_Request>()
{
  return "im_actions/action/Test_GetResult_Request";
}

template<>
struct has_fixed_size<im_actions::action::Test_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<im_actions::action::Test_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<im_actions::action::Test_GetResult_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'result'
// already included above
// #include "im_actions/action/detail/test__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<im_actions::action::Test_GetResult_Response>()
{
  return "im_actions::action::Test_GetResult_Response";
}

template<>
inline const char * name<im_actions::action::Test_GetResult_Response>()
{
  return "im_actions/action/Test_GetResult_Response";
}

template<>
struct has_fixed_size<im_actions::action::Test_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<im_actions::action::Test_Result>::value> {};

template<>
struct has_bounded_size<im_actions::action::Test_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<im_actions::action::Test_Result>::value> {};

template<>
struct is_message<im_actions::action::Test_GetResult_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<im_actions::action::Test_GetResult>()
{
  return "im_actions::action::Test_GetResult";
}

template<>
inline const char * name<im_actions::action::Test_GetResult>()
{
  return "im_actions/action/Test_GetResult";
}

template<>
struct has_fixed_size<im_actions::action::Test_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<im_actions::action::Test_GetResult_Request>::value &&
    has_fixed_size<im_actions::action::Test_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<im_actions::action::Test_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<im_actions::action::Test_GetResult_Request>::value &&
    has_bounded_size<im_actions::action::Test_GetResult_Response>::value
  >
{
};

template<>
struct is_service<im_actions::action::Test_GetResult>
  : std::true_type
{
};

template<>
struct is_service_request<im_actions::action::Test_GetResult_Request>
  : std::true_type
{
};

template<>
struct is_service_response<im_actions::action::Test_GetResult_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'feedback'
// already included above
// #include "im_actions/action/detail/test__traits.hpp"

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<im_actions::action::Test_FeedbackMessage>()
{
  return "im_actions::action::Test_FeedbackMessage";
}

template<>
inline const char * name<im_actions::action::Test_FeedbackMessage>()
{
  return "im_actions/action/Test_FeedbackMessage";
}

template<>
struct has_fixed_size<im_actions::action::Test_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<im_actions::action::Test_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<im_actions::action::Test_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<im_actions::action::Test_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<im_actions::action::Test_FeedbackMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits


namespace rosidl_generator_traits
{

template<>
struct is_action<im_actions::action::Test>
  : std::true_type
{
};

template<>
struct is_action_goal<im_actions::action::Test_Goal>
  : std::true_type
{
};

template<>
struct is_action_result<im_actions::action::Test_Result>
  : std::true_type
{
};

template<>
struct is_action_feedback<im_actions::action::Test_Feedback>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits


#endif  // IM_ACTIONS__ACTION__DETAIL__TEST__TRAITS_HPP_
