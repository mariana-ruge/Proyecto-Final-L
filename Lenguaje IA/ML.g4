grammar ML;

program: statement+ EOF;

statement
    : arithmeticStatement
    | matrixStatement
    | conditionalStatement
    | fileStatement
    | loopStatement
    | assignment
    | incrementStatement
    | regresionStatement
    | perceptronStatement
    ;

arithmeticStatement
    : 'calc' '(' expression ')'
    | 'predecir' '(' expression ')'
    ;

matrixStatement
    : 'matrix' ID '=' matrixOperation
    ;

assignment
    : variable '=' expression;

incrementStatement
    : variable incrementOp;

loopStatement
    : whileLoop
    | forLoop
    ;

whileLoop
    : 'while' comparisonExpression '{' statement* '}'
    ;

forLoop
    : 'for' variable 'in' range (',' 'step' '=' expression)? '{' statement* '}'
    ;


range
    : expression '..' expression
    ;

breakStatement
    : 'break'
    ;

conditionalStatement
    : 'if' '(' comparisonExpression ')' '{' statement* '}'
    ;

fileStatement
    : 'read' '(' STRING ')'
    | 'write' '(' STRING ',' expression ')'
    | 'print' '(' STRING ',' expression ')'
    ;

comparisonExpression
    : expression compareOp expression
    ;

compareOp
    : '==' | '!=' | '<' | '<=' | '>' | '>='
    ;

expression
    : expression '^' expression                             // PowerExpression
    | expression ('*' | '/' | '%') expression                // MultiplicativeExpression
    | expression ('+' | '-') expression                      // AdditiveExpression
    | ID '(' expression (',' expression)* ')'                // FunctionCallExpression
    | '(' expression ')'                                     // ParenthesizedExpression
    | NUMBER                                                 // NumberExpression
    | variable                                               // VariableExpression
    | 'raiz' '(' expression ',' expression ')'               // RootExpression
    | matrix                                                 // MatrixExpression
    ;

matrix
    : '[' (expression (',' expression)*)? ']'  // Matrix as a list of expressions
    ;

matrixOperation
    : matrixFunction '(' matrix (',' matrix)* ')'
    ;

matrixFunction
    : 'add' | 'subtract' | 'multiply' | 'inverse' | 'transpose'
    ;

matrixAccess
    : ID '[' NUMBER ']'
    ;

matrixRow
    : NUMBER (',' NUMBER)*
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

NUMBER: [0-9]+ ('.' [0-9]+)?;
ID: [a-zA-Z_][a-zA-Z0-9_]*;
STRING: '"' .*? '"';
WS: [ \t\r\n]+ -> skip;

COMMENT: '#' ~[\r\n]* -> skip;
