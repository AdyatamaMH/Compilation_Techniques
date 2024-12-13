
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'DASH DOT SLASHmessage : wordswords : words word\n             | wordword : morse SLASH\n            | morsemorse : morse DOT\n             | morse DASH\n             | DOT\n             | DASH'
    
_lr_action_items = {'DOT':([0,2,3,4,5,6,7,8,9,10,],[5,5,-3,9,-8,-9,-2,-4,-6,-7,]),'DASH':([0,2,3,4,5,6,7,8,9,10,],[6,6,-3,10,-8,-9,-2,-4,-6,-7,]),'$end':([1,2,3,4,5,6,7,8,9,10,],[0,-1,-3,-5,-8,-9,-2,-4,-6,-7,]),'SLASH':([4,5,6,9,10,],[8,-8,-9,-6,-7,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'message':([0,],[1,]),'words':([0,],[2,]),'word':([0,2,],[3,7,]),'morse':([0,2,],[4,4,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> message","S'",1,None,None,None),
  ('message -> words','message',1,'p_message','lexer_parser.py',28),
  ('words -> words word','words',2,'p_words','lexer_parser.py',32),
  ('words -> word','words',1,'p_words','lexer_parser.py',33),
  ('word -> morse SLASH','word',2,'p_word','lexer_parser.py',39),
  ('word -> morse','word',1,'p_word','lexer_parser.py',40),
  ('morse -> morse DOT','morse',2,'p_morse','lexer_parser.py',44),
  ('morse -> morse DASH','morse',2,'p_morse','lexer_parser.py',45),
  ('morse -> DOT','morse',1,'p_morse','lexer_parser.py',46),
  ('morse -> DASH','morse',1,'p_morse','lexer_parser.py',47),
]