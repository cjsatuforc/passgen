function gen_pass()
	v = ARGS[2]
	f_set = Any[]
	while length(f_set) != int(v)
		for i in rand(1:z)
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
		global z = length(c_set)
		gen_pass()
	elseif ARGS[1] == "-u"
		global c_set = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		global z = length(c_set)
		gen_pass()
	elseif ARGS[1] == "-lu"
		global c_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
		global z = length(c_set)
		gen_pass()
	elseif ARGS[1] == "-n"
		global c_set = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
		global z = length(c_set)
		gen_pass()
	elseif ARGS[1] == "-ln"
                global c_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                global z = length(c_set)
                gen_pass()
	elseif ARGS[1] == "-un"
                global c_set = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
                global z = length(c_set)
                gen_pass()
    elseif ARGS[1] == "-lun"
				global c_set = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
				global z = length(c_set)
				gen_pass()
	else
		println("Arguments: -l [num], -u [num]")
		break
	end
end

