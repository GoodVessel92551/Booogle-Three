 var num = ''
var screen = ''
var ans = 0
document.onkeyup = function() {
    var key = event.key
    if (key == "X" || key == "x" || key == "*"){
        calc("*")
    }
    else if(key == "c"){
        calc("ac")
    }
    else if(key == "=" || key == "Enter"){
        calc("=")
    }
	else if(key == "("){
		calc("(")
	}
	else if(key == ")"){
		calc(")")
	}
	else if(key == "Backspace"){
		calc("del")
	}else{
        calc(key)
    }
}
function calc(a) {
    switch(a){
        case "ac":
            num = ""
            screen = ""
            document.getElementById("screen").innerText = "Press or Type"
            break
        case "del":
            num = num.slice(0,-1)
            screen = screen.slice(0,-1)
			if (screen == ""){
				screen = ""
				document.getElementById("screen").innerText = "Press or Type"
			}
			else{
            	document.getElementById("screen").innerText = screen
			}
            break
        case "ans":
            num += ans
            screen += ans
            document.getElementById("screen").innerText = screen
            break
        case "+":
            num = num +"+"
            screen += "+"
            document.getElementById("screen").innerText = screen
            break
        case "(":
            num = num +"("
            screen += "("
            document.getElementById("screen").innerText = screen
            break
        case ")":
            num = num +")"
            screen += ")"
            document.getElementById("screen").innerText = screen
            break
        case "-":
            num = num +"-"
            screen += "-"
            document.getElementById("screen").innerText = screen
            break
        case "*":
            num = num +"*"
            screen += "x"
            document.getElementById("screen").innerText = screen
            break
        case "/":
            num = num +"/"
            screen += "÷"
            document.getElementById("screen").innerText = screen
            break
        case "0":
            num = num +"0"
            screen += "0"
            document.getElementById("screen").innerText = screen
            break
        case "1":
            num = num +"1"
            screen += "1"
            document.getElementById("screen").innerText = screen
            break
        case "2":
            num = num +"2"
            screen += "2"
            document.getElementById("screen").innerText = screen
            break
        case "3":
            num = num +"3"
            screen += "3"
            document.getElementById("screen").innerText = screen
            break
        case "4":
            num = num +"4"
            screen += "4"
            document.getElementById("screen").innerText = screen
            break
        case "5":
            num = num +"5"
            screen += "5"
            document.getElementById("screen").innerText = screen
            break
        case "6":
            num = num +"6"
            screen += "6"
            document.getElementById("screen").innerText = screen
            break
        case "7":
            num = num +"7"
            screen += "7"
            document.getElementById("screen").innerText = screen
            break
        case "8":
            num = num +"8"
            screen += "8"
            document.getElementById("screen").innerText = screen
            break
        case "9":
            num = num +"9"
            screen += "9"
            document.getElementById("screen").innerText = screen
            break
        case ".":
            num = num +"."
            screen += "."
            document.getElementById("screen").innerText = screen
            break
        case "=":
            ans = eval(num)
            screen += " = " + ans
            document.getElementById("screen").innerText = screen
            num = ""
            screen = ""
            break
        default:
            break
    }
}