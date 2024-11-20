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


    # Enter a parse tree produced by MLParser#conditionalStatement.
    def enterConditionalStatement(self, ctx:MLParser.ConditionalStatementContext):
        pass

    # Exit a parse tree produced by MLParser#conditionalStatement.
    def exitConditionalStatement(self, ctx:MLParser.ConditionalStatementContext):
        pass


    # Enter a parse tree produced by MLParser#loopStatement.
    def enterLoopStatement(self, ctx:MLParser.LoopStatementContext):
        pass

    # Exit a parse tree produced by MLParser#loopStatement.
    def exitLoopStatement(self, ctx:MLParser.LoopStatementContext):
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


    # Enter a parse tree produced by MLParser#ParenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:MLParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by MLParser#ParenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:MLParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by MLParser#AdditiveExpression.
    def enterAdditiveExpression(self, ctx:MLParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by MLParser#AdditiveExpression.
    def exitAdditiveExpression(self, ctx:MLParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by MLParser#PowerExpression.
    def enterPowerExpression(self, ctx:MLParser.PowerExpressionContext):
        pass

    # Exit a parse tree produced by MLParser#PowerExpression.
    def exitPowerExpression(self, ctx:MLParser.PowerExpressionContext):
        pass


    # Enter a parse tree produced by MLParser#MatrixAccessExpression.
    def enterMatrixAccessExpression(self, ctx:MLParser.MatrixAccessExpressionContext):
        pass

    # Exit a parse tree produced by MLParser#MatrixAccessExpression.
    def exitMatrixAccessExpression(self, ctx:MLParser.MatrixAccessExpressionContext):
        pass


    # Enter a parse tree produced by MLParser#NumberExpression.
    def enterNumberExpression(self, ctx:MLParser.NumberExpressionContext):
        pass

    # Exit a parse tree produced by MLParser#NumberExpression.
    def exitNumberExpression(self, ctx:MLParser.NumberExpressionContext):
        pass


    # Enter a parse tree produced by MLParser#VariableExpression.
    def enterVariableExpression(self, ctx:MLParser.VariableExpressionContext):
        pass

    # Exit a parse tree produced by MLParser#VariableExpression.
    def exitVariableExpression(self, ctx:MLParser.VariableExpressionContext):
        pass


    # Enter a parse tree produced by MLParser#MultiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:MLParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by MLParser#MultiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:MLParser.MultiplicativeExpressionContext):
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


    # Enter a parse tree produced by MLParser#matrix.
    def enterMatrix(self, ctx:MLParser.MatrixContext):
        pass

    # Exit a parse tree produced by MLParser#matrix.
    def exitMatrix(self, ctx:MLParser.MatrixContext):
        pass


    # Enter a parse tree produced by MLParser#matrixAccess.
    def enterMatrixAccess(self, ctx:MLParser.MatrixAccessContext):
        pass

    # Exit a parse tree produced by MLParser#matrixAccess.
    def exitMatrixAccess(self, ctx:MLParser.MatrixAccessContext):
        pass


    # Enter a parse tree produced by MLParser#variable.
    def enterVariable(self, ctx:MLParser.VariableContext):
        pass

    # Exit a parse tree produced by MLParser#variable.
    def exitVariable(self, ctx:MLParser.VariableContext):
        pass


    # Enter a parse tree produced by MLParser#range.
    def enterRange(self, ctx:MLParser.RangeContext):
        pass

    # Exit a parse tree produced by MLParser#range.
    def exitRange(self, ctx:MLParser.RangeContext):
        pass



del MLParser