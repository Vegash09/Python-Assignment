def can_stack_blocks(blocks):
    start = 0
    end = len(blocks) - 1
    top = float('inf')

    while start <= end:
        if blocks[start] >= blocks[end]:
            pick = blocks[start]
            start += 1
        else:
            pick = blocks[end]
            end -= 1

        if pick > top:
            return "No"

        top = pick

    return "Yes"
