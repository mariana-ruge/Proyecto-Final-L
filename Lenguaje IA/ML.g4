grammar ML;

program: statement+ EOF;

statement
    : arithmeticStatement
    | matrixStatement
    | fileStatement
    | loopStatement
    | assignment
    | incrementStatement
    | regresionStatement
    | perceptronStatement
    | matrixAccess
    | printStatement
    | condicionalStatement
    ;

printStatement: 'print' '(' expression ')' ;

literal
    : NUMBER
    | STRING
    ;

arithmeticStatement
    : 'calc' '(' expression ')'
    | 'predecir' '(' expression ')'
    ;

matrixStatement
    : 'matrix' ID '=' (matrix | matrixOperation)
    ;

assignment
    : variable '=' expression
    ;

incrementStatement
    : variable incrementOp
    ;

loopStatement
    : whileLoop
    | forLoop
    ;

condicionalStatement
    : ifStatement
    | ifElseStatement
    | ifElseIfStatement
    ;

ifStatement
    : 'if' '(' comparisonExpression ')' '{' statement* '}'
    ;

ifElseStatement
    : 'if' '(' comparisonExpression ')' '{' statement* '}' 'else' '{' statement* '}'
    ;

ifElseIfStatement
    : 'if' '(' comparisonExpression ')' '{' statement* '}' 
      ('else' 'if' '(' comparisonExpression ')' '{' statement* '}')* 
      ('else' '{' statement* '}')?
    ;

whileLoop
    : 'while' expression '{' statement* '}'
    ;

forLoop
    : 'for' variable 'in' range (',' 'step' '=' expression)? '{' statement* '}'
    ;

range
    : expression '..' expression
    ;

fileStatement
    : 'read' '(' STRING ')'
    | 'write' '(' STRING ',' expression ')'
    | 'print' '(' STRING ',' expression ')'
    ;

expression
    : primaryExpression
    | expression '^' expression
    | expression ('*' | '/' | '%') expression
    | expression ('+' | '-') expression
    ;

comparisonExpression
    : primaryExpression compareOp primaryExpression
    | comparisonExpression '&&' comparisonExpression
    | comparisonExpression '||' comparisonExpression
    ;

compareOp
    : '==' | '!=' | '<' | '<=' | '>' | '>='
    ;

matrix
    : '[' (expression (',' expression)*)? ']'  // Matriz de expresiones
    ;

matrixOperation
    : matrixFunction '(' matrix (',' matrix)* ')'
    ;

matrixFunction
    : 'add' | 'subtract' | 'multiply' | 'inverse' | 'transpose'
    ;

matrixAccess
    : ID '[' expression ']'
    ;

incrementOp
    : '++' | '--'
    ;

variable
    : ID
    ;

regresionStatement
    : 'regresion' '(' expression ',' expression ')'
    ;

perceptronStatement
    : 'perceptron' '(' (statement | expression) ')'
    ;

primaryExpression
    : literal
    | ID
    | matrixAccess
    | functionCall
    | '(' expression ')'
    ;

functionCall
    : ID '(' expression (',' expression)* ')'
    ;

NUMBER: [0-9]+ ('.' [0-9]+)?;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;