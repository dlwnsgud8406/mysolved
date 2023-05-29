


king_count = 1
queen_count = 1
rock_count = 2
vishop_count = 2
knight_count = 2
pawn_count = 8

king, queen, rock, vishop, knight, pawn = input().split()
king = int(king)
queen = int(queen)
rock = int(rock)
vishop = int(vishop)
knight = int(knight)
pawn = int(pawn)

print(king_count-king, queen_count-queen, rock_count-rock, vishop_count-vishop, knight_count-knight, pawn_count - pawn)