from pycparser import parse_file, c_ast, c_parser, c_generator

C_FILE = './c_files/example.c'

class FunctionVisitor(c_ast.NodeVisitor):
    def __init__(self):
        self.functions = []

    def visit_FuncDef(self, node):
        self.functions.append(node)
        self.generic_visit(node)


def preprocess_c_code(file_path):
    with open(file_path, 'r') as f:
        c_code = f.read()

    # Parse the C code into an AST
    ast = parse_file(file_path, use_cpp=True)

    # Remove comments
    comments = ast.ext[-1]
    ast.ext = ast.ext[:-1]

    # Extract functions
    function_visitor = FunctionVisitor()
    function_visitor.visit(ast)

    # Convert the modified AST back to C code
    modified_code = ast_to_code(ast)

    return modified_code, function_visitor.functions


# Convert an AST back to C code
def ast_to_code(ast):
    generator = c_generator.CGenerator()
    return generator.visit(ast)


# Example usage
code_without_comments, functions = preprocess_c_code(C_FILE)
print("Code without comments:")
print(code_without_comments)

print("\nFunctions:")
for function in functions:
    print(ast_to_code(function))
    print(f"Function and line {function.coord.line}")
    print("----------------------")

