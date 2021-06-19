var arr = (1...10000).map( {_ in Int.random(in: 1...1000)} )
arr.sort()
