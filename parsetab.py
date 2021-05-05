
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BOOL COLON COMMA COMMENT DEF DEFINITION DOT EQUAL IDENT INPUT LBRACKET LONGCOMMENT LPAREN MAPPING MATH MULTIPLE NEWLINE NUMBER PREFERENCE RBRACKET REQUIRED RPAREN SECTION STRING\n        program : program NEWLINE funcDef\n                | funcDef\n    \n        program : program NEWLINE prefBlock\n                | prefBlock\n                | notNeededBlock\n                | program NEWLINE notNeededBlock\n    \n        notNeededBlock : DEFINITION LPAREN error RPAREN\n                       | MAPPING LBRACKET error RBRACKET\n    funcDef : DEF IDENT LPAREN paramlist RPAREN LBRACKET stmtList RBRACKET NEWLINE\n            | DEF IDENT LPAREN RPAREN LBRACKET stmtList RBRACKET NEWLINE\n    prefBlock : PREFERENCE LBRACKET sectionblocklist RBRACKET NEWLINEsectionblocklist : sectionblock\n            | sectionblocklist NEWLINE sectionblocksectionblock : SECTION LPAREN STRING RPAREN LBRACKET blockparamlist RBRACKET NEWLINEblockparamlist : blockparamlist COMMA blockparam\n            | blockparamblockparam : INPUT STRING\n                | STRING\n                | MULTIPLE COLON BOOL\n                | REQUIRED COLON BOOLstmtList : stmtList NEWLINE stmt\n            | stmt \n            | stmtList stmtstmt : functionCall\n         | functionWithObjstmt : error NEWLINEfunctionCall : IDENT LPAREN paramlist RPAREN\n                | IDENT LPAREN RPARENfunctionCall : IDENT error NEWLINE\n                    | IDENT LPAREN error NEWLINEfunctionWithObj : IDENT DOT functionCallfunctionWithObj : IDENT DOT error NEWLINEparamlist : paramlist COMMA param\n                | paramparam : identparam\n            | strparam\n            | numparam identparam : IDENT\n                | IDENT NEWLINE\n                | NEWLINE IDENTstrparam : STRING\n            | STRING NEWLINE\n            | NEWLINE STRINGnumparam : NUMBER\n            | NUMBER NEWLINE\n            | NEWLINE NUMBER'
    
