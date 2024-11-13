grammar MLDSL;

// Definición de reglas para el análisis léxico y sintáctico

// Tokens y Palabras Clave
MODEL   : 'modelo';
TRAIN   : 'entrenar';
DATA    : 'datos';
EVALUATE: 'evaluar';
IF      : 'if';
ELSE    : 'else';
FOR     : 'for';
DEF     : 'def';
RETURN  : 'return';

// Operadores
ASIG    : '=';
PLUS    : '+';
MINUS   : '-';
MULT    : '*';
DIV     : '/';
LT      : '<';
GT      : '>';
EQ      : '==';
LPAREN  : '(';
RPAREN  : ')';
LBRACE  : '{';
RBRACE  : '}';
COLON   : ':';
COMMA   : ',';
INDENT  : '    ';

// Identificadores y números
ID      : [a-zA-Z_][a-zA-Z_0-9]*;
INT     : [0-9]+;
FLOAT   : [0-9]+ '.' [0-9]+;

// Espacios y comentarios
WS      : [ \t\r\n]+ -> skip;
COMMENT : '#' ~[\r\n]* -> skip;

// Reglas de gramática (producciones)
program : statement+;

statement
    : model_definition
    | train_statement
    | evaluate_statement
    | if_statement
    | for_statement
    | function_definition
    | return_statement
    ;

model_definition : MODEL ID LPAREN RPAREN LBRACE statement* RBRACE;
train_statement  : TRAIN ID LPAREN DATA RPAREN;
evaluate_statement : EVALUATE ID LPAREN RPAREN;
if_statement     : IF LPAREN condition RPAREN COLON INDENT statement+ (DEDENT ELSE COLON INDENT statement+)? DEDENT;
for_statement    : FOR ID IN DATA COLON INDENT statement+ DEDENT;
function_definition : DEF ID LPAREN (ID (COMMA ID)*)? RPAREN COLON INDENT statement+ DEDENT;
return_statement : RETURN expression;

condition : expression (EQ | LT | GT) expression;
expression : INT | FLOAT | ID | LPAREN expression RPAREN (PLUS | MINUS | MULT | DIV expression)*;
