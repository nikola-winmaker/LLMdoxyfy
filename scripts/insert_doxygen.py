# def insert_comments(original_file, function_comments, output_file):
#     with open(original_file, 'r') as f:
#         lines = f.readlines()

#     modified_lines = []
#     line_offset = 0

#     for i, line in enumerate(lines):
#         modified_lines.append(line)

#         if i + 1 in function_comments:
#             comment = function_comments[i + 1]
#             modified_lines.append(comment)

#             line_offset += len(comment.split('\n'))

#     with open(output_file, 'w') as f:
#         f.writelines(modified_lines)

#     print(f"Comments inserted successfully into '{output_file}'.")

def insert_comments(original_file, function_comments, output_file):
    with open(original_file, 'r') as f:
        lines = f.readlines()

    modified_lines = []
    line_offset = 0

    for i, line in enumerate(lines):
        if i + 1 in function_comments:
            comment = function_comments[i + 1]
            modified_lines.append(comment + '\n')
            modified_lines.append(line)
            line_offset += len(comment.split('\n')) + 1
        else:
            modified_lines.append(line)

    with open(output_file, 'w') as f:
        f.writelines(modified_lines)

    print(f"Comments inserted successfully into '{output_file}'.")
