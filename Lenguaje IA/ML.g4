grammar ML;

program: statement+ EOF;

statement
    : arithmeticStatement
    | matrixStatement
    | conditionalStatement
    | loopStatement
    | fileStatement
    ;

arithmeticStatement
    : 'calc' '(' expression ')'
    ;

matrixStatement
    : 'matrix' ID '=' matrixOperation
    ;

conditionalStatement
    : 'if' '(' comparisonExpression ')' '{' statement* '}'
    ;

loopStatement
    : 'for' '(' variable 'in' range ')' '{' statement* '}'
    | 'while' '(' comparisonExpression ')' '{' statement* '}'
    ;

fileStatement
    : 'read' '(' STRING ')'
    | 'write' '(' STRING ',' expression ')'
    ;

comparisonExpression
    : expression compareOp expression
    ;

compareOp
    : '==' | '!=' | '<' | '<=' | '>' | '>='
    ;

expression
    : expression '^' expression                   # PowerExpression
    | expression ('*' | '/' | '%') expression    # MultiplicativeExpression
    | expression ('+' | '-') expression          # AdditiveExpression
    | '(' expression ')'                         # ParenthesizedExpression
    | NUMBER                                     # NumberExpression
    | variable                                   # VariableExpression
    | matrixAccess                               # MatrixAccessExpression
    ;

matrixOperation
    : matrixFunction '(' matrix (',' matrix)* ')'
    ;

matrixFunction
    : 'add' | 'subtract' | 'multiply' | 'inverse' | 'transpose'
    ;

matrix
    : '[' (NUMBER (',' NUMBER)*)? ']'
    ;

matrixAccess
    : ID '[' NUMBER ']'
    ;

variable
    : ID
    ;

range
    : NUMBER '..' NUMBER
    ;

NUMBER: [0-9]+('.'[0-9]+)?;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;