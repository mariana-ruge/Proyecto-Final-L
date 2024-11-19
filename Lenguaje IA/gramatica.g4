grammar gramatica;

options {
    language = Python3;
}

// Regla principal
program: statement*;

// Declaración de sentencias
statement
    : arithmetic_stmt
    | matrix_stmt
    | conditional_stmt
    | loop_stmt
    | graph_stmt
    | file_stmt
    | function_stmt
    | assignment_stmt
    ;

// Declaración de asignación
assignment_stmt: ID '=' expr;  // Corrected rule for assignment

// Declaración de operaciones aritméticas
arithmetic_stmt
    : expr ('+'|'-'|'*'|'/') expr
    | function_call
    ;

// Expresiones que pueden ser números, identificadores, o paréntesis
expr
    : NUMERO
    | ID
    | '(' expr ')'
    | expr ('+'|'-'|'*'|'/') expr
    | expr ('>'|'<') expr
    | function_call
    ;

// Llamadas a funciones (incluyendo sqrt, sin, transpose, inverse)
function_call
    : (trig_function|'sqrt'|'transpose'|'inverse') '(' expr ')'
    ;

// Declaración de operaciones con matrices
matrix_stmt
    : 'matriz' ID '=' matrix_operation
    ;

// Definición de operaciones con matrices
matrix_operation
    : matrix
    | matrix '+' matrix
    | matrix '*' matrix
    | function_call
    ;

// Definición de matrices
matrix: '[' row (',' row)* ']';

// Filas de matrices
row: '[' expr (',' expr)* ']';

// Funciones trigonométricas
trig_function
    : 'sin' | 'cos' | 'tan' | 'asin' | 'acos' | 'atan'
    ;

// Sentencias condicionales
conditional_stmt
    : 'if' expr 'then' statement+ ('else' statement+)?
    ;

// Sentencias de bucles
loop_stmt
    : 'for' ID '=' expr 'to' expr 'do' statement+ 'end'
    | 'while' expr 'do' statement+ 'end'
    ;

// Sentencia para graficar
graph_stmt
    : 'plot' '(' expr ',' expr ')'
    ;

// Sentencias de entrada/salida de archivos
file_stmt
    : 'read' '(' STRING ')'
    | 'write' '(' STRING ',' expr ')'
    ;

// Sentencias de funciones
function_stmt
    : 'function' ID '(' param_list ')' 'return' expr
    ;

// Lista de parámetros para funciones
param_list
    : ID (',' ID)*
    | /* empty */
    ;

// Definición de tipos básicos
NUMERO: [0-9]+ ('.' [0-9]+)?;
ID: [a-zA-Z_][a-zA-Z_0-9]*;
STRING: '"' (~["\r\n])* '"';

// Espacios en blanco
WS: [ \t\r\n]+ -> skip;

// Comentarios
COMMENT: '#' ~[\r\n]* -> skip;
