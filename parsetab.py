
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ARRAY BOOL COLON COMMA COMMENT DEF DEFINITION DOT EQUAL IDENT ILBRACKET INPUT IRBRACKET LBRACKET LONGCOMMENT LPAREN MAPPING MATH MULTIPLE NEWLINE NUMBER PREFERENCE RBRACKET REQUIRED RPAREN SECTION STRING TITLE\n            program : program funcDef\n                    | funcDef\n        \n            program : program prefBlock\n                    | prefBlock\n                    | notNeededBlock\n                    | program notNeededBlock\n        \n            notNeededBlock : DEFINITION LPAREN error RPAREN\n                        | MAPPING LBRACKET error RBRACKET\n        funcDef : DEF IDENT LPAREN paramlist RPAREN LBRACKET stmtList RBRACKET\n                | DEF IDENT LPAREN RPAREN LBRACKET stmtList RBRACKET\n        prefBlock : PREFERENCE LBRACKET sectionblocklist RBRACKETsectionblocklist : sectionblock\n                | sectionblocklist NEWLINE sectionblock\n                | sectionblocklist NEWLINEsectionblock : SECTION LPAREN STRING RPAREN ILBRACKET blockparamlist IRBRACKETblockparamlist : blockparamlist COMMA blockparam\n                | blockparamblockparam : INPUT STRING\n                    | STRING\n                    | TITLE COLON STRING\n                    | MULTIPLE COLON BOOL\n                    | REQUIRED COLON BOOLstmtList : stmtList NEWLINEstmtList : stmtList NEWLINE stmt\n                | stmt \n                | stmtList stmtstmt : functionCall\n            | functionWithObjstmt : error NEWLINEfunctionCall : IDENT LPAREN paramlist RPAREN\n                    | IDENT LPAREN RPARENfunctionCall : IDENT LPAREN error NEWLINE\n                    | IDENT error NEWLINEfunctionWithObj : IDENT DOT functionCallfunctionWithObj : IDENT DOT error NEWLINEparamlist : paramlist COMMA param\n                    | paramparam : identparam\n                | strparam\n                | numparam identparam : IDENT\n                    | IDENT NEWLINE\n                    | NEWLINE IDENTstrparam : STRING\n                | STRING NEWLINE\n                | NEWLINE STRINGnumparam : NUMBER\n                | NUMBER NEWLINE\n                | NEWLINE NUMBER'
    
