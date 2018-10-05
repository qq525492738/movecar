window.onload= function(){
    var car_data = new Array("京","沪","浙","苏","粤","鲁","晋","冀","豫","川","渝","辽","吉","黑","皖","鄂","津","贵","云","桂","琼","青","新","藏","蒙","宁","甘","陕","闽","赣","湘");

    $("#car1").empty();
    
    car_data_l = car_data.length;
    for (var i=0; i < car_data_l; i++){
        if(car_data[i]!="云"){
            $("#car1").append("<option value='" + car_data[i] + "'>" + car_data[i] + "</option>")
        }else{
            $("#car1").append("<option selected value='" + car_data[i] + "'>" + car_data[i] + "</option>")
        }

};


}

$(document).ready(function(){
    console.log("ready")
	$("#car2").on("focus", function() {
        $("#car2").val("");
	});

    $("#car2").bind("input propertychange",function(event){
        $('#car2').val($('#car2').val().toUpperCase())
        console.log($("#car2").val())
        $('#car3').focus()
    });
    $("#car3").bind("input propertychange",function(event){
        $('#car3').val($('#car3').val().toUpperCase())
        if($('#car3').val().length == 6){
            $('#car3').css('font-size','12px')
        }else{
            $('#car3').css('font-size','20px')
        }
    });
     



});


