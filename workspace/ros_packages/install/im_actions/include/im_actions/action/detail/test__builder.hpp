// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from im_actions:action/Test.idl
// generated code does not contain a copyright notice

#ifndef IM_ACTIONS__ACTION__DETAIL__TEST__BUILDER_HPP_
#define IM_ACTIONS__ACTION__DETAIL__TEST__BUILDER_HPP_

#include "im_actions/action/detail/test__struct.hpp"
#include <rosidl_runtime_cpp/message_initialization.hpp>
#include <algorithm>
#include <utility>


namespace im_actions
{

namespace action
{

namespace builder
{

class Init_Test_Goal_order
{
public:
  Init_Test_Goal_order()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::im_actions::action::Test_Goal order(::im_actions::action::Test_Goal::_order_type arg)
  {
    msg_.order = std::move(arg);
    return std::move(msg_);
  }

private:
  ::im_actions::action::Test_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::im_actions::action::Test_Goal>()
{
  return im_actions::action::builder::Init_Test_Goal_order();
}

}  // namespace im_actions


namespace im_actions
{

namespace action
{

namespace builder
{

class Init_Test_Result_sequence
{
public:
  Init_Test_Result_sequence()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::im_actions::action::Test_Result sequence(::im_actions::action::Test_Result::_sequence_type arg)
  {
    msg_.sequence = std::move(arg);
    return std::move(msg_);
  }

private:
  ::im_actions::action::Test_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::im_actions::action::Test_Result>()
{
  return im_actions::action::builder::Init_Test_Result_sequence();
}

}  // namespace im_actions


namespace im_actions
{

namespace action
{

namespace builder
{

class Init_Test_Feedback_partial_sequence
{
public:
  Init_Test_Feedback_partial_sequence()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::im_actions::action::Test_Feedback partial_sequence(::im_actions::action::Test_Feedback::_partial_sequence_type arg)
  {
    msg_.partial_sequence = std::move(arg);
    return std::move(msg_);
  }

private:
  ::im_actions::action::Test_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::im_actions::action::Test_Feedback>()
{
  return im_actions::action::builder::Init_Test_Feedback_partial_sequence();
}

}  // namespace im_actions


namespace im_actions
{

namespace action
{

namespace builder
{

class Init_Test_SendGoal_Request_goal
{
public:
  explicit Init_Test_SendGoal_Request_goal(::im_actions::action::Test_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::im_actions::action::Test_SendGoal_Request goal(::im_actions::action::Test_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::im_actions::action::Test_SendGoal_Request msg_;
};

class Init_Test_SendGoal_Request_goal_id
{
public:
  Init_Test_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Test_SendGoal_Request_goal goal_id(::im_actions::action::Test_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Test_SendGoal_Request_goal(msg_);
  }

private:
  ::im_actions::action::Test_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::im_actions::action::Test_SendGoal_Request>()
{
  return im_actions::action::builder::Init_Test_SendGoal_Request_goal_id();
}

}  // namespace im_actions


namespace im_actions
{

namespace action
{

namespace builder
{

class Init_Test_SendGoal_Response_stamp
{
public:
  explicit Init_Test_SendGoal_Response_stamp(::im_actions::action::Test_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::im_actions::action::Test_SendGoal_Response stamp(::im_actions::action::Test_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::im_actions::action::Test_SendGoal_Response msg_;
};

class Init_Test_SendGoal_Response_accepted
{
public:
  Init_Test_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Test_SendGoal_Response_stamp accepted(::im_actions::action::Test_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_Test_SendGoal_Response_stamp(msg_);
  }

private:
  ::im_actions::action::Test_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::im_actions::action::Test_SendGoal_Response>()
{
  return im_actions::action::builder::Init_Test_SendGoal_Response_accepted();
}

}  // namespace im_actions


namespace im_actions
{

namespace action
{

namespace builder
{

class Init_Test_GetResult_Request_goal_id
{
public:
  Init_Test_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::im_actions::action::Test_GetResult_Request goal_id(::im_actions::action::Test_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::im_actions::action::Test_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::im_actions::action::Test_GetResult_Request>()
{
  return im_actions::action::builder::Init_Test_GetResult_Request_goal_id();
}

}  // namespace im_actions


namespace im_actions
{

namespace action
{

namespace builder
{

class Init_Test_GetResult_Response_result
{
public:
  explicit Init_Test_GetResult_Response_result(::im_actions::action::Test_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::im_actions::action::Test_GetResult_Response result(::im_actions::action::Test_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::im_actions::action::Test_GetResult_Response msg_;
};

class Init_Test_GetResult_Response_status
{
public:
  Init_Test_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Test_GetResult_Response_result status(::im_actions::action::Test_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_Test_GetResult_Response_result(msg_);
  }

private:
  ::im_actions::action::Test_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::im_actions::action::Test_GetResult_Response>()
{
  return im_actions::action::builder::Init_Test_GetResult_Response_status();
}

}  // namespace im_actions


namespace im_actions
{

namespace action
{

namespace builder
{

class Init_Test_FeedbackMessage_feedback
{
public:
  explicit Init_Test_FeedbackMessage_feedback(::im_actions::action::Test_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::im_actions::action::Test_FeedbackMessage feedback(::im_actions::action::Test_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::im_actions::action::Test_FeedbackMessage msg_;
};

class Init_Test_FeedbackMessage_goal_id
{
public:
  Init_Test_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_Test_FeedbackMessage_feedback goal_id(::im_actions::action::Test_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_Test_FeedbackMessage_feedback(msg_);
  }

private:
  ::im_actions::action::Test_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::im_actions::action::Test_FeedbackMessage>()
{
  return im_actions::action::builder::Init_Test_FeedbackMessage_goal_id();
}

}  // namespace im_actions

#endif  // IM_ACTIONS__ACTION__DETAIL__TEST__BUILDER_HPP_
