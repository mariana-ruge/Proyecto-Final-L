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
    | trigFunction
    | plotStatement
    | randomStatement
    ;

printStatement: 'print' '(' expression ')' ;

plotTrig: 'plotTrig' '(' trigFunction (',' trigFunction)* ',' range ')' ;

expression
    : primaryExpression
    | expression '^' expression
    | expression ('*' | '/' | '%') expression
    | expression ('+' | '-') expression
    | list 
    | trigFunction
    | NUMBER
    ;

list
    : '[' (expression (',' expression)*)? ']'  // Define a list of expressions
    ;


primaryExpression
    : literal
    | ID
    | matrixAccess
    | functionCall
    | '(' expression ')'
    ;

trigFunction
    : ('sin' | 'cos' | 'tan' | 'asin' | 'acos' | 'atan') '(' expression ')'
    | 'plt' '.' ('plot' | 'scatter' | 'show' | 'figure' | 'savefig') '(' expression (',' expression)* ')'
    ;

range
    : expression '..' expression
    | 'range' '(' expression ',' expression ')'
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
    : 'while' '(' comparisonExpression ')' '{' statement* '}'
    ;

forLoop
    : 'for' variable 'in' range (',' 'step' '=' expression)? '{' statement* '}'
    ;

fileStatement
    : 'read' '(' STRING ')'
    | 'write' '(' STRING ',' expression ')'
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

randomStatement
    : 'random' '(' (expression (',' expression)?)? ')'
    ;

regresionStatement
    : 'regresion' '(' expression ',' expression ')'
    ;

perceptronStatement
    : 'perceptron' '(' (statement | expression) ')'
    ;

functionCall
    : ID '(' expression (',' expression)* ')'
    ;

literal
    : NUMBER
    | STRING
    ;

plotStatement
    : 'plotTrig' '(' trigFunction (',' trigFunction)* ',' range ')'
    ;

NUMBER: [0-9]+ ('.' [0-9]+)?;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;
COMMENT: '#' ~[\r\n]* -> skip;
