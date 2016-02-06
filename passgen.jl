#Work In Progress#
#Passgen port to julia#
function gen_alpha()
        c_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        f_set = Any[]
        while length(f_set) != 10
                for i in rand(1:26)
                        for x in c_set[i]
                                push!(f_set, x)
                        end
                end
        end
z_set = join(f_set)
println(z_set)
end
while true
        gen_alpha()
end
