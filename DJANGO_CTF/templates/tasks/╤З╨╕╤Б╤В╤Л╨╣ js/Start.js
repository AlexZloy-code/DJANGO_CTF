let name = document.getElementById("name");
let pass = document.getElementById("password");
document.getElementById("btn").onclick = lala;
function lala(){
    if ((name.value == 'admin') && (pass.value == '')) {
        document.getElementById("error").innerHTML = 'Q1RGe0YxYWdfaTVfZmw0Z30========';
    } else if ((name.value) && (pass.value)) {
        document.getElementById("error").innerHTML = decodeURIComponent(escape('\xd0\x9e\xd1\x88\xd0\xb8\xd0\xb1\xd0\xba\xd0\xb0 \xd1\x80\xd0\xb5\xd0\xb3\xd0\xb8\xd1\x81\xd1\x82\xd1\x80\xd0\xb0\xd1\x86\xd0\xb8\xd0\xb8'))
    } else {
        document.getElementById("error").innerHTML = '';
    }
} 