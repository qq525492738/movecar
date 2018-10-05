
var AlipayJSBridgeIntervalValue = setTimeout(function ()
{
    if (typeof (AlipayJSBridge) != 'undefined')
    {
        clearTimeout(AlipayJSBridgeIntervalValue);
        setAlipayTitle();
    }
}, 100);

function setAlipayTitle()
{
    AlipayJSBridge.call("showTitlebar");
    AlipayJSBridge.call("setTitle",
        {
            title: document.title
        });
}


function SetBtnShow(obj) {    
    if (obj != null) {
        obj.disabled = true;             
//        AlipayJSBridge.call('showLoading', {
//            text: '加载中',
//            delay:100
//        });     
        var timeoutShow = setTimeout(function () {
            obj.disabled = false;
          //  AlipayJSBridge.call('hideLoading');
        }, 15000);
    }
}

function showAlert(message)
{
    if (typeof (AlipayJSBridge) != 'undefined')
    {
        AlipayJSBridge.call('alert', {
            title: '提示',
            message: message,
            button: '确定'
        }, function ()
        {
        });
    }
    else
    {
        alert(message);
    }
}

/////////////////////////////////////////////////////遮罩层////////////////////////////////////////////////////////
//显示遮罩层
function showBg() {
    var bh = $("body").height();
    var bw = $("body").width();
    
    $("body").remove("#BackGroupDiv");
    $("body").remove("#divimgshow");
    var htmlstr = "<div style='width:100%;padding-top:90px; text-align:center; '>";
    htmlstr += " <div id='BackGroupDiv'  style='background-color:gray; left:0; opacity:0.5; position:absolute; top:0; z-index:3; filter:alpha(opacity=50); -moz-opacity:0.5; -khtml-opacity:0.5;'>"
    htmlstr += " </div>";
    htmlstr += " <div id='divimgshow' style='background-color:#fff; border:0px solid rgba(0,0,0, 0.4); padding:1px; position:fixed !important; position:absolute;  z-index:5; border-radius:5px; '>";
    htmlstr += " <img src='./images/Loading.gif' style='width:100%; height:100%' style='background-color:#fff; border:0px solid rgba(0,0,0, 0.4);' />";
    htmlstr += " </div>";
    htmlstr += " </div>";  
    $(htmlstr).appendTo($("body"));  
    $("body").css(
    {
        margin: 0
    });
    $("#BackGroupDiv").css({
        height: bh,
        width: bw,
        display: "block"
    });
    $("#divimgshow").css({
        height: bh * 0.2,
        width: bw * 0.2,
        top: bh * 0.4,
        left: bw * 0.4
    });   
}

//关闭灰色 jQuery 遮罩 
function closeBg() {
    $("#BackGroupDiv,#divimgshow").hide();
}



////////////////////////////保存输入的操作车牌/////////////////////
function SaveInputCarNo(appid, userid, InpuCarNo) {
    $.post("./Handler/SavePlate.ashx?app_id=" + encodeURI(appid) + "&userid=" + encodeURI(userid) + "&InpuCarNo=" + encodeURI(InpuCarNo), null);
}


 