from typing import Any, Union, Optional
from typing_extensions import Self

class LLNode:
  _data: Any
  _next: Union[Self, None]

  def __init__(self, data):
    self._data = data
    self._next = None
  
  def get_data(self) -> Any:
    return self._data
  
  def set_data(self, new_data: Any) -> None:
    self.data = new_data

  def get_next(self) -> Self:
    return self._next

  def set_next(self, new_node: Self) -> None:
    if not self._next:
      self._next = new_node

class LinkedList:
  _head_node: Union[LLNode, None]
  _tail_node: Union[LLNode, None]

  def __init__(self, data: Optional[Any] = None):
    self._head_node = None
    self._tail_node = None

    if data:
      self.push(data)
  
  def get_head(self) -> Union[LLNode, None]:
    return self._head_node
  
  def get_tail(self) -> Union[LLNode, None]:
    return self._tail_node

  def push(self, data: Any) -> None:
    """ Sets a new node with given value to
    the beginning of the list
    """

    # The first node case
    if not self._head_node:
      self._head_node = LLNode(data)
      self._tail_node = self._head_node
      return
    
    new_node = LLNode(data)
    new_node.set_next(self._head_node)
    self._head_node = new_node
  
  def append(self, data: Any) -> None:
    """ Sets a node with given value
    to the tail of the list 
    """

    # The first node case
    if not self._head_node:
      self.push(data)
      return
    
    new_node: LLNode = LLNode(data)
    self._tail_node.set_next(new_node)
    self._tail_node = self._tail_node.get_next()
  
  def log(self, curr_node: Union[LLNode, None]):
    """ Recursive method that prints all list's
    node values starting from 'curr_node' 
    """
    if curr_node:
      print(curr_node.get_data())
      self.log(curr_node.get_next())
    else:
      return