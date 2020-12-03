file = File.read("input.txt")
lines = file.split("\n")
count = 0
lines.each_with_index do |line, index|
    char = line[index*3 % line.length]
    if char == "#" then
        count = count + 1
    end
end
puts "Trees encountered: #{count}"