// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from im_actions:action/Test.idl
// generated code does not contain a copyright notice
#include "im_actions/action/detail/test__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


bool
im_actions__action__Test_Goal__init(im_actions__action__Test_Goal * msg)
{
  if (!msg) {
    return false;
  }
  // order
  return true;
}

void
im_actions__action__Test_Goal__fini(im_actions__action__Test_Goal * msg)
{
  if (!msg) {
    return;
  }
  // order
}

bool
im_actions__action__Test_Goal__are_equal(const im_actions__action__Test_Goal * lhs, const im_actions__action__Test_Goal * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // order
  if (lhs->order != rhs->order) {
    return false;
  }
  return true;
}

bool
im_actions__action__Test_Goal__copy(
  const im_actions__action__Test_Goal * input,
  im_actions__action__Test_Goal * output)
{
  if (!input || !output) {
    return false;
  }
  // order
  output->order = input->order;
  return true;
}

im_actions__action__Test_Goal *
im_actions__action__Test_Goal__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_Goal * msg = (im_actions__action__Test_Goal *)allocator.allocate(sizeof(im_actions__action__Test_Goal), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(im_actions__action__Test_Goal));
  bool success = im_actions__action__Test_Goal__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
im_actions__action__Test_Goal__destroy(im_actions__action__Test_Goal * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    im_actions__action__Test_Goal__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
im_actions__action__Test_Goal__Sequence__init(im_actions__action__Test_Goal__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_Goal * data = NULL;

  if (size) {
    data = (im_actions__action__Test_Goal *)allocator.zero_allocate(size, sizeof(im_actions__action__Test_Goal), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = im_actions__action__Test_Goal__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        im_actions__action__Test_Goal__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
im_actions__action__Test_Goal__Sequence__fini(im_actions__action__Test_Goal__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      im_actions__action__Test_Goal__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

im_actions__action__Test_Goal__Sequence *
im_actions__action__Test_Goal__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_Goal__Sequence * array = (im_actions__action__Test_Goal__Sequence *)allocator.allocate(sizeof(im_actions__action__Test_Goal__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = im_actions__action__Test_Goal__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
im_actions__action__Test_Goal__Sequence__destroy(im_actions__action__Test_Goal__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    im_actions__action__Test_Goal__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
im_actions__action__Test_Goal__Sequence__are_equal(const im_actions__action__Test_Goal__Sequence * lhs, const im_actions__action__Test_Goal__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!im_actions__action__Test_Goal__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
im_actions__action__Test_Goal__Sequence__copy(
  const im_actions__action__Test_Goal__Sequence * input,
  im_actions__action__Test_Goal__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(im_actions__action__Test_Goal);
    im_actions__action__Test_Goal * data =
      (im_actions__action__Test_Goal *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!im_actions__action__Test_Goal__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          im_actions__action__Test_Goal__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!im_actions__action__Test_Goal__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `sequence`
#include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
im_actions__action__Test_Result__init(im_actions__action__Test_Result * msg)
{
  if (!msg) {
    return false;
  }
  // sequence
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->sequence, 0)) {
    im_actions__action__Test_Result__fini(msg);
    return false;
  }
  return true;
}

void
im_actions__action__Test_Result__fini(im_actions__action__Test_Result * msg)
{
  if (!msg) {
    return;
  }
  // sequence
  rosidl_runtime_c__int32__Sequence__fini(&msg->sequence);
}

bool
im_actions__action__Test_Result__are_equal(const im_actions__action__Test_Result * lhs, const im_actions__action__Test_Result * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // sequence
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->sequence), &(rhs->sequence)))
  {
    return false;
  }
  return true;
}

bool
im_actions__action__Test_Result__copy(
  const im_actions__action__Test_Result * input,
  im_actions__action__Test_Result * output)
{
  if (!input || !output) {
    return false;
  }
  // sequence
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->sequence), &(output->sequence)))
  {
    return false;
  }
  return true;
}

im_actions__action__Test_Result *
im_actions__action__Test_Result__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_Result * msg = (im_actions__action__Test_Result *)allocator.allocate(sizeof(im_actions__action__Test_Result), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(im_actions__action__Test_Result));
  bool success = im_actions__action__Test_Result__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
im_actions__action__Test_Result__destroy(im_actions__action__Test_Result * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    im_actions__action__Test_Result__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
im_actions__action__Test_Result__Sequence__init(im_actions__action__Test_Result__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_Result * data = NULL;

  if (size) {
    data = (im_actions__action__Test_Result *)allocator.zero_allocate(size, sizeof(im_actions__action__Test_Result), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = im_actions__action__Test_Result__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        im_actions__action__Test_Result__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
im_actions__action__Test_Result__Sequence__fini(im_actions__action__Test_Result__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      im_actions__action__Test_Result__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

im_actions__action__Test_Result__Sequence *
im_actions__action__Test_Result__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_Result__Sequence * array = (im_actions__action__Test_Result__Sequence *)allocator.allocate(sizeof(im_actions__action__Test_Result__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = im_actions__action__Test_Result__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
im_actions__action__Test_Result__Sequence__destroy(im_actions__action__Test_Result__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    im_actions__action__Test_Result__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
im_actions__action__Test_Result__Sequence__are_equal(const im_actions__action__Test_Result__Sequence * lhs, const im_actions__action__Test_Result__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!im_actions__action__Test_Result__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
im_actions__action__Test_Result__Sequence__copy(
  const im_actions__action__Test_Result__Sequence * input,
  im_actions__action__Test_Result__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(im_actions__action__Test_Result);
    im_actions__action__Test_Result * data =
      (im_actions__action__Test_Result *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!im_actions__action__Test_Result__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          im_actions__action__Test_Result__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!im_actions__action__Test_Result__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `partial_sequence`
// already included above
// #include "rosidl_runtime_c/primitives_sequence_functions.h"

bool
im_actions__action__Test_Feedback__init(im_actions__action__Test_Feedback * msg)
{
  if (!msg) {
    return false;
  }
  // partial_sequence
  if (!rosidl_runtime_c__int32__Sequence__init(&msg->partial_sequence, 0)) {
    im_actions__action__Test_Feedback__fini(msg);
    return false;
  }
  return true;
}

void
im_actions__action__Test_Feedback__fini(im_actions__action__Test_Feedback * msg)
{
  if (!msg) {
    return;
  }
  // partial_sequence
  rosidl_runtime_c__int32__Sequence__fini(&msg->partial_sequence);
}

bool
im_actions__action__Test_Feedback__are_equal(const im_actions__action__Test_Feedback * lhs, const im_actions__action__Test_Feedback * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // partial_sequence
  if (!rosidl_runtime_c__int32__Sequence__are_equal(
      &(lhs->partial_sequence), &(rhs->partial_sequence)))
  {
    return false;
  }
  return true;
}

bool
im_actions__action__Test_Feedback__copy(
  const im_actions__action__Test_Feedback * input,
  im_actions__action__Test_Feedback * output)
{
  if (!input || !output) {
    return false;
  }
  // partial_sequence
  if (!rosidl_runtime_c__int32__Sequence__copy(
      &(input->partial_sequence), &(output->partial_sequence)))
  {
    return false;
  }
  return true;
}

im_actions__action__Test_Feedback *
im_actions__action__Test_Feedback__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_Feedback * msg = (im_actions__action__Test_Feedback *)allocator.allocate(sizeof(im_actions__action__Test_Feedback), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(im_actions__action__Test_Feedback));
  bool success = im_actions__action__Test_Feedback__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
im_actions__action__Test_Feedback__destroy(im_actions__action__Test_Feedback * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    im_actions__action__Test_Feedback__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
im_actions__action__Test_Feedback__Sequence__init(im_actions__action__Test_Feedback__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_Feedback * data = NULL;

  if (size) {
    data = (im_actions__action__Test_Feedback *)allocator.zero_allocate(size, sizeof(im_actions__action__Test_Feedback), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = im_actions__action__Test_Feedback__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        im_actions__action__Test_Feedback__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
im_actions__action__Test_Feedback__Sequence__fini(im_actions__action__Test_Feedback__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      im_actions__action__Test_Feedback__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

im_actions__action__Test_Feedback__Sequence *
im_actions__action__Test_Feedback__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_Feedback__Sequence * array = (im_actions__action__Test_Feedback__Sequence *)allocator.allocate(sizeof(im_actions__action__Test_Feedback__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = im_actions__action__Test_Feedback__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
im_actions__action__Test_Feedback__Sequence__destroy(im_actions__action__Test_Feedback__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    im_actions__action__Test_Feedback__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
im_actions__action__Test_Feedback__Sequence__are_equal(const im_actions__action__Test_Feedback__Sequence * lhs, const im_actions__action__Test_Feedback__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!im_actions__action__Test_Feedback__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
im_actions__action__Test_Feedback__Sequence__copy(
  const im_actions__action__Test_Feedback__Sequence * input,
  im_actions__action__Test_Feedback__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(im_actions__action__Test_Feedback);
    im_actions__action__Test_Feedback * data =
      (im_actions__action__Test_Feedback *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!im_actions__action__Test_Feedback__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          im_actions__action__Test_Feedback__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!im_actions__action__Test_Feedback__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
#include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `goal`
// already included above
// #include "im_actions/action/detail/test__functions.h"

bool
im_actions__action__Test_SendGoal_Request__init(im_actions__action__Test_SendGoal_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    im_actions__action__Test_SendGoal_Request__fini(msg);
    return false;
  }
  // goal
  if (!im_actions__action__Test_Goal__init(&msg->goal)) {
    im_actions__action__Test_SendGoal_Request__fini(msg);
    return false;
  }
  return true;
}

void
im_actions__action__Test_SendGoal_Request__fini(im_actions__action__Test_SendGoal_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // goal
  im_actions__action__Test_Goal__fini(&msg->goal);
}

bool
im_actions__action__Test_SendGoal_Request__are_equal(const im_actions__action__Test_SendGoal_Request * lhs, const im_actions__action__Test_SendGoal_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  // goal
  if (!im_actions__action__Test_Goal__are_equal(
      &(lhs->goal), &(rhs->goal)))
  {
    return false;
  }
  return true;
}

bool
im_actions__action__Test_SendGoal_Request__copy(
  const im_actions__action__Test_SendGoal_Request * input,
  im_actions__action__Test_SendGoal_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  // goal
  if (!im_actions__action__Test_Goal__copy(
      &(input->goal), &(output->goal)))
  {
    return false;
  }
  return true;
}

im_actions__action__Test_SendGoal_Request *
im_actions__action__Test_SendGoal_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_SendGoal_Request * msg = (im_actions__action__Test_SendGoal_Request *)allocator.allocate(sizeof(im_actions__action__Test_SendGoal_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(im_actions__action__Test_SendGoal_Request));
  bool success = im_actions__action__Test_SendGoal_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
im_actions__action__Test_SendGoal_Request__destroy(im_actions__action__Test_SendGoal_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    im_actions__action__Test_SendGoal_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
im_actions__action__Test_SendGoal_Request__Sequence__init(im_actions__action__Test_SendGoal_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_SendGoal_Request * data = NULL;

  if (size) {
    data = (im_actions__action__Test_SendGoal_Request *)allocator.zero_allocate(size, sizeof(im_actions__action__Test_SendGoal_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = im_actions__action__Test_SendGoal_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        im_actions__action__Test_SendGoal_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
im_actions__action__Test_SendGoal_Request__Sequence__fini(im_actions__action__Test_SendGoal_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      im_actions__action__Test_SendGoal_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

im_actions__action__Test_SendGoal_Request__Sequence *
im_actions__action__Test_SendGoal_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_SendGoal_Request__Sequence * array = (im_actions__action__Test_SendGoal_Request__Sequence *)allocator.allocate(sizeof(im_actions__action__Test_SendGoal_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = im_actions__action__Test_SendGoal_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
im_actions__action__Test_SendGoal_Request__Sequence__destroy(im_actions__action__Test_SendGoal_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    im_actions__action__Test_SendGoal_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
im_actions__action__Test_SendGoal_Request__Sequence__are_equal(const im_actions__action__Test_SendGoal_Request__Sequence * lhs, const im_actions__action__Test_SendGoal_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!im_actions__action__Test_SendGoal_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
im_actions__action__Test_SendGoal_Request__Sequence__copy(
  const im_actions__action__Test_SendGoal_Request__Sequence * input,
  im_actions__action__Test_SendGoal_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(im_actions__action__Test_SendGoal_Request);
    im_actions__action__Test_SendGoal_Request * data =
      (im_actions__action__Test_SendGoal_Request *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!im_actions__action__Test_SendGoal_Request__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          im_actions__action__Test_SendGoal_Request__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!im_actions__action__Test_SendGoal_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `stamp`
#include "builtin_interfaces/msg/detail/time__functions.h"

bool
im_actions__action__Test_SendGoal_Response__init(im_actions__action__Test_SendGoal_Response * msg)
{
  if (!msg) {
    return false;
  }
  // accepted
  // stamp
  if (!builtin_interfaces__msg__Time__init(&msg->stamp)) {
    im_actions__action__Test_SendGoal_Response__fini(msg);
    return false;
  }
  return true;
}

void
im_actions__action__Test_SendGoal_Response__fini(im_actions__action__Test_SendGoal_Response * msg)
{
  if (!msg) {
    return;
  }
  // accepted
  // stamp
  builtin_interfaces__msg__Time__fini(&msg->stamp);
}

bool
im_actions__action__Test_SendGoal_Response__are_equal(const im_actions__action__Test_SendGoal_Response * lhs, const im_actions__action__Test_SendGoal_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // accepted
  if (lhs->accepted != rhs->accepted) {
    return false;
  }
  // stamp
  if (!builtin_interfaces__msg__Time__are_equal(
      &(lhs->stamp), &(rhs->stamp)))
  {
    return false;
  }
  return true;
}

bool
im_actions__action__Test_SendGoal_Response__copy(
  const im_actions__action__Test_SendGoal_Response * input,
  im_actions__action__Test_SendGoal_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // accepted
  output->accepted = input->accepted;
  // stamp
  if (!builtin_interfaces__msg__Time__copy(
      &(input->stamp), &(output->stamp)))
  {
    return false;
  }
  return true;
}

im_actions__action__Test_SendGoal_Response *
im_actions__action__Test_SendGoal_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_SendGoal_Response * msg = (im_actions__action__Test_SendGoal_Response *)allocator.allocate(sizeof(im_actions__action__Test_SendGoal_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(im_actions__action__Test_SendGoal_Response));
  bool success = im_actions__action__Test_SendGoal_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
im_actions__action__Test_SendGoal_Response__destroy(im_actions__action__Test_SendGoal_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    im_actions__action__Test_SendGoal_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
im_actions__action__Test_SendGoal_Response__Sequence__init(im_actions__action__Test_SendGoal_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_SendGoal_Response * data = NULL;

  if (size) {
    data = (im_actions__action__Test_SendGoal_Response *)allocator.zero_allocate(size, sizeof(im_actions__action__Test_SendGoal_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = im_actions__action__Test_SendGoal_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        im_actions__action__Test_SendGoal_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
im_actions__action__Test_SendGoal_Response__Sequence__fini(im_actions__action__Test_SendGoal_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      im_actions__action__Test_SendGoal_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

im_actions__action__Test_SendGoal_Response__Sequence *
im_actions__action__Test_SendGoal_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_SendGoal_Response__Sequence * array = (im_actions__action__Test_SendGoal_Response__Sequence *)allocator.allocate(sizeof(im_actions__action__Test_SendGoal_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = im_actions__action__Test_SendGoal_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
im_actions__action__Test_SendGoal_Response__Sequence__destroy(im_actions__action__Test_SendGoal_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    im_actions__action__Test_SendGoal_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
im_actions__action__Test_SendGoal_Response__Sequence__are_equal(const im_actions__action__Test_SendGoal_Response__Sequence * lhs, const im_actions__action__Test_SendGoal_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!im_actions__action__Test_SendGoal_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
im_actions__action__Test_SendGoal_Response__Sequence__copy(
  const im_actions__action__Test_SendGoal_Response__Sequence * input,
  im_actions__action__Test_SendGoal_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(im_actions__action__Test_SendGoal_Response);
    im_actions__action__Test_SendGoal_Response * data =
      (im_actions__action__Test_SendGoal_Response *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!im_actions__action__Test_SendGoal_Response__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          im_actions__action__Test_SendGoal_Response__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!im_actions__action__Test_SendGoal_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"

bool
im_actions__action__Test_GetResult_Request__init(im_actions__action__Test_GetResult_Request * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    im_actions__action__Test_GetResult_Request__fini(msg);
    return false;
  }
  return true;
}

void
im_actions__action__Test_GetResult_Request__fini(im_actions__action__Test_GetResult_Request * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
}

bool
im_actions__action__Test_GetResult_Request__are_equal(const im_actions__action__Test_GetResult_Request * lhs, const im_actions__action__Test_GetResult_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  return true;
}

bool
im_actions__action__Test_GetResult_Request__copy(
  const im_actions__action__Test_GetResult_Request * input,
  im_actions__action__Test_GetResult_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  return true;
}

im_actions__action__Test_GetResult_Request *
im_actions__action__Test_GetResult_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_GetResult_Request * msg = (im_actions__action__Test_GetResult_Request *)allocator.allocate(sizeof(im_actions__action__Test_GetResult_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(im_actions__action__Test_GetResult_Request));
  bool success = im_actions__action__Test_GetResult_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
im_actions__action__Test_GetResult_Request__destroy(im_actions__action__Test_GetResult_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    im_actions__action__Test_GetResult_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
im_actions__action__Test_GetResult_Request__Sequence__init(im_actions__action__Test_GetResult_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_GetResult_Request * data = NULL;

  if (size) {
    data = (im_actions__action__Test_GetResult_Request *)allocator.zero_allocate(size, sizeof(im_actions__action__Test_GetResult_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = im_actions__action__Test_GetResult_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        im_actions__action__Test_GetResult_Request__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
im_actions__action__Test_GetResult_Request__Sequence__fini(im_actions__action__Test_GetResult_Request__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      im_actions__action__Test_GetResult_Request__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

im_actions__action__Test_GetResult_Request__Sequence *
im_actions__action__Test_GetResult_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_GetResult_Request__Sequence * array = (im_actions__action__Test_GetResult_Request__Sequence *)allocator.allocate(sizeof(im_actions__action__Test_GetResult_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = im_actions__action__Test_GetResult_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
im_actions__action__Test_GetResult_Request__Sequence__destroy(im_actions__action__Test_GetResult_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    im_actions__action__Test_GetResult_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
im_actions__action__Test_GetResult_Request__Sequence__are_equal(const im_actions__action__Test_GetResult_Request__Sequence * lhs, const im_actions__action__Test_GetResult_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!im_actions__action__Test_GetResult_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
im_actions__action__Test_GetResult_Request__Sequence__copy(
  const im_actions__action__Test_GetResult_Request__Sequence * input,
  im_actions__action__Test_GetResult_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(im_actions__action__Test_GetResult_Request);
    im_actions__action__Test_GetResult_Request * data =
      (im_actions__action__Test_GetResult_Request *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!im_actions__action__Test_GetResult_Request__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          im_actions__action__Test_GetResult_Request__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!im_actions__action__Test_GetResult_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `result`
// already included above
// #include "im_actions/action/detail/test__functions.h"

bool
im_actions__action__Test_GetResult_Response__init(im_actions__action__Test_GetResult_Response * msg)
{
  if (!msg) {
    return false;
  }
  // status
  // result
  if (!im_actions__action__Test_Result__init(&msg->result)) {
    im_actions__action__Test_GetResult_Response__fini(msg);
    return false;
  }
  return true;
}

void
im_actions__action__Test_GetResult_Response__fini(im_actions__action__Test_GetResult_Response * msg)
{
  if (!msg) {
    return;
  }
  // status
  // result
  im_actions__action__Test_Result__fini(&msg->result);
}

bool
im_actions__action__Test_GetResult_Response__are_equal(const im_actions__action__Test_GetResult_Response * lhs, const im_actions__action__Test_GetResult_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // status
  if (lhs->status != rhs->status) {
    return false;
  }
  // result
  if (!im_actions__action__Test_Result__are_equal(
      &(lhs->result), &(rhs->result)))
  {
    return false;
  }
  return true;
}

bool
im_actions__action__Test_GetResult_Response__copy(
  const im_actions__action__Test_GetResult_Response * input,
  im_actions__action__Test_GetResult_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // status
  output->status = input->status;
  // result
  if (!im_actions__action__Test_Result__copy(
      &(input->result), &(output->result)))
  {
    return false;
  }
  return true;
}

im_actions__action__Test_GetResult_Response *
im_actions__action__Test_GetResult_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_GetResult_Response * msg = (im_actions__action__Test_GetResult_Response *)allocator.allocate(sizeof(im_actions__action__Test_GetResult_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(im_actions__action__Test_GetResult_Response));
  bool success = im_actions__action__Test_GetResult_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
im_actions__action__Test_GetResult_Response__destroy(im_actions__action__Test_GetResult_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    im_actions__action__Test_GetResult_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
im_actions__action__Test_GetResult_Response__Sequence__init(im_actions__action__Test_GetResult_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_GetResult_Response * data = NULL;

  if (size) {
    data = (im_actions__action__Test_GetResult_Response *)allocator.zero_allocate(size, sizeof(im_actions__action__Test_GetResult_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = im_actions__action__Test_GetResult_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        im_actions__action__Test_GetResult_Response__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
im_actions__action__Test_GetResult_Response__Sequence__fini(im_actions__action__Test_GetResult_Response__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      im_actions__action__Test_GetResult_Response__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

im_actions__action__Test_GetResult_Response__Sequence *
im_actions__action__Test_GetResult_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_GetResult_Response__Sequence * array = (im_actions__action__Test_GetResult_Response__Sequence *)allocator.allocate(sizeof(im_actions__action__Test_GetResult_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = im_actions__action__Test_GetResult_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
im_actions__action__Test_GetResult_Response__Sequence__destroy(im_actions__action__Test_GetResult_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    im_actions__action__Test_GetResult_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
im_actions__action__Test_GetResult_Response__Sequence__are_equal(const im_actions__action__Test_GetResult_Response__Sequence * lhs, const im_actions__action__Test_GetResult_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!im_actions__action__Test_GetResult_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
im_actions__action__Test_GetResult_Response__Sequence__copy(
  const im_actions__action__Test_GetResult_Response__Sequence * input,
  im_actions__action__Test_GetResult_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(im_actions__action__Test_GetResult_Response);
    im_actions__action__Test_GetResult_Response * data =
      (im_actions__action__Test_GetResult_Response *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!im_actions__action__Test_GetResult_Response__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          im_actions__action__Test_GetResult_Response__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!im_actions__action__Test_GetResult_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


// Include directives for member types
// Member `goal_id`
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__functions.h"
// Member `feedback`
// already included above
// #include "im_actions/action/detail/test__functions.h"

bool
im_actions__action__Test_FeedbackMessage__init(im_actions__action__Test_FeedbackMessage * msg)
{
  if (!msg) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__init(&msg->goal_id)) {
    im_actions__action__Test_FeedbackMessage__fini(msg);
    return false;
  }
  // feedback
  if (!im_actions__action__Test_Feedback__init(&msg->feedback)) {
    im_actions__action__Test_FeedbackMessage__fini(msg);
    return false;
  }
  return true;
}

void
im_actions__action__Test_FeedbackMessage__fini(im_actions__action__Test_FeedbackMessage * msg)
{
  if (!msg) {
    return;
  }
  // goal_id
  unique_identifier_msgs__msg__UUID__fini(&msg->goal_id);
  // feedback
  im_actions__action__Test_Feedback__fini(&msg->feedback);
}

bool
im_actions__action__Test_FeedbackMessage__are_equal(const im_actions__action__Test_FeedbackMessage * lhs, const im_actions__action__Test_FeedbackMessage * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__are_equal(
      &(lhs->goal_id), &(rhs->goal_id)))
  {
    return false;
  }
  // feedback
  if (!im_actions__action__Test_Feedback__are_equal(
      &(lhs->feedback), &(rhs->feedback)))
  {
    return false;
  }
  return true;
}

bool
im_actions__action__Test_FeedbackMessage__copy(
  const im_actions__action__Test_FeedbackMessage * input,
  im_actions__action__Test_FeedbackMessage * output)
{
  if (!input || !output) {
    return false;
  }
  // goal_id
  if (!unique_identifier_msgs__msg__UUID__copy(
      &(input->goal_id), &(output->goal_id)))
  {
    return false;
  }
  // feedback
  if (!im_actions__action__Test_Feedback__copy(
      &(input->feedback), &(output->feedback)))
  {
    return false;
  }
  return true;
}

im_actions__action__Test_FeedbackMessage *
im_actions__action__Test_FeedbackMessage__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_FeedbackMessage * msg = (im_actions__action__Test_FeedbackMessage *)allocator.allocate(sizeof(im_actions__action__Test_FeedbackMessage), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(im_actions__action__Test_FeedbackMessage));
  bool success = im_actions__action__Test_FeedbackMessage__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
im_actions__action__Test_FeedbackMessage__destroy(im_actions__action__Test_FeedbackMessage * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    im_actions__action__Test_FeedbackMessage__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
im_actions__action__Test_FeedbackMessage__Sequence__init(im_actions__action__Test_FeedbackMessage__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_FeedbackMessage * data = NULL;

  if (size) {
    data = (im_actions__action__Test_FeedbackMessage *)allocator.zero_allocate(size, sizeof(im_actions__action__Test_FeedbackMessage), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = im_actions__action__Test_FeedbackMessage__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        im_actions__action__Test_FeedbackMessage__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
im_actions__action__Test_FeedbackMessage__Sequence__fini(im_actions__action__Test_FeedbackMessage__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      im_actions__action__Test_FeedbackMessage__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

im_actions__action__Test_FeedbackMessage__Sequence *
im_actions__action__Test_FeedbackMessage__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  im_actions__action__Test_FeedbackMessage__Sequence * array = (im_actions__action__Test_FeedbackMessage__Sequence *)allocator.allocate(sizeof(im_actions__action__Test_FeedbackMessage__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = im_actions__action__Test_FeedbackMessage__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
im_actions__action__Test_FeedbackMessage__Sequence__destroy(im_actions__action__Test_FeedbackMessage__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    im_actions__action__Test_FeedbackMessage__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
im_actions__action__Test_FeedbackMessage__Sequence__are_equal(const im_actions__action__Test_FeedbackMessage__Sequence * lhs, const im_actions__action__Test_FeedbackMessage__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!im_actions__action__Test_FeedbackMessage__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
im_actions__action__Test_FeedbackMessage__Sequence__copy(
  const im_actions__action__Test_FeedbackMessage__Sequence * input,
  im_actions__action__Test_FeedbackMessage__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(im_actions__action__Test_FeedbackMessage);
    im_actions__action__Test_FeedbackMessage * data =
      (im_actions__action__Test_FeedbackMessage *)realloc(output->data, allocation_size);
    if (!data) {
      return false;
    }
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!im_actions__action__Test_FeedbackMessage__init(&data[i])) {
        /* free currently allocated and return false */
        for (; i-- > output->capacity; ) {
          im_actions__action__Test_FeedbackMessage__fini(&data[i]);
        }
        free(data);
        return false;
      }
    }
    output->data = data;
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!im_actions__action__Test_FeedbackMessage__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