_lr_action_items = {'DEF':([0,1,2,3,4,9,10,11,32,35,36,61,66,],[5,5,-2,-4,-5,-1,-3,-6,-11,-7,-8,-10,-9,]),'PREFERENCE':([0,1,2,3,4,9,10,11,32,35,36,61,66,],[6,6,-2,-4,-5,-1,-3,-6,-11,-7,-8,-10,-9,]),'DEFINITION':([0,1,2,3,4,9,10,11,32,35,36,61,66,],[7,7,-2,-4,-5,-1,-3,-6,-11,-7,-8,-10,-9,]),'MAPPING':([0,1,2,3,4,9,10,11,32,35,36,61,66,],[8,8,-2,-4,-5,-1,-3,-6,-11,-7,-8,-10,-9,]),'$end':([1,2,3,4,9,10,11,32,35,36,61,66,],[0,-2,-4,-5,-1,-3,-6,-11,-7,-8,-10,-9,]),'IDENT':([5,16,29,39,40,48,51,52,53,54,57,58,60,62,63,64,68,70,72,74,82,83,84,],[12,22,41,22,50,50,50,-25,-27,-28,50,22,71,50,-26,-29,-31,-33,-34,-24,-30,-32,-35,]),'LBRACKET':([6,8,24,38,],[13,15,40,48,]),'LPAREN':([7,12,19,50,71,],[14,16,34,58,58,]),'SECTION':([13,33,],[19,19,]),'error':([14,15,40,48,50,51,52,53,54,57,58,60,62,63,64,68,70,71,72,74,82,83,84,],[20,21,55,55,59,55,-25,-27,-28,55,69,73,55,-26,-29,-31,-33,59,-34,-24,-30,-32,-35,]),'RPAREN':([16,20,22,23,25,26,27,28,30,31,37,41,42,43,44,45,47,49,58,67,],[24,35,-41,38,-37,-38,-39,-40,-44,-47,-42,-43,-46,-49,-45,-48,56,-36,68,82,]),'NEWLINE':([16,17,18,22,30,31,33,39,46,51,52,53,54,55,57,58,59,62,63,64,68,69,70,72,73,74,82,83,84,85,],[29,33,-12,37,44,45,-14,29,-13,62,-25,-27,-28,64,62,29,70,-23,-26,-29,-31,83,-33,-34,84,-24,-30,-32,-35,-15,]),'STRING':([16,29,34,39,58,65,78,86,88,],[30,42,47,30,30,75,87,75,92,]),'NUMBER':([16,29,39,58,],[31,43,31,31,]),'RBRACKET':([17,18,21,33,46,51,52,53,54,57,62,63,64,68,70,72,74,82,83,84,85,],[32,-12,36,-14,-13,61,-25,-27,-28,66,-23,-26,-29,-31,-33,-34,-24,-30,-32,-35,-15,]),'COMMA':([22,23,25,26,27,28,30,31,37,41,42,43,44,45,49,67,75,76,77,87,91,92,93,94,],[-41,39,-37,-38,-39,-40,-44,-47,-42,-43,-46,-49,-45,-48,-36,39,-19,86,-17,-18,-16,-20,-21,-22,]),'DOT':([50,],[60,]),'ILBRACKET':([56,],[65,]),'INPUT':([65,86,],[78,78,]),'TITLE':([65,86,],[79,79,]),'MULTIPLE':([65,86,],[80,80,]),'REQUIRED':([65,86,],[81,81,]),'IRBRACKET':([75,76,77,87,91,92,93,94,],[-19,85,-17,-18,-16,-20,-21,-22,]),'COLON':([79,80,81,],[88,89,90,]),'BOOL':([89,90,],[93,94,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'program':([0,],[1,]),'funcDef':([0,1,],[2,9,]),'prefBlock':([0,1,],[3,10,]),'notNeededBlock':([0,1,],[4,11,]),'sectionblocklist':([13,],[17,]),'sectionblock':([13,33,],[18,46,]),'paramlist':([16,58,],[23,67,]),'param':([16,39,58,],[25,49,25,]),'identparam':([16,39,58,],[26,26,26,]),'strparam':([16,39,58,],[27,27,27,]),'numparam':([16,39,58,],[28,28,28,]),'stmtList':([40,48,],[51,57,]),'stmt':([40,48,51,57,62,],[52,52,63,63,74,]),'functionCall':([40,48,51,57,60,62,],[53,53,53,53,72,53,]),'functionWithObj':([40,48,51,57,62,],[54,54,54,54,54,]),'blockparamlist':([65,],[76,]),'blockparam':([65,86,],[77,91,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> program","S'",1,None,None,None),
  ('program -> program funcDef','program',2,'p_program_funcDef','parsefile.py',9),
  ('program -> funcDef','program',1,'p_program_funcDef','parsefile.py',10),
  ('program -> program prefBlock','program',2,'p_program_block','parsefile.py',23),
  ('program -> prefBlock','program',1,'p_program_block','parsefile.py',24),
  ('program -> notNeededBlock','program',1,'p_program_block','parsefile.py',25),
  ('program -> program notNeededBlock','program',2,'p_program_block','parsefile.py',26),
  ('notNeededBlock -> DEFINITION LPAREN error RPAREN','notNeededBlock',4,'p_notNeededBlock','parsefile.py',39),
  ('notNeededBlock -> MAPPING LBRACKET error RBRACKET','notNeededBlock',4,'p_notNeededBlock','parsefile.py',40),
  ('funcDef -> DEF IDENT LPAREN paramlist RPAREN LBRACKET stmtList RBRACKET','funcDef',8,'p_funcDef','parsefile.py',45),
  ('funcDef -> DEF IDENT LPAREN RPAREN LBRACKET stmtList RBRACKET','funcDef',7,'p_funcDef','parsefile.py',46),
  ('prefBlock -> PREFERENCE LBRACKET sectionblocklist RBRACKET','prefBlock',4,'p_prefBlock','parsefile.py',54),
  ('sectionblocklist -> sectionblock','sectionblocklist',1,'p_sectionblocklist','parsefile.py',58),
  ('sectionblocklist -> sectionblocklist NEWLINE sectionblock','sectionblocklist',3,'p_sectionblocklist','parsefile.py',59),
  ('sectionblocklist -> sectionblocklist NEWLINE','sectionblocklist',2,'p_sectionblocklist','parsefile.py',60),
  ('sectionblock -> SECTION LPAREN STRING RPAREN ILBRACKET blockparamlist IRBRACKET','sectionblock',7,'p_sectionblock','parsefile.py',70),
  ('blockparamlist -> blockparamlist COMMA blockparam','blockparamlist',3,'p_blockparamlist','parsefile.py',74),
  ('blockparamlist -> blockparam','blockparamlist',1,'p_blockparamlist','parsefile.py',75),
  ('blockparam -> INPUT STRING','blockparam',2,'p_blockparam','parsefile.py',83),
  ('blockparam -> STRING','blockparam',1,'p_blockparam','parsefile.py',84),
  ('blockparam -> TITLE COLON STRING','blockparam',3,'p_blockparam','parsefile.py',85),
  ('blockparam -> MULTIPLE COLON BOOL','blockparam',3,'p_blockparam','parsefile.py',86),
  ('blockparam -> REQUIRED COLON BOOL','blockparam',3,'p_blockparam','parsefile.py',87),
  ('stmtList -> stmtList NEWLINE','stmtList',2,'p_stmtList_withNewline','parsefile.py',100),
  ('stmtList -> stmtList NEWLINE stmt','stmtList',3,'p_stmtList','parsefile.py',104),
  ('stmtList -> stmt','stmtList',1,'p_stmtList','parsefile.py',105),
  ('stmtList -> stmtList stmt','stmtList',2,'p_stmtList','parsefile.py',106),
  ('stmt -> functionCall','stmt',1,'p_stmt','parsefile.py',124),
  ('stmt -> functionWithObj','stmt',1,'p_stmt','parsefile.py',125),
  ('stmt -> error NEWLINE','stmt',2,'p_stmt_error','parsefile.py',132),
  ('functionCall -> IDENT LPAREN paramlist RPAREN','functionCall',4,'p_functionCall','parsefile.py',137),
  ('functionCall -> IDENT LPAREN RPAREN','functionCall',3,'p_functionCall','parsefile.py',138),
  ('functionCall -> IDENT LPAREN error NEWLINE','functionCall',4,'p_functionCall_error','parsefile.py',145),
  ('functionCall -> IDENT error NEWLINE','functionCall',3,'p_functionCall_error','parsefile.py',146),
  ('functionWithObj -> IDENT DOT functionCall','functionWithObj',3,'p_functionWithObj','parsefile.py',151),
  ('functionWithObj -> IDENT DOT error NEWLINE','functionWithObj',4,'p_functionWithObj_error','parsefile.py',158),
  ('paramlist -> paramlist COMMA param','paramlist',3,'p_paramlist','parsefile.py',163),
  ('paramlist -> param','paramlist',1,'p_paramlist','parsefile.py',164),
  ('param -> identparam','param',1,'p_param','parsefile.py',172),
  ('param -> strparam','param',1,'p_param','parsefile.py',173),
  ('param -> numparam','param',1,'p_param','parsefile.py',174),
  ('identparam -> IDENT','identparam',1,'p_identparam','parsefile.py',178),
  ('identparam -> IDENT NEWLINE','identparam',2,'p_identparam','parsefile.py',179),
  ('identparam -> NEWLINE IDENT','identparam',2,'p_identparam','parsefile.py',180),
  ('strparam -> STRING','strparam',1,'p_strparam','parsefile.py',187),
  ('strparam -> STRING NEWLINE','strparam',2,'p_strparam','parsefile.py',188),
  ('strparam -> NEWLINE STRING','strparam',2,'p_strparam','parsefile.py',189),
  ('numparam -> NUMBER','numparam',1,'p_numparam','parsefile.py',196),
  ('numparam -> NUMBER NEWLINE','numparam',2,'p_numparam','parsefile.py',197),
  ('numparam -> NEWLINE NUMBER','numparam',2,'p_numparam','parsefile.py',198),
]
