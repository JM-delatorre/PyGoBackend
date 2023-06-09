from antlr4 import *
from .gen.Python3Lexer import Python3Lexer
from .gen.Python3Parser import Python3Parser
from .gen.CustomListener import CustomListener
import os


def translator(textInput):   
    input_stream = InputStream(textInput)
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()
    printer = CustomListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    return printer.print_dictionnary() 

def translatorTesting():   
    filePath = os.path.abspath("antlr/prueba.txt")
    input_stream = FileStream(filePath)
    lexer = Python3Lexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Python3Parser(stream)
    tree = parser.file_input()
    printer = CustomListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    print(printer.print_dictionnary())
    return printer.print_dictionnary() 
    

