from scripts.c_preproc import preprocess_c_code, ast_to_code

C_FILE = './c_files/example.c'

# Example usage
code_without_comments, functions = preprocess_c_code(C_FILE)
print("Code without comments:")
print(code_without_comments)

print("\nFunctions:")
for function in functions:
    print(ast_to_code(function))
    print(f"Function and line {function.coord.line}")
    print("----------------------")