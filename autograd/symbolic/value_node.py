#/usr/bin/env python
#! -*- coding: utf-8 -*-
'''
value node, including 
    input node,
    output node,
    parameter node.
'''

from graph_node import GraphNode

class ValueNode(GraphNode):

    def __init__(self, value=None):
        super(ValueNode, self).__init__()
        self._value = value
    
    def get_value(self):
        if self._value is None:
            raise ValueError("ValueNode's Value is None")
        return self._value
    
    @property
    def value(self):
        return self.get_value()
    
    @value.setter
    def value(self, value):
        self._value = value
    
    def _do_forward2get_value(self):
        raise NotImplementedError("ValueNode has no forward process.")
    
    def get_node_expr_grad(self, pos_in_expr):
        raise NotImplementedError("ValueNode has no grad")

Input = ValueNode
Output = ValueNode
Parameter = ValueNode