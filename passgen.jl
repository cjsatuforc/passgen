#Work In Progress#
#Passgen port to julia#
function gen_lower()
        v = ARGS[2]
        f_set = Any[]
        while length(f_set) != int(v)
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
        if ARGS[1] == "-l"
                global c_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
                gen_lower()
        elseif ARGS[1] == "-u"
                global c_set = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
                gen_lower()
        else
                println("Arguments: -l [num]")
                break
        end
end


