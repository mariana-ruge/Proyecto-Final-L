# Generated from ML.g4 by ANTLR 4.13.0
from antlr4 import *
if "." in __name__:
    from .MLParser import MLParser
else:
    from MLParser import MLParser

# This class defines a complete listener for a parse tree produced by MLParser.
class MLListener(ParseTreeListener):

    # Enter a parse tree produced by MLParser#program.
    def enterProgram(self, ctx:MLParser.ProgramContext):
        pass

    # Exit a parse tree produced by MLParser#program.
    def exitProgram(self, ctx:MLParser.ProgramContext):
        pass


    # Enter a parse tree produced by MLParser#statement.
    def enterStatement(self, ctx:MLParser.StatementContext):
        pass

    # Exit a parse tree produced by MLParser#statement.
    def exitStatement(self, ctx:MLParser.StatementContext):
        pass


    # Enter a parse tree produced by MLParser#arithmeticStatement.
    def enterArithmeticStatement(self, ctx:MLParser.ArithmeticStatementContext):
        pass

    # Exit a parse tree produced by MLParser#arithmeticStatement.
    def exitArithmeticStatement(self, ctx:MLParser.ArithmeticStatementContext):
        pass


    # Enter a parse tree produced by MLParser#matrixStatement.
    def enterMatrixStatement(self, ctx:MLParser.MatrixStatementContext):
        pass

    # Exit a parse tree produced by MLParser#matrixStatement.
    def exitMatrixStatement(self, ctx:MLParser.MatrixStatementContext):
        pass


    # Enter a parse tree produced by MLParser#assignment.
    def enterAssignment(self, ctx:MLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by MLParser#assignment.
    def exitAssignment(self, ctx:MLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by MLParser#incrementStatement.
    def enterIncrementStatement(self, ctx:MLParser.IncrementStatementContext):
        pass

    # Exit a parse tree produced by MLParser#incrementStatement.
    def exitIncrementStatement(self, ctx:MLParser.IncrementStatementContext):
        pass


    # Enter a parse tree produced by MLParser#loopStatement.
    def enterLoopStatement(self, ctx:MLParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by MLParser#loopStatement.
    def exitLoopStatement(self, ctx:MLParser.LoopStatementContext):
        pass


    # Enter a parse tree produced by MLParser#whileLoop.
    def enterWhileLoop(self, ctx:MLParser.WhileLoopContext):
        pass

    # Exit a parse tree produced by MLParser#whileLoop.
    def exitWhileLoop(self, ctx:MLParser.WhileLoopContext):
        pass


    # Enter a parse tree produced by MLParser#forLoop.
    def enterForLoop(self, ctx:MLParser.ForLoopContext):
        pass

    # Exit a parse tree produced by MLParser#forLoop.
    def exitForLoop(self, ctx:MLParser.ForLoopContext):
        pass


    # Enter a parse tree produced by MLParser#range.
    def enterRange(self, ctx:MLParser.RangeContext):
        pass

    # Exit a parse tree produced by MLParser#range.
    def exitRange(self, ctx:MLParser.RangeContext):
        pass


    # Enter a parse tree produced by MLParser#breakStatement.
    def enterBreakStatement(self, ctx:MLParser.BreakStatementContext):
        pass

    # Exit a parse tree produced by MLParser#breakStatement.
    def exitBreakStatement(self, ctx:MLParser.BreakStatementContext):
        pass


    # Enter a parse tree produced by MLParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:MLParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by MLParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:MLParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by MLParser#fileStatement.
    def enterFileStatement(self, ctx:MLParser.FileStatementContext):
        pass

    # Exit a parse tree produced by MLParser#fileStatement.
    def exitFileStatement(self, ctx:MLParser.FileStatementContext):
        pass


    # Enter a parse tree produced by MLParser#comparisonExpression.
    def enterComparisonExpression(self, ctx:MLParser.ComparisonExpressionContext):
        pass

    # Exit a parse tree produced by MLParser#comparisonExpression.
    def exitComparisonExpression(self, ctx:MLParser.ComparisonExpressionContext):
        pass


    # Enter a parse tree produced by MLParser#compareOp.
    def enterCompareOp(self, ctx:MLParser.CompareOpContext):
        pass

    # Exit a parse tree produced by MLParser#compareOp.
    def exitCompareOp(self, ctx:MLParser.CompareOpContext):
        pass


    # Enter a parse tree produced by MLParser#expression.
    def enterExpression(self, ctx:MLParser.ExpressionContext):
        pass

    # Exit a parse tree produced by MLParser#expression.
    def exitExpression(self, ctx:MLParser.ExpressionContext):
        pass


    # Enter a parse tree produced by MLParser#matrix.
    def enterMatrix(self, ctx:MLParser.MatrixContext):
        pass

    # Exit a parse tree produced by MLParser#matrix.
    def exitMatrix(self, ctx:MLParser.MatrixContext):
        pass


    # Enter a parse tree produced by MLParser#matrixOperation.
    def enterMatrixOperation(self, ctx:MLParser.MatrixOperationContext):
        pass

    # Exit a parse tree produced by MLParser#matrixOperation.
    def exitMatrixOperation(self, ctx:MLParser.MatrixOperationContext):
        pass


    # Enter a parse tree produced by MLParser#matrixFunction.
    def enterMatrixFunction(self, ctx:MLParser.MatrixFunctionContext):
        pass

    # Exit a parse tree produced by MLParser#matrixFunction.
    def exitMatrixFunction(self, ctx:MLParser.MatrixFunctionContext):
        pass


    # Enter a parse tree produced by MLParser#matrixAccess.
    def enterMatrixAccess(self, ctx:MLParser.MatrixAccessContext):
        pass

    # Exit a parse tree produced by MLParser#matrixAccess.
    def exitMatrixAccess(self, ctx:MLParser.MatrixAccessContext):
        pass


    # Enter a parse tree produced by MLParser#matrixRow.
    def enterMatrixRow(self, ctx:MLParser.MatrixRowContext):
        pass

    # Exit a parse tree produced by MLParser#matrixRow.
    def exitMatrixRow(self, ctx:MLParser.MatrixRowContext):
        pass


    # Enter a parse tree produced by MLParser#incrementOp.
    def enterIncrementOp(self, ctx:MLParser.IncrementOpContext):
        pass

    # Exit a parse tree produced by MLParser#incrementOp.
    def exitIncrementOp(self, ctx:MLParser.IncrementOpContext):
        pass


    # Enter a parse tree produced by MLParser#variable.
    def enterVariable(self, ctx:MLParser.VariableContext):
        pass

    # Exit a parse tree produced by MLParser#variable.
    def exitVariable(self, ctx:MLParser.VariableContext):
        pass


    # Enter a parse tree produced by MLParser#regresionStatement.
    def enterRegresionStatement(self, ctx:MLParser.RegresionStatementContext):
        pass

    # Exit a parse tree produced by MLParser#regresionStatement.
    def exitRegresionStatement(self, ctx:MLParser.RegresionStatementContext):
        pass


    # Enter a parse tree produced by MLParser#perceptronStatement.
    def enterPerceptronStatement(self, ctx:MLParser.PerceptronStatementContext):
        pass

    # Exit a parse tree produced by MLParser#perceptronStatement.
    def exitPerceptronStatement(self, ctx:MLParser.PerceptronStatementContext):
        pass



del MLParser