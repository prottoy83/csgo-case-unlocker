$("#result_show").hide();
$(".wp_name").hide();
var selected_data;
var cases = document.getElementsByClassName("case");
for(var i =0;i<cases.length ;i++){
    cases[i].onclick = function(){

        var el = cases[0];
        while(el){
            if(el.tagName == "DIV"){
                el.classList.remove("focused");
            }
            el = el.nextSibling;
        }


        this.classList.add("focused");
        selected_data = this.dataset.name;
    };
}
