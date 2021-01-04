user_grain_input = int(input("Enter Grain Insert: "))
user_draw_length_input = int(input("Enter Draw Length: "))
user_bow_poundage = int(input("Enter Bow Poundage: "))

column_pattern = [[400], [400], [400], [340], [340,300], [300], [300,260], [260]]
bow_poundage_breakpoints = [23, 28, 33, 38, 43, 48, 53, 58, 63, 69, 75, 81, 86]

row_index = None
for i, bp in enumerate(bow_poundage_breakpoints):
    if user_bow_poundage >= bp:
        row_index = i

if row_index == len(bow_poundage_breakpoints) - 1 or row_index is None:
    print("Bow poundage not supported.")

if not (23 <= user_draw_length_input <= 32):
    print("Draw length not supported.")
    
column_index = user_draw_length_input - 23

# (Max Draw Length) - (Min Draw Length) + (1 because of python index)
# 32 - 23 + 1
number_of_columns = 10
effective_row_index = row_index - (number_of_columns - 1 - column_index)
if not (0 <= effective_row_index < len(column_pattern)):
    print("Bow poundage not supported.")
    
arrow_spine = column_pattern[effective_row_index]
print(" or ".join(str(s) for s in arrow_spine) + " spine.")