_lr_action_items = {'DEF':([0,9,],[5,5,]),'PREFERENCE':([0,9,],[6,6,]),'DEFINITION':([0,9,],[7,7,]),'MAPPING':([0,9,],[8,8,]),'$end':([1,2,3,4,14,15,16,36,37,47,76,84,],[0,-2,-4,-5,-1,-3,-6,-7,-8,-11,-10,-9,]),'NEWLINE':([1,2,3,4,14,15,16,17,18,19,23,31,32,33,36,37,40,47,48,53,54,55,56,57,59,60,61,63,65,66,68,70,71,72,74,75,76,77,84,85,86,87,88,93,],[9,-2,-4,-5,-1,-3,-6,26,34,-12,38,45,46,47,-7,-8,26,-11,-13,64,-22,-24,-25,66,64,26,72,76,-23,-26,84,-28,86,-29,-31,87,-10,-21,-9,-27,-30,-32,93,-14,]),'IDENT':([5,17,26,40,41,50,53,54,55,56,59,60,62,64,65,66,70,72,74,77,85,86,87,],[10,23,42,23,52,52,52,-22,-24,-25,52,23,73,52,-23,-26,-28,-29,-31,-21,-27,-30,-32,]),'LBRACKET':([6,8,25,39,58,],[11,13,41,50,67,]),'LPAREN':([7,10,20,52,73,],[12,17,35,60,60,]),'SECTION':([11,34,],[20,20,]),'error':([12,13,41,50,52,53,54,55,56,59,60,62,64,65,66,70,72,73,74,77,85,86,87,],[21,22,57,57,61,57,-22,-24,-25,57,71,75,57,-23,-26,-28,-29,61,-31,-21,-27,-30,-32,]),'RPAREN':([17,21,23,24,27,28,29,30,31,32,38,42,43,44,45,46,49,51,60,69,],[25,36,-38,39,-34,-35,-36,-37,-41,-44,-39,-40,-43,-46,-42,-45,58,-33,70,85,]),'STRING':([17,26,35,40,60,67,81,89,],[31,43,49,31,31,78,90,78,]),'NUMBER':([17,26,40,60,],[32,44,32,32,]),'RBRACKET':([18,19,22,48,53,54,55,56,59,65,66,70,72,74,77,78,79,80,85,86,87,90,93,94,95,96,],[33,-12,37,-13,63,-22,-24,-25,68,-23,-26,-28,-29,-31,-21,-18,88,-16,-27,-30,-32,-17,-14,-15,-19,-20,]),'COMMA':([23,24,27,28,29,30,31,32,38,42,43,44,45,46,51,69,78,79,80,90,94,95,96,],[-38,40,-34,-35,-36,-37,-41,-44,-39,-40,-43,-46,-42,-45,-33,40,-18,89,-16,-17,-15,-19,-20,]),'DOT':([52,],[62,]),'INPUT':([67,89,],[81,81,]),'MULTIPLE':([67,89,],[82,82,]),'REQUIRED':([67,89,],[83,83,]),'COLON':([82,83,],[91,92,]),'BOOL':([91,92,],[95,96,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'funcDef':([0,9,],[2,14,]),'prefBlock':([0,9,],[3,15,]),'notNeededBlock':([0,9,],[4,16,]),'sectionblocklist':([11,],[18,]),'sectionblock':([11,34,],[19,48,]),'paramlist':([17,60,],[24,69,]),'param':([17,40,60,],[27,51,27,]),'identparam':([17,40,60,],[28,28,28,]),'strparam':([17,40,60,],[29,29,29,]),'numparam':([17,40,60,],[30,30,30,]),'stmtList':([41,50,],[53,59,]),'stmt':([41,50,53,59,64,],[54,54,65,65,77,]),'functionCall':([41,50,53,59,62,64,],[55,55,55,55,74,55,]),'functionWithObj':([41,50,53,59,64,],[56,56,56,56,56,]),'blockparamlist':([67,],[79,]),'blockparam':([67,89,],[80,94,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program NEWLINE funcDef','program',3,'p_program_funcDef','parsefile.py',7),
  ('program -> funcDef','program',1,'p_program_funcDef','parsefile.py',8),
  ('program -> program NEWLINE prefBlock','program',3,'p_program_block','parsefile.py',18),
  ('program -> prefBlock','program',1,'p_program_block','parsefile.py',19),
  ('program -> notNeededBlock','program',1,'p_program_block','parsefile.py',20),
  ('program -> program NEWLINE notNeededBlock','program',3,'p_program_block','parsefile.py',21),
  ('notNeededBlock -> DEFINITION LPAREN error RPAREN','notNeededBlock',4,'p_notNeededBlock','parsefile.py',31),
  ('notNeededBlock -> MAPPING LBRACKET error RBRACKET','notNeededBlock',4,'p_notNeededBlock','parsefile.py',32),
  ('funcDef -> DEF IDENT LPAREN paramlist RPAREN LBRACKET stmtList RBRACKET NEWLINE','funcDef',9,'p_funcDef','parsefile.py',37),
  ('funcDef -> DEF IDENT LPAREN RPAREN LBRACKET stmtList RBRACKET NEWLINE','funcDef',8,'p_funcDef','parsefile.py',38),
  ('prefBlock -> PREFERENCE LBRACKET sectionblocklist RBRACKET NEWLINE','prefBlock',5,'p_prefBlock','parsefile.py',46),
  ('sectionblocklist -> sectionblock','sectionblocklist',1,'p_sectionblocklist','parsefile.py',50),
  ('sectionblocklist -> sectionblocklist NEWLINE sectionblock','sectionblocklist',3,'p_sectionblocklist','parsefile.py',51),
  ('sectionblock -> SECTION LPAREN STRING RPAREN LBRACKET blockparamlist RBRACKET NEWLINE','sectionblock',8,'p_sectionblock','parsefile.py',59),
  ('blockparamlist -> blockparamlist COMMA blockparam','blockparamlist',3,'p_blockparamlist','parsefile.py',63),
  ('blockparamlist -> blockparam','blockparamlist',1,'p_blockparamlist','parsefile.py',64),
  ('blockparam -> INPUT STRING','blockparam',2,'p_blockparam','parsefile.py',72),
  ('blockparam -> STRING','blockparam',1,'p_blockparam','parsefile.py',73),
  ('blockparam -> MULTIPLE COLON BOOL','blockparam',3,'p_blockparam','parsefile.py',74),
  ('blockparam -> REQUIRED COLON BOOL','blockparam',3,'p_blockparam','parsefile.py',75),
  ('stmtList -> stmtList NEWLINE stmt','stmtList',3,'p_stmtList','parsefile.py',86),
  ('stmtList -> stmt','stmtList',1,'p_stmtList','parsefile.py',87),
  ('stmtList -> stmtList stmt','stmtList',2,'p_stmtList','parsefile.py',88),
  ('stmt -> functionCall','stmt',1,'p_stmt','parsefile.py',105),
  ('stmt -> functionWithObj','stmt',1,'p_stmt','parsefile.py',106),
  ('stmt -> error NEWLINE','stmt',2,'p_stmt_error','parsefile.py',110),
  ('functionCall -> IDENT LPAREN paramlist RPAREN','functionCall',4,'p_functionCall','parsefile.py',115),
  ('functionCall -> IDENT LPAREN RPAREN','functionCall',3,'p_functionCall','parsefile.py',116),
  ('functionCall -> IDENT error NEWLINE','functionCall',3,'p_functionCall_error','parsefile.py',123),
  ('functionCall -> IDENT LPAREN error NEWLINE','functionCall',4,'p_functionCall_error','parsefile.py',124),
  ('functionWithObj -> IDENT DOT functionCall','functionWithObj',3,'p_functionWithObj','parsefile.py',129),
  ('functionWithObj -> IDENT DOT error NEWLINE','functionWithObj',4,'p_functionWithObj_error','parsefile.py',133),
  ('paramlist -> paramlist COMMA param','paramlist',3,'p_paramlist','parsefile.py',138),
  ('paramlist -> param','paramlist',1,'p_paramlist','parsefile.py',139),
  ('param -> identparam','param',1,'p_param','parsefile.py',147),
  ('param -> strparam','param',1,'p_param','parsefile.py',148),
  ('param -> numparam','param',1,'p_param','parsefile.py',149),
  ('identparam -> IDENT','identparam',1,'p_identparam','parsefile.py',153),
  ('identparam -> IDENT NEWLINE','identparam',2,'p_identparam','parsefile.py',154),
  ('identparam -> NEWLINE IDENT','identparam',2,'p_identparam','parsefile.py',155),
  ('strparam -> STRING','strparam',1,'p_strparam','parsefile.py',162),
  ('strparam -> STRING NEWLINE','strparam',2,'p_strparam','parsefile.py',163),
  ('strparam -> NEWLINE STRING','strparam',2,'p_strparam','parsefile.py',164),
  ('numparam -> NUMBER','numparam',1,'p_numparam','parsefile.py',171),
  ('numparam -> NUMBER NEWLINE','numparam',2,'p_numparam','parsefile.py',172),
  ('numparam -> NEWLINE NUMBER','numparam',2,'p_numparam','parsefile.py',173),
]