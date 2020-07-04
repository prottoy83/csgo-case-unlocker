window.onload = function(e) {
    $("#spinning_progress").animate({'width':'100%'},5000).promise().then(function(){ 
        $(".spin_progress").hide();
        $("#result_show").show();
        $(".wp_name").show();
     });
}

function red_back(){
    if(confirm("Are you sure you want to go back? You will loose your case if not brought it yet."))
   {
    window.location.replace("index.html");
   }        
   return false;
};

function spin_case(){
    if(selected_data == null){
        alert("You must selet a box");
    }
    else{
        $(location).attr('href', '/result/'+selected_data);
    }
}