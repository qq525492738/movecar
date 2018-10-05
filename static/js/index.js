window.onload = function() {
    console.log("onload")

}

$(document).ready(function(){


     $("#call").on("click" ,function(){
        $.ajax({
            type:"POST",
            url:"inquire",
            async:false,
            data:{
                lp:$("#car1").val()+$("#car2").val()+$("#car3").val()
            },
            dataType:"json",
            success:function(data){
                console.log(data);
                if(data.code==0){
                    console.log(data.data);
                    $("#call_a").attr("href","tel:"+data.data);
                    setTimeout(function(){
                        $("#call_a")[0].click();
                    },1000);
                }else if(data.code==40404){
                    alert("对方没有绑定手机号码");
                }else if(data.code==40004){
                    alert("用户不存在");
                }else if(data.code==40005){
                    window.location.href="wechat_service";
                    window.open("wechat_service");
                }else if(data.code==40011){
                    window.open("login");
                }

            },
            error:function(data){
                console.log(data)
                window.open("login")
            }
        
        });
        

     });



});
