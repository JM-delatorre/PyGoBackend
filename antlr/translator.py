from antlr4 import *
from .gen.Python3Lexer import Python3Lexer
from .gen.Python3Parser import Python3Parser
from .gen.CustomListener import CustomListener
import os


def translator():
    filePath = os.path.abspath("antlr/prueba.txt")
    input_stream = FileStream(filePath)
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.single_input()
    printer = CustomListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)

    

