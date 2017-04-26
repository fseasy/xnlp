#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Basic graph node.

'''
from weakref import WeakKeyDictionary

class GraphNode(object):
    '''
    basic graph node.
    '''
    def __init__(self, parents=()):
        self._cached_value = None
        # target-node => grad value
        self._cached_grad = WeakKeyDictionary()
        self._parents = parents
        # This node's children and this node's position
        # as to this child.
        # eg:
        # c = a / b,
        # c is the current node, and c has parents a, b;
        # when calculate difference, it is from parent to
        # child (that is , down to top) [in fact , it is a
        # recursive process, so actual order is from child to
        # parent.] when calc  \frac{\delta c}{\delta a}
        # it is better to kown a's position to get the
        # difference.
        # this value is maintained by it's child
        self._children_and_expr_position = (
            WeakKeyDictionary()
        )
        for position_in_expr, parent in enumerate(parents):
            parent.add_child_and_expr_position(
                self, position_in_expr
            )

    def add_child_and_expr_position(self, child, expr_pos):
        '''
        to add child and current node's position info in the expr
        '''
        self._children_and_expr_position[child] = expr_pos
    
    @property
    def children_and_expr_position(self):
        return self._children_and_expr_position.items()
    
    def get_value(self):
        '''
        get the node value.
        return the cached value if have, else do forward.
        '''
        if self._cached_value is None:
            self._cached_value = self._do_forward2get_value()
        return self._cached_value
    
    def _do_forward2get_value(self):
        '''
        do forward.
        '''
        raise NotImplementedError(("virtual function in base class "
                                   "{}").format(self.__class__))
    
    def calc_grad2some_node(self, node):
        '''
        do \frac{\delta self}{\delta node}
        use a recursive DFS search to get the grad.
        '''
        if node in self._cached_grad:
            return self._cached_grad[node]
        # edge condition
        if self == node:
            return 1 
        # calc from parent to child (node -> self)
        grad_value = 0
        node_children_pos = node.children_and_expr_position()
        # hidden edge condition:
        # if the node's current child has no way to self,
        # then this recursive will continues to go
        # until the last child is the final child (
        # no other children any more), then recursive 
        # ended, 0 is return.
        for child, pos in node_children_pos:
            to_child_grad = child.calc_grad2some_node(self)
            if to_child_grad != 0:
                child2node_grad = child.calc_expr_grad(pos)
            else:
                child2node_grad = 0
            current_branch_grad = to_child_grad * child2node_grad
            grad_value += current_branch_grad
        return grad_value
    
    def get_node_expr_grad(self, pos_in_expr):
        '''
        calc grad for every parameter in current expr.
        '''
        raise NotImplementedError(("virtual function in base class "
                                   "{}").format(self.__class__))
    