player1_deck = {}
player2_deck = {}
flag = false

-- skip first line
io.read()

repeat
    line = io.read()
    if line == nil then
        break
    end
    if line == "" then
        -- skip player label
        io.read()
        line = io.read()
        flag = true
    end
    if flag == true then
        table.insert(player2_deck, tonumber(line))
    else
        table.insert(player1_deck, tonumber(line))
    end
until false

repeat
    i1, c1 = next(player1_deck)
    i2, c2 = next(player2_deck)

    c1 = table.remove(player1_deck, i1)
    c2 = table.remove(player2_deck, i2)

    if c1 > c2 then
        print("1")
        table.insert(player1_deck, c1)
        table.insert(player1_deck, c2)
        winner = player1_deck
    else
        print("2")
        table.insert(player2_deck, c2)
        table.insert(player2_deck, c1)
        winner = player2_deck
    end
until #player1_deck == 0 or #player2_deck == 0

score = 0
n = 1
for i=1,#winner do
    score = score + n * winner[#winner + 1 - i]
    n = n + 1
end
print("Part 1 = ", score)

