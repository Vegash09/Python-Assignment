from src.text_alignment.util import generate_logo

thickness = int(input())
char = input().strip() or 'H'

logo = generate_logo(thickness, char)
for line in logo:
    print(line)
