var id = setInterval(time, 1000)
function time() {
    const date = new Date()
    var hour = date.getHours()
    var minute = date.getMinutes()
    var second = date.getSeconds()
    hour = update(hour);
    minute = update(minute)
    second = update(second)
    function update(t) {
        if (t < 10) {
            return "0" + t
        }else{
            return t
            }
    }
    document.getElementById("navtime").innerText = hour + " : " + minute + " : " + second
}
time()
