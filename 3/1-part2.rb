class Route < Struct.new(:right, :down)
end

file = File.read("input.txt")
lines = file.split("\n")
routes = [(Route.new 1, 1),
          (Route.new 3, 1),
          (Route.new 5, 1),
          (Route.new 7, 1),
          (Route.new 1, 2)]
multiplier = 1
routes.each do |route|
    count = 0
    lines.each_with_index do |line, index|
        if (index % route.down != 0)
            next
        end
        char = line[(index/route.down)*route.right % line.length]
        if char == "#" then
            count = count + 1
        end
    end
    multiplier = multiplier * count
end

puts "Multiplied total of trees encountered: #{multiplier}"