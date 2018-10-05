window.onload = function() {
    console.log("onload")

}

$(document).ready(function(){


     $("#apply").on("click" ,function(){
        $.ajax({
            type:"POST",
            url:"bind_api",
            async:false,
            data:{
                p:$("#bind_car_p").val(),
                lp:$("#car1").val()+$("#car2").val()+$("#car3").val()
            },
            dataType:"json",
            success:function(data){
                console.log(data);
                if(data.code==0){
                    window.location.reload()
                    alert("绑定成功")
                }else if(data.code==40011){
                    alert("请先登录")
                    window.open("wechat_service?path=center");
                }else{
                    alert('绑定失败')
                }

            },
            error:function(data){
                console.log(data)
                window.open("login")
            }
        
        });
        

     });



});